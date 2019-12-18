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
import bpy
import socket
import threading
from datetime import datetime


bl_info = {
    "name": "Unreal Engine 4 Live Link",
    "author": "Tom Delaney",
    "description": "",
    "blender": (2, 81, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Animation"
}


# =====================================================
# Operators
# =====================================================
class UELL_OT_toggle_server(bpy.types.Operator):
    bl_idname = "uell.start_server"
    bl_label = "Start Live Link Server"
    bl_description = "Start broadcasting UE Live Link data"

    @classmethod
    def poll(cls, context):
        return context.scene.unreal_list

    def get_armature_name(self, mesh_object):
        if mesh_object.parent.type == 'ARMATURE':
                return mesh_object.parent.name
        return None

    @classmethod
    def startserver(self, context):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), 8888))
        s.listen(1)
        context.scene.unreal_settings.is_running = True

        while context.scene.unreal_settings.is_running:
            for tracked_object in context.scene.unreal_list:
                if bpy.data.objects[tracked_object.name].type == 'MESH':
                    object = bpy.data.objects[tracked_object.name]
                    armature_name = self.get_armature_name(self, object)
                    armature = bpy.data.objects[armature_name]
                    for bone in armature.pose.bones:
                        msg = bone.name
                        msg += " " + str(bone.location)
                        msg += " " + str(bone.scale)
                        msg += " " + str(bone.rotation_quaternion)
                        print(msg)
                else:
                    print(str(datetime.now(tz=None)) +
                          " - Broadcasting object " + tracked_object.name)

    def execute(self, context):
        if context.scene.unreal_settings.is_running:
            context.scene.unreal_settings.is_running = False
        else:
            thread = threading.Thread(target=UELL_OT_toggle_server.startserver,
                                      args=(context,))
            thread.start()

        return {'FINISHED'}


class UELL_OT_track_objects(bpy.types.Operator):
    bl_idname = "uell.track_objects"
    bl_label = "Track selected objects"
    bl_description = 'Unreal Engine Live Link will start tracking '
    'the currently selected objects'

    @classmethod
    def poll(cls, context):
        return not context.scene.unreal_settings.is_running

    def mesh_has_armature(self, mesh_object):
        if mesh_object.parent.type == 'ARMATURE':
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


# =================================
# Properties and PropertyGroups
# =================================
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


class UnrealLiveLinkData(bpy.types.PropertyGroup):
    broadcast_port: bpy.props.IntProperty(
        name="Port",
        description="Port that blender broadcasts animation data from",
        default=8888)

    is_running: bpy.props.BoolProperty(
        name="Is Running",
        description="Is the Live Link server broadcasting?",
        default=False)


# =====================================
# Class for List
# =====================================
class MY_UL_List(bpy.types.UIList):
    """Demo UIList."""
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        # We could write some code to decide which icon to use here...
        custom_icon = 'OBJECT_DATAMODE'
        if item:
            # Make sure your code supports all 3 layout types
            if self.layout_type in {'DEFAULT', 'COMPACT'}:
                layout.label(text=item.name, icon=custom_icon)
            elif self.layout_type in {'GRID'}:
                layout.alignment = 'CENTER'
                layout.label(text="", icon=custom_icon)
        else:
            print("Item to be added to list is nothing")


# ======================================
# Panel
# ======================================
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


classes = (UnrealLiveLinkData, SCENE_PT_UnrealLiveLinkPanel, ListItem, MY_UL_List,
           UELL_OT_track_objects, UELL_OT_untrack_objects,
           UELL_OT_toggle_server)


def register():
    for class_to_register in classes:
        bpy.utils.register_class(class_to_register)
    bpy.types.Scene.list_index = bpy.props.IntProperty(
        name="Index for my_list", default=0)
    bpy.types.Scene.unreal_list = bpy.props.CollectionProperty(type=ListItem)
    bpy.types.Scene.unreal_settings = bpy.props.PointerProperty(
        type=UnrealLiveLinkData)


def unregister():
    for class_to_register in classes:
        bpy.utils.unregister_class(class_to_register)


if __name__ == "__main__":
    register()
