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

# https://github.com/EpicGames/UnrealEngine/blob/4.23/Engine/Source/Runtime/Core/Public/Misc/QualifiedFrameTime.h

from .FrameRate import FrameRate
from .FrameTime import FrameTime
from .Timecode import Timecode


class QualifiedFrameTime(object):
    """
    A frame time qualified by a frame rate context
    """
    time: FrameTime
    rate: FrameRate

    def __init__(self, _in_time: FrameTime = FrameTime(),
                 _in_rate: FrameRate = FrameRate(24, 1),
                 _in_timecode: Timecode = None):
        """
        User construction from a frame time and its frame rate
        """
        if _in_timecode:
            self.time = _in_timecode.to_frame_number(_in_rate)
        else:
            self.time = _in_time
        self.rate = _in_rate

    def as_seconds(self):
        """
        Convert this frame time to a value in seconds
        """
        return self.time / self.rate

    def convert_to(self, _desired_rate: FrameRate):
        """
        Convert this frame time to a different frame rate
        """
        return self.rate.transform_time(self.time, self.rate, _desired_rate)
