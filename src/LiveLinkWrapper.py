# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from ctypes import cdll, c_double
from BlenderLiveLinkDevice import BlenderLiveLinkDevice
from BlenderLiveLinkLib import BlenderLiveLinkLib


class LiveLinkWrapper(object):

    lib = None
    lib_path = ''

    def __init__(self, lib_path):
        self.lib = cdll.LoadLibrary(lib_path)
        self.lib_path = lib_path

    def BlenderLiveLinkDevice(self):
        return BlenderLiveLinkDevice(self.lib_path)
    
    def BlenderLiveLinkLib(self):
        return BlenderLiveLinkLib(self.lib_path)
