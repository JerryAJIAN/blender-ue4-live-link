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


class SCENE_PT_UnrealLiveLinkPanel(bpy.types.Panel):
    """Creates a panel in the scene context of the properties editor"""
    bl_label = "Unreal Engine Live Link"
    bl_idname = "SCENE_PT_ue4livelink"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        layout.alignment = "RIGHT"

        scene = context.scene

        # Create a simple row.
        row = layout.row()
        row.alignment = "RIGHT"
        row.label(text="Online")
        row.operator("uell.start_server",
                     text=str(context.scene.unreal_settings.is_running))

        row = layout.row()
        row.template_list("MY_UL_List", "The_List", scene, "unreal_list",
                          scene, "list_index")
        col = row.column(align=True)
        col.operator("uell.track_objects", icon='ADD', text="")
        col.operator("uell.untrack_objects", icon='REMOVE', text="")
