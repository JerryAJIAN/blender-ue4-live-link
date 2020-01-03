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

from uuid import UUID
import time


class LiveLinkSubjectName(object):
    __name = ""
    __is_none = True

    def __str__(self):
        return self.__name

    def __eq__(self, o: object):
        return isinstance(o, LiveLinkSubjectName) and o.__name == self.__name


class LiveLinkSubjectKey(object):
    __source = None
    __subject_name = None

    def __init__(self, _source=UUID(), _subject_name=None):
        self.__source = _source
        if not _subject_name:
            _subject_name = str(_source)
        self.__subject_name = _subject_name

    def __eq__(self, o: object):
        return (isinstance(o, LiveLinkSubjectKey)
                and self.__source == o.__source
                and self.__subject_name == o.subject_name)


class LiveLinkWorldTime(object):
    __time = 0.0
    __offset = 0.0

    def __init__(self, _in_time=None, _in_offset=None):
        if _in_time and isinstance(_in_time, float):
            self.__time = time.time() - _in_time
        else:
            self.__time = time.time()

        if _in_offset and isinstance(_in_offset, float):
            self.__offset = _in_offset

    def get_offseted_time(self):
        return self.__time + self.__offset


class LiveLinkTime(object):
    __world_time = 0.0
    __scene_time = 0.0

    def __init__(self, _in_world_time=None, _in_scene_time=None):
        self.__world_time = _in_world_time
        self.__scene_time = _in_scene_time


class LiveLinkMetaData(object):
    __string_meta_data = []
    __scene_time = 0.0