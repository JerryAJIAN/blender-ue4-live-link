import ctypes as C


class BlenderLiveLinkLib(object):
    def __init__(self, lib_path):
        self.lib = C.cdll.LoadLibrary(lib_path)

        self.lib.BlenderLiveLinkLib_new.restype = C.c_void_p
        self.lib.BlenderLiveLinkLib_new.argtypes = []

        self.lib.BlenderLiveLinkLib_destroy.restype = None
        self.lib.BlenderLiveLinkLib_destroy.argtypes = [C.c_void_p]

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

        self.obj = self.lib.BlenderLiveLinkLib_new()

    def Destroy(self):
        self.lib.BlenderLiveLinkLib_destroy(self.obj)

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
