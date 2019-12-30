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


class UELL_OT_untrack_objects(bpy.types.Operator):
    bl_idname = "uell.untrack_objects"
    bl_label = "Stop tracking selected objects"
    bl_description = 'Unreal Engine Live Link will stop tracking '
    'the currently selected objects'

    @classmethod
    def poll(cls, context):
        return (context.scene.unreal_list
                and not context.scene.unreal_settings.is_running)

    def execute(self, context):
        unreal_list = context.scene.unreal_list
        index = context.scene.list_index

        unreal_list.remove(index)
        context.scene.list_index = min(max(0, index - 1), len(unreal_list) - 1)

        return {'FINISHED'}
