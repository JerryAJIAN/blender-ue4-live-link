import ctypes as C


class Foo(object):
    def __init__(self, lib_path, nbits):
        self.lib = C.cdll.LoadLibrary(lib_path)

        self.lib.Foo_new.restype = C.c_void_p
        self.lib.Foo_new.argtypes = [C.c_int32]
        self.lib.Foo_bar.restype = None
        self.lib.Foo_bar.argtypes = [C.c_void_p]

        self.nbits = C.c_int(nbits)
        self.obj = self.lib.Foo_new(self.nbits)

    def bar(self):
        self.lib.Foo_bar(self.obj)
