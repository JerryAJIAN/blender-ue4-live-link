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

# https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Source/Runtime/LiveLinkInterface/Public/LiveLinkTypes.h

from Misc.FrameRate import FrameRate
from Misc.QualifiedFrameTime import QualifiedFrameTime


class LiveLinkSubjectName(object):
    """
    Name of the subject
    """
    name: str

    def __eq__(self, o: object):
        return ((isinstance(o, LiveLinkSubjectName) and self.name == o.name)
                or (isinstance(o, str) and self.name == o))

    def __str__(self):
        return str(self.name)

    def is_none(self):
        return self.name is None
