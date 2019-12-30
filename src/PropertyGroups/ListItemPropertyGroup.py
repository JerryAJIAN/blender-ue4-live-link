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
import bpy


class ListItem(bpy.types.PropertyGroup):
    """Group of properties representing an item in the list."""
    name: bpy.props.StringProperty(
        name="Name",
        description="A name for this item",
        default="Untitled")
    random_prop: bpy.props.StringProperty(
        name="Any other property you want",
        description="",
        default="")
