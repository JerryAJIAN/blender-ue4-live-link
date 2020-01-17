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

from uuid import UUID
from time import time
from .Misc.FrameRate import FrameRate
from .Misc.QualifiedFrameTime import QualifiedFrameTime


class LiveLinkSubjectName(object):
    """
    Name of the subject
    """
    name: str

    def __init__(self, _in_name: str):
        self.name = _in_name

    def __eq__(self, o: object):
        return ((isinstance(o, LiveLinkSubjectName) and self.name == o.name)
                or (isinstance(o, str) and self.name == o))

    def __str__(self):
        return str(self.name)

    def is_none(self):
        return self.name is None


class LiveLinkSubjectKey(object):
    """
    Structure that identifies an individual subject
    """
    source: UUID
    subject_name: LiveLinkSubjectName

    def __init__(self, _in_source: UUID,
                 _in_Subject_name: str,
                 _in_rhs: object = None):
        if _in_rhs and isinstance(_in_rhs, LiveLinkSubjectKey):
            self.source = _in_rhs.source
            self.subject_name = _in_rhs.subject_name
        else:
            self.source = _in_source
            self.subject_name = LiveLinkSubjectName(_in_Subject_name)

    def __eq__(self, o: object):
        return (isinstance(o, LiveLinkSubjectKey)
                and self.source == o.source
                and self.subject_name == o.subject_name)

    def __ne__(self, o: object):
        return not (self == o)


class LiveLinkWorldTime(object):
    time: float
    offset: float

    def __init__(self, _in_time: float = None, _in_offset: float = 0.0):
        if _in_time:
            self.time = _in_time
        else:
            self.time = time()

        self.offset = _in_offset

    def get_offsetted_time(self):
        return self.time + self.offset


class LiveLinkTime(object):
    world_time: float
    scene_time: QualifiedFrameTime

    def __init__(self, _in_world_time: float,
                 _in_scene_time: QualifiedFrameTime):
        self.scene_time = _in_scene_time
        self.world_time = _in_world_time


class LiveLinkMetaData(object):
    string_metadata: list
    scene_time: QualifiedFrameTime


class LiveLinkBaseFrameData(object):
    """
    Base data structure for each frame coming in for asubject
    """
    world_time: LiveLinkWorldTime
    metadata: LiveLinkMetaData
    property_values: list


class LiveLinkBaseStaticData(object):
    """
    Base static data structure for a subject
    Use to store information that is common to every frame
    """
    property_names: list

    def find_property_value(self, _in_frame_data: LiveLinkBaseFrameData,
                            _in_property_name: str):
        """
        Returns the value of a property in the frame, None if the property
        can't be found
        """
        if len(self.property_names) == len(_in_frame_data.property_values):
            try:
                found_index = self.property_names.index(_in_property_name)
                return _in_frame_data.property_values[found_index]
            except ValueError:
                return None


class LiveLinkSubjectFrameData(object):
    """
    Static and dynamic data to be used when fetching a subject complete data
    """
    static_data: LiveLinkBaseStaticData
    frame_data: LiveLinkBaseFrameData
