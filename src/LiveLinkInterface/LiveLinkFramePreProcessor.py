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

from .LiveLinkTypes import LiveLinkBaseFrameData
from .LiveLinkRole import LiveLinkRole


class LiveLinkFramePreProcessorWorker(object):
    """
    Basic object to apply preprocessing to a live link frame.
    Inherit from it to add specific operations/options for
    a certain type of data
    Can called from any thread
    """

    def get_role(self):
        return LiveLinkRole()

    def PreProcessFrame(self, _in_frame: LiveLinkBaseFrameData):
        return _in_frame


class LiveLinkFramePreProcessor(object):
    """
    Base object to apply preprocessing to a live link frame.
    Inherit from it to add specific operations/options for
    a certain type of data
    Can only be called on main thread
    """
    worker: LiveLinkFramePreProcessorWorker

    def get_role(self):
        return LiveLinkRole()

    def fetch_worker(self):
        return LiveLinkFramePreProcessorWorker()
