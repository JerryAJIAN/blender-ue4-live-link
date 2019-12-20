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
from ctypes import cdll

class Foo(object):

    lib = None

    def __init__(self, lib_path):
        self.lib = cdll.LoadLibrary(lib_path)
        self.obj = self.lib._Z7Foo_newv()

    def bar(self, x, y, z):
        return self.lib._Z7Foo_barP3Fooiii(self.obj, x, y, z)
