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

from .LiveLinkTypes import (LiveLinkBaseStaticData,
                            LiveLinkBaseFrameData,
                            LiveLinkSubjectName)


class LiveLinkRole(object):
    """
    Basic object to extend the meaning of outgoing live link frames
    """

    def get_display_name(self):
        return ""

    def is_static_data_valid(self, _in_static_data: LiveLinkBaseStaticData):
        return True

    def is_frame_data_valid(self, _in_frame_data: LiveLinkBaseFrameData):
        return True


class LiveLinkSubjectRepresentation(object):
    subject: LiveLinkSubjectName
    role: LiveLinkRole

    def __eq__(self, o: object):
        return (isinstance(o, LiveLinkSubjectRepresentation)
                and self.subject == o.subject
                and self.role == o.role)
