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


from ctypes import cdll, c_int

class BlenderLiveLinkDevice(object):

    lib = None
    blld_ptr = None

    def __init__(self, lib_path):
        self.lib = cdll.LoadLibrary(lib_path)
        self.blld_ptr = self.lib.BlenderLiveLink_Construct()
        self.lib.BlenderLiveLink_GetNextUID.restype = c_int

    def Destroy(self):
        self.lib.BlenderLiveLink_Destroy(self.blld_ptr)

    def Done(self):
        self.lib.BlenderLiveLink_Done(self.blld_ptr)

    def GetCurrentSampleRateIndex(self):
        self.lib.BlenderLiveLink_GetCurrentSampleRateIndex(self.blld_ptr)

    def GetNextUID(self):
        self.lib.BlenderLiveLink_GetNextUID(self.blld_ptr)
