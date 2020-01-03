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
from sys import float_info
from .FrameNumber import FrameNumber


class FrameTime(object):
    frame_number: FrameNumber
    __sub_frame: float

    def __init__(self, _in_frame_number=None, _in_sub_frame=None):
        if _in_frame_number and isinstance(_in_frame_number, FrameNumber):
            self.frame_number = _in_frame_number
        elif _in_frame_number and isinstance(_in_frame_number, int):
            self.frame_number = FrameNumber(_in_frame_number)

        if _in_sub_frame:
            self.__sub_frame = _in_sub_frame

    def get_frame(self):
        return self.frame_number

    def get_sub_frame(self):
        return self.__sub_frame

    def floor_to_frame(self):
        return self.frame_number

    def ceil_to_frame(self):
        return (self.frame_number if self.__sub_frame == 0.0
                else self.frame_number+1)

    def round_to_frame(self):
        return (self.frame_number if self.__sub_frame < 0.5
                else self.__sub_frame+1)

    def as_decimal(self):
        """
        Retrieve a decimal representation of this frame time
        Sub frames are always added to the current frame number,
        so for negative frame times, a time of -10 [sub frame 0.25]
        will yield a decimal value of -9.75
        """
        return self.frame_number.get_value() + self.__sub_frame

    def from_decimal(self, _in_decimal_frame):
        """
        Convert a decimal representation to a frame time
        Note that subframes are always positive, so negative
        decimal representations result in an inverted sub frame
        and floored frame number
        """
        new_frame = math.floor(_in_decimal_frame)

        # Ensure fractional parts above the highest sub frame
        # float precision do not round to 0.0
        fraction = _in_decimal_frame - math.floor(_in_decimal_frame)

        # clamp = max(min(value, max_value), min_value)
        return FrameTime(new_frame,
                         max(min(fraction, float_info.max), float_info.min))

    def __eq__(self, o: object):
        """
        A FrameTime is equivalent to another FrameTime if they have
        the same FrameNumber and SubFrame
        """
        return (isinstance(o, FrameTime)
                and self.frame_number == o.frame_number
                and self.__sub_frame == o.__sub_frame)

    def __ne__(self, o: object):
        """
        A FrameTime is not equivalent to another FrameTime if either
        the FrameNumber or SubFrame are different
        """
        return (not isinstance(o, FrameTime)
                or self.frame_number != o.frame_number
                or self.__sub_frame != o.__sub_frame)

    def __gt__(self, o: object):
        """
        A FrameTime is greater if its FrameNumber is greater,
        or if its FrameNumber is equal and its SubFrame is greater.
        If the rhs is not a FrameTime, a TypeError is thrown
        """
        if not isinstance(o, FrameTime):
            raise TypeError()
        return (self.frame_number > o.frame_number
                or (self.frame_number == o.frame_number
                    and self.__sub_frame > o.__sub_frame))

    def __ge__(self, o: object):
        """
        A FrameTime is greater or equal if its FrameNumber is greater,
        its FrameNumber is equal and its SubFrame is greater or equal.
        If the rhs is not a FrameTime, a TypeError is thrown
        """
        if not isinstance(o, FrameTime):
            raise TypeError()
        return (self.frame_number > o.frame_number
                or (self.frame_number == o.frame_number
                    and self.__sub_frame >= o.__sub_frame))

    def __lt__(self, o: object):
        """
        A FrameTime is less than if its FrameNumber is less,
        or its FrameNumber is equal and its SubFrame is less.
        If the rhs is not a FrameTime, a TypeError is thrown
        """
        if not isinstance(o, FrameTime):
            raise TypeError()
        return (self.frame_number < o.frame_number
                or (self.frame_number == o.frame_number
                    and self.__sub_frame == o.__sub_frame))

    def __le__(self, o: object):
        """
        A FrameTime is lesser or equal if its FrameNumber is less,
        its FrameNumber is equal and its SubFrame is less or equal.
        If the rhs is not a FrameTime, a TypeError is thrown
        """
        if not isinstance(o, FrameTime):
            raise TypeError()
        return (self.frame_number < o.frame_number
                or (self.frame_number == o.frame_number
                    and self.__sub_frame <= o.__sub_frame))

    def __iadd__(self, o: object):
        if isinstance(o, FrameTime):
            new_sub_frame = self.__sub_frame + o.__sub_frame
            new_frame_num = (self.frame_number + o.frame_number
                             + FrameNumber(math.floor(new_sub_frame)))
            # FMath::Frac(x) = x - math.floor(x)
            return FrameTime(new_frame_num,
                             (new_sub_frame - math.floor(new_sub_frame)))
        else:
            raise TypeError()

    def __add__(self, o: object):
        if isinstance(o, FrameTime):
            new_sub_frame = self.__sub_frame + o.__sub_frame
            new_frame_num = (self.frame_number + o.frame_number
                             + FrameNumber(math.floor(new_sub_frame)))
            # FMath::Frac(x) = x - math.floor(x)
            return FrameTime(new_frame_num,
                             (new_sub_frame - math.floor(new_sub_frame)))
        else:
            raise TypeError()
