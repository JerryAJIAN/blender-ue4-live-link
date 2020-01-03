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

# https://github.com/EpicGames/UnrealEngine/blob/4.23/Engine/Source/Runtime/Core/Public/Misc/FrameRate.h
from .FrameNumber import FrameNumber
from .FrameTime import FrameTime
import math
from sys import float_info


class FrameRate(object):
    numerator: int
    denominator: int

    def __init__(self, _numerator: int, _denominator: int):
        self.numerator = _numerator
        self.denominator = _denominator

    def is_valid(self):
        """
        Verify that this frame rate is valid to use
        """
        return self.denominator > 0

    def as_interval(self):
        """
        Get the decimal representation of this framerate's interval.
        Returns the time in seconds for a single frame under this frame rate
        """
        return self.denominator / self.numerator

    def as_decimal(self):
        """
        Get the decimal representation of this framerate.
        Returns the number of frames per second
        """
        return self.numerator / self.denominator

    def as_seconds(self, _frame_time: FrameTime, _frame_number: FrameNumber):
        """
        Convert the specified time in seconds to a frame number by rounding
        down to the nearest integer.

        Param: _frame_time
        Param: _frame_number  The frame number to convert

        Returns the number of seconds that the specified frame
        number represents
        """
        int_part = (_frame_time.get_frame().get_value()
                    * int(self.__denominator))
        float_part = _frame_time.get_sub_frame() * self.denominator

        return (float(int_part) + float_part) / self.numerator

    def as_frame_time(self, _in_time_seconds: float):
        """
        Convert the specified time in seconds to a frame number by rounding
        down to the nearest integer

        Param: _in_time_seconds  The time to convert in seconds

        Returns a frame number that represents the supplied time. Rounded
        down to the nearest integer
        """
        time_as_frame = ((_in_time_seconds * self.numerator)
                         / self.denominator)
        frame_number = math.floor(time_as_frame)
        sub_frame = time_as_frame - math.floor(time_as_frame)
        if sub_frame > 0:
            sub_frame = min(sub_frame, float_info.max)
        return FrameTime(frame_number, sub_frame)

    def as_frame_number(self, _in_time_seconds: float):
        """
        Convert the specified time in seconds to a frame number by rounding
        down to the nearest integer.

        Param: _in_tim_seconds The time to convert in seconds
        Returns a frame number that represents the supplied time. Rounded
        down to the nearest integer.
        """
        time_as_frame = ((_in_time_seconds * self.numerator)
                         / self.denominator)
        return FrameNumber(math.floor(time_as_frame))

    def is_multiple_of(self, o: object):
        """
        Checks whether this frame rate is a multiple of another
        """
        o = FrameRate(o)
        common_val_a = int(int(self.numerator) * o.denominator)
        common_val_b = int(int(o.numerator) * self.denominator)
        return (common_val_a <= common_val_b
                and common_val_b % common_val_a == 0)

    def is_factor_of(self, o: object):
        """
        Check whether this frame rate is a factor of another
        """
        o = FrameRate(o)
        return o.is_multiple_of(self)

    def convert_frame_time(self,
                           _source_time: FrameTime,
                           _source_rate: object,
                           _destination_rate: object):
        if (isinstance(_source_rate, FrameRate)
           and isinstance(_destination_rate, FrameRate)
           and _source_rate == _destination_rate):
            return _source_rate

        _source_rate = FrameRate(_source_rate.numerator,
                                 _source_rate.denominator)
        _destination_rate = FrameRate(_destination_rate.numerator,
                                      _destination_rate.denominator)

        # We want NewTime =SourceTime * (DestinationRate/SourceRate)
        # And want to  limit conversions and keep int precision
        # as much as possible
        new_numerator = math.floor(_destination_rate.numerator
                                   * _source_rate.denominator)
        new_denominator = math.floor(_destination_rate.denominator
                                     * _source_rate.numerator)
        new_numerator = float(new_numerator)
        new_denominator = float(new_denominator)
        # Now the integerpart may have a float part, and then the
        # float part may have an integer part, so we add the extra
        # float from the integer part to the float part and then
        # add back any extra integer to integer part
        int_part = ((int(_source_time.get_frame().get_value())
                    * new_numerator) / new_denominator)
        int_float_part = (((float(_source_time.get_frame().get_value())
                          * new_numerator) / new_denominator)
                          - float(int_part))
        float_part = ((_source_time.get_sub_frame() * new_numerator)
                      / new_denominator) + int_float_part
        float_part_floored = math.floor(float_part)
        float_as_int = int(float_part_floored)
        int_part += float_as_int
        sub_frame = float_part - float_part_floored
        if sub_frame > 0:
            sub_frame = min(sub_frame, 0.999999940)

        return FrameTime(int(int_part), sub_frame)

    def transform_time(self,
                       _source_time: FrameTime,
                       _source_rate: object,
                       _destination_rate: object):
        return self.convert_frame_time(_source_time,
                                       _source_rate,
                                       _destination_rate)

    def snap(self, _source_time: FrameTime, _source_rate: object,
             _snap_to_rate: object):
        return self.convert_frame_time(self.convert_frame_time(
            _source_time, _source_rate, _snap_to_rate
        ).round_to_frame(), _snap_to_rate, _source_rate)

    def reciprocal(self):
        """
        Get the reciprocal of this frame rate
        """
        return FrameRate(self.__denominator, self.__numerator)
