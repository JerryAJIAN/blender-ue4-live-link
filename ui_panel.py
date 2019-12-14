import bpy

class UnrealLiveLinkData(bpy.types.PropertyGroup):
    is_running: bpy.props.BoolProperty(
        name="Is Running",
        description="Is the Live Link server broadcasting?",
        default=False)



class UnrealLiveLinkPanel(bpy.types.Panel):
    """Creates a panel in the scene context of the properties editor"""
    bl_label = "Unreal Engine Live Link"
    bl_idname = "SCENE_PT_ue4livelink"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        layout.label(text=" Online:")

        row = layout.row()
        layout.prop(scene.unreal_settings, 'is_running', text="Is Running")



def register():
    bpy.utils.register_class(UnrealLiveLinkData)
    bpy.types.Scene.unreal_settings = bpy.props.PointerProperty(type=UnrealLiveLinkData)
    bpy.utils.register_class(UnrealLiveLinkPanel)


def unregister():
    bpy.utils.unregister_class(UnrealLiveLinkPanel)


if __name__ == "__main__":
    register()
