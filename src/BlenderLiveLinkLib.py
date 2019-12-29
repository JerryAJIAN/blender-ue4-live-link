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


class BlenderLiveLinkLib(object):
    def __init__(self, lib_path):
        self.lib = C.cdll.LoadLibrary(lib_path)

        self.lib.BlenderLiveLinkLib_New.restype = C.c_void_p
        self.lib.BlenderLiveLinkLib_New.argtypes = []

        self.lib.BlenderLiveLinkLib_Destroy.restype = None
        self.lib.BlenderLiveLinkLib_Destroy.argtypes = [C.c_void_p]

        self.lib.BlenderLiveLinkLib_Init.restype = C.c_bool
        self.lib.BlenderLiveLinkLib_Init.argtypes = [C.c_void_p]

        self.lib.BlenderLiveLinkLib_Open.restype = C.c_bool
        self.lib.BlenderLiveLinkLib_Open.argtypes = [C.c_void_p]

        self.lib.BlenderLiveLinkLib_Ready.restype = C.c_bool
        self.lib.BlenderLiveLinkLib_Ready.argtypes = [C.c_void_p]

        self.lib.BlenderLiveLinkLib_Close.restype = C.c_bool
        self.lib.BlenderLiveLinkLib_Close.argtypes = [C.c_void_p]

        self.lib.BlenderLiveLinkLib_Release.restype = C.c_bool
        self.lib.BlenderLiveLinkLib_Release.argtypes = [C.c_void_p]

        self.obj = self.lib.BlenderLiveLinkLib_New()

    def Destroy(self):
        self.lib.BlenderLiveLinkLib_Destroy(self.obj)

    def Init(self):
        return self.lib.BlenderLiveLinkLib_Init(self.obj)

    def Open(self):
        return self.lib.BlenderLiveLinkLib_Open(self.obj)

    def Ready(self):
        return self.lib.BlenderLiveLinkLib_Ready(self.obj)

    def Close(self):
        return self.lib.BlenderLiveLinkLib_Close(self.obj)

    def Release(self):
        return self.lib.BlenderLiveLinkLib_Release(self.obj)
