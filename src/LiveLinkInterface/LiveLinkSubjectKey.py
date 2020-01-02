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
