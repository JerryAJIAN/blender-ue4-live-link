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
import ctypes as C

class BlenderLiveLinkDevice(object):
    def __init__(self, lib_path):
        self.lib = C.cdll.LoadLibrary(lib_path)

        self.lib.BlenderLiveLink_New.restype = C.c_void_p
        self.lib.BlenderLiveLink_New.argtypes = []

        self.lib.BlenderLiveLink_Destroy.restype = None
        self.lib.BlenderLiveLink_Destroy.argtypes = [C.c_void_p]

        self.lib.BlenderLiveLink_Start.restype = None
        self.lib.BlenderLiveLink_Start.argtypes = [C.c_void_p]

        self.lib.BlenderLiveLink_Stop.restype = None
        self.lib.BlenderLiveLink_Stop.argtypes = [C.c_void_p]

        self.obj = self.lib.BlenderLiveLink_New()

    def Destroy(self):
        self.lib.BlenderLiveLink_Destroy(self.obj)

    def Start(self):
        self.lib.BlenderLiveLink_Start(self.obj)

    def Stop(self):
        self.lib.BlenderLiveLink_Stop(self.obj)
