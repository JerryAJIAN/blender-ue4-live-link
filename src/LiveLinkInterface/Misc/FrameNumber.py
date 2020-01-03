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


class FrameNumber(object):
    """Represents a Frame of a scene/animation with an integer"""
    __value: int

    def __init__(self, _in_value):
        """A FrameNumber must be constructed with an int"""
        if isinstance(_in_value, int):
            self.__value = _in_value
        else:
            raise TypeError()

    # friend FFrameNumber operator+(FFrameNumber A, FFrameNumber B)
    def __add__(self, o: object):
        """
        A FrameNumber can be added to an int, float or FrameNumber.
        A float will be floored before being added
        """
        if isinstance(o, float) or isinstance(o, int):
            return FrameNumber(self.__value + math.floor(o))
        elif isinstance(o, FrameNumber):
            return FrameNumber(self.__value + o.__value)
        else:
            raise TypeError

    # friend FFrameNumber operator-(FFrameNumber A, FFrameNumber B)
    def __sub__(self, o: object):
        """
        A FrameNumber can have an int, float, or FrameNumber
        subtracted from it. A float will be floored before being
        subtracted.
        """
        if isinstance(o, float) or isinstance(o, int):
            return FrameNumber(self.__value - math.floor(o))
        elif isinstance(o, FrameNumber):
            return FrameNumber(self.__value - o.__value)
        else:
            raise TypeError()

    # friend FFrameNumber operator*(FFrameNumber A, float Scalar)
    def __mul__(self, o: object):
        if isinstance(o, int):
            return FrameNumber(self.__value * math.floor(o))
        elif isinstance(o, FrameNumber):
            return FrameNumber(self.__value * o.__value)
        else:
            raise TypeError()

    # friend FFrameNumber operator/(FFrameNumber A, float Scalar)
    def __truediv__(self, o: object):
        if isinstance(o, float) or isinstance(o, int):
            return FrameNumber(self.__value // math.floor(o))
        elif isinstance(o, FrameNumber):
            return FrameNumber(self.__value // o.__value)
        else:
            raise TypeError()

    def __floordiv__(self, o: object):
        if isinstance(o, float) or isinstance(o, int):
            return FrameNumber(self.__value // math.floor(o))
        elif isinstance(o, FrameNumber):
            return FrameNumber(self.__value // o.__value)
        else:
            raise TypeError()

    # FFrameNumber& operator+=(FFrameNumber RHS)
    def __iadd__(self, o: object):
        if isinstance(o, float) or isinstance(o, int):
            return FrameNumber(self.__value + math.floor(o))
        elif isinstance(o, FrameNumber):
            return FrameNumber(self.__value + o.__value)
        else:
            raise TypeError()

    # FFrameNumber& operator-=(FFrameNumber RHS)
    def __isub__(self, o: object):
        if isinstance(o, float) or isinstance(o, int):
            return FrameNumber(self.__value - math.floor(o))
        elif isinstance(o, FrameNumber):
            return FrameNumber(self.__value - o.__value)
        else:
            raise TypeError()

    # friend bool operator==(FFrameNumber A, FFrameNumber B)
    def __eq__(self, o: object):
        return ((isinstance(o, FrameNumber) and self.__value == o.__value)
                or (isinstance(o, int) and self.__value == o))

    # friend bool operator!=(FFrameNumber A, FFrameNumber B)
    def __ne__(self, o: object):
        return not isinstance(o, FrameNumber) or self.__value != o.__value

    # friend bool operator< (FFrameNumber A, FFrameNumber B)
    def __lt__(self, o: object):
        if isinstance(o, FrameNumber):
            return self.__value < o.__value
        elif isinstance(o, float) or isinstance(o, int):
            return self.__value < o
        else:
            raise TypeError()

    # friend bool operator> (FFrameNumber A, FFrameNumber B)
    def __gt__(self, o: object):
        if isinstance(o, FrameNumber):
            return self.__value > o.__value
        elif isinstance(o, float) or isinstance(o, int):
            return self.__value > o
        else:
            raise TypeError()

    # friend bool operator<=(FFrameNumber A, FFrameNumber B)
    def __le__(self, o: object):
        if isinstance(o, FrameNumber):
            return self.__value <= o.__value
        elif isinstance(o, float) or isinstance(o, int):
            return self.__value <= o
        else:
            raise TypeError()

    # friend bool operator>=(FFrameNumber A, FFrameNumber B)
    def __ge__(self, o: object):
        if isinstance(o, FrameNumber):
            return self.__value >= o.__value
        elif isinstance(o, float) or isinstance(o, int):
            return self.__value >= o
        else:
            raise TypeError()

    def __neg__(self):
        return FrameNumber(-self.__value)

    def __pos__(self):
        return FrameNumber(+self.__value)

    def __invert__(self):
        return FrameNumber(~self.__value)

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        return self.__value

    def set_value(self, _in_value):
        self.__value = math.floor(_in_value)
