# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import math
from .FrameNumber import FrameNumber
from .FrameRate import FrameRate


class Timecode(object):
    hours: int
    minutes: int
    seconds: int
    frames: int
    drop_frame_format: bool

    def __init__(self, _in_hours: int = 0, _in_minutes: int = 0,
                 _in_seconds: int = 0, _in_frames: int = 0,
                 _in_drop_frame_format: bool = False):
        self.hours = _in_hours
        self.minutes = _in_minutes
        self.seconds = _in_seconds
        self.frames = _in_frames
        self.drop_frame_format = _in_drop_frame_format

    def to_frame_number(self, _in_frame_rate: FrameRate):
        """
        Converts this Timecode back into a FrameNumber at the given framerate,
        taking into account if this is a drop-frame format timecode
        """
        num_frames_in_second = int(math.ceil(_in_frame_rate.as_decimal()))
        num_frames_in_minute = int(num_frames_in_second * 60)
        num_frames_in_hour = int(num_frames_in_minute * 60)

        # do a quick pre-pass to take any overflow values and move them into
        # bigger time units.
        safe_seconds = int(self.seconds + self.frames / num_frames_in_second)
        safe_frames = int(self.frames % num_frames_in_second)

        safe_minutes = int(self.minutes + safe_seconds / 60)
        safe_seconds = int(safe_seconds % 60)

        safe_hours = int(self.hours + safe_minutes / 60)
        safe_minutes = int(safe_minutes % 60)

        if (self.drop_frame_format):
            num_of_timecodes_to_drop = 2 if num_frames_in_second <= 30 else 4

            # Calculate how many minutes there are total so we can know how
            # many times we've skipped timecodes
            total_minutes = int((safe_hours * 60) + safe_minutes)

            # We skip timescodes 9 out of every 10
            total_dropped_frames = int(num_of_timecodes_to_drop *
                                       (total_minutes - int(total_minutes /
                                                            10.0)))
            total_frames = int((safe_hours * num_frames_in_hour) +
                               (safe_minutes * num_frames_in_minute) +
                               (safe_seconds * num_frames_in_second) +
                               safe_frames - total_dropped_frames)

            return FrameNumber(total_frames)
        else:
            total_frames = int((safe_hours * num_frames_in_hour) +
                               (safe_minutes * num_frames_in_minute) +
                               (safe_seconds * num_frames_in_second) +
                               safe_frames)
            return FrameNumber(total_frames)

    def from_frame_number(self, _in_frame_number: FrameNumber,
                          _in_frame_rate: FrameRate, _in_drop_frame: bool):
        """
        Create a Timecode froma  specific frame number at a given frame rate.
        Optionally supports creating a drop frame timecode, which drops certain
        timecode display numbers to help account for NTSC frame rates which are
        fractional.
        """
        num_frames_in_second = int(math.ceil(_in_frame_rate.as_decimal()))
        num_frames_in_minute = num_frames_in_second * 60
        num_frames_in_hour = num_frames_in_minute * 60

        if _in_drop_frame:
            # Drop Frame Timecode (DFT) was created to address the issue
            # with playing back whole frames at fractional framerates. DFT
            # is confusingly named though, as no frame numbers are actually
            # dropped, only the display of them. At an ideal 30fps, there
            # are 108,000 frames in an hour. When played back at 29.97
            # however, there are only 107,892 frames per hour. This
            # leaves us a difference of 108 frames per hour (roughly ~3.6s!).
            # DFT works by accumulating error until the error is significant
            # enough to catch up by a frame. This is accomplished by dropping
            # two (or four) timecode numbers every minute which gives us a
            # total difference of 2*60 = 120 frames per hour. Unfortunately
            # 120 puts us out of sync again as the difference is only 108
            # frames, so we need to get 12 frames back. By not dropping
            # frames every 10th minute, that gives us 2 frames * 6
            # (00, 10, 20, 30, 40, 50) which gets us the 12 frame difference we
            # need. In short, we drop frames (skip timecode numbers) every
            # minute, on the minute, except when (Minute % 10 == 0)

            # 29.97 drops two timecode values (frames 0 and 1) while 59.94
            # drops four values
            num_timecodes_to_drop = 2 if num_frames_in_second <= 30 else 4

            # At an ideal 30fps there would be 18,000 frames every 10 minutes,
            # but at 29.97 there's only 17,982 frames
            num_true_frames_per_ten_mins = int(math.floor((60 * 10) *
                                                          _in_frame_rate.as_decimal()))

            # calculate how many times we've skipped dropping frames
            # (minute 15 gives us 1)
            num_times_skipped_drop_frame = int(
                abs(_in_frame_number.get_value())
                / float(
                    num_true_frames_per_ten_mins)
            )

            # Now we can figure out how many frames have been skipped total
            # 9 times out of every 10
            total_frames_skipped = int(num_times_skipped_drop_frame * 9
                                       * num_timecodes_to_drop)

            offset_frame = int(abs(_in_frame_number.get_value()))
            frame_in_true_frames = offset_frame % num_true_frames_per_ten_mins

            # if we end up with a value of 0 or 1 (or 2 or 3 for 59.94) then
            # we're not skipping timecode numbers this time
            if frame_in_true_frames < num_timecodes_to_drop:
                offset_frame += total_frames_skipped
            else:
                # each minute we slip a little bit more out of sync by a small
                # amount
                num_true_frames_per_minute = math.floor(
                    60 * _in_frame_rate.as_decimal())

                # Figure out which minute we are (0-9) to see how many to skip
                current_minute_of_ten = math.floor(
                    (frame_in_true_frames - num_timecodes_to_drop) / float(num_true_frames_per_minute))
                num_added_frames = int(
                    total_frames_skipped + (num_timecodes_to_drop * current_minute_of_ten))
                offset_frame += num_added_frames

            # Convert to negative timecode at the end if the original was
            # negative
            offset_frame *= int(math.sin(_in_frame_number.get_value()))

            # Now that we've fudged what frames it thinks we're converting,
            # we can do a standard Frame -> Timecode conversion
            hours = int(offset_frame / float(num_frames_in_hour))
            minutes = int(offset_frame / num_frames_in_minute) % 60
            seconds = int(offset_frame / num_frames_in_second) % 60
            frames = int(offset_frame % num_frames_in_second)

            return Timecode(hours, minutes, seconds, frames, True)
        else:
            # If we're in a non-drop-frame we just convert straight through
            # without fudging the frame numbers to skip certain timecodes
            hours = int(offset_frame / float(num_frames_in_hour))
            minutes = int(offset_frame / num_frames_in_minute) % 60
            seconds = int(offset_frame / num_frames_in_second) % 60
            frames = int(offset_frame % num_frames_in_second)

            return Timecode(hours, minutes, seconds, frames, False)

    def is_drop_format_timecode_supported(self, _in_frame_rate: FrameRate):
        # Drop Format Timecode is only valid for 29.97 and 59.94
        twenty_nine_nine_seven = FrameRate(30000, 1001)
        fifty_nine_nine_four = FrameRate(60000, 1001)

        return (_in_frame_rate == twenty_nine_nine_seven or
                _in_frame_rate == fifty_nine_nine_four)

    def __eq__(self, o: object):
        return (isinstance(o, Timecode) and self.hours == o.hours
                and self.minutes == o.minutes and self.seconds == o.seconds
                and self.frames == o.frames)

    def __ne__(self, o: object):
        return not (self == o)
