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
import threading
from datetime import datetime
from UE4LiveLink.LiveLinkWrapper import LiveLinkWrapper


class UELL_OT_toggle_server(bpy.types.Operator):
    bl_idname = "uell.start_server"
    bl_label = "Start Live Link Server"
    bl_description = "Start broadcasting UE Live Link data"

    @classmethod
    def poll(cls, context):
        return context.scene.unreal_list

    def get_armature_name(self, mesh_object):
        if mesh_object.parent and mesh_object.parent.type == 'ARMATURE':
                return mesh_object.parent.name
        return None

    @classmethod
    def startserver(self, context):
        context.scene.unreal_settings.is_running = True
        if not hasattr(self, 'wrapper'):
            self.wrapper = LiveLinkWrapper.LiveLinkWrapper('/media/tomd/Storage/engines/UnrealEngine/4.23/Engine/Source/Programs/BlenderLiveLink/Binaries/libBlenderLiveLinkPlugin.so')
            self.device = self.wrapper.BlenderLiveLinkDevice()
            self.lib = self.wrapper.BlenderLiveLinkLib()
            self.lib.Init()

        self.device.Start()

        # while context.scene.unreal_settings.is_running:
            # for tracked_object in context.scene.unreal_list:
            #     if bpy.data.objects[tracked_object.name].type == 'MESH':
            #         object = bpy.data.objects[tracked_object.name]
            #         armature_name = self.get_armature_name(self, object)
            #         armature = bpy.data.objects[armature_name]
            #         for bone in armature.pose.bones:
            #             msg = bone.name
            #             msg += " " + str(bone.location)
            #             msg += " " + str(bone.scale)
            #             msg += " " + str(bone.rotation_quaternion)
            #             print(msg)
            #     else:
            #         print(str(datetime.now(tz=None)) +
            #               " - Broadcasting object " + tracked_object.name)

    def execute(self, context):
        if context.scene.unreal_settings.is_running:
            self.device.Stop()
            context.scene.unreal_settings.is_running = False
        else:
            thread = threading.Thread(target=UELL_OT_toggle_server.startserver,
                                      args=(context,))
            thread.start()

        return {'FINISHED'}
