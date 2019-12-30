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


class UELL_OT_track_objects(bpy.types.Operator):
    bl_idname = "uell.track_objects"
    bl_label = "Track selected objects"
    bl_description = 'Unreal Engine Live Link will start tracking '
    'the currently selected objects'

    @classmethod
    def poll(cls, context):
        return not context.scene.unreal_settings.is_running

    def mesh_has_armature(self, mesh_object):
        if mesh_object.parent and mesh_object.parent.type == 'ARMATURE':
            return True
        return False

    def execute(self, context):
        unreal_list = context.scene.unreal_list
        for object in context.selected_objects:
            if ((object.type == 'MESH' and self.mesh_has_armature(object)) or
               object.type == 'CAMERA'):
                if object.name not in unreal_list.keys():
                    print("adding object " + object.name)
                    context.scene.unreal_list.add()
                    unreal_list[len(unreal_list) - 1].name = object.name
                else:
                    print(object.name + " is already being tracked")
        return {'FINISHED'}
