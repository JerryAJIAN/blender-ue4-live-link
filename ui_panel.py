import bpy

class StreamObject(bpy.types.PropertyGroup):
    subject_name: bpy.props.StringProperty(
        name="Subject Name",
        description="Name of the subject that will be sent to UE4")
    
    is_active: bpy.props.BoolProperty(
        name="Is Active",
        description="Should data for this object be streamed",
        default=True)
        
class ListItem(bpy.types.PropertyGroup): 
    """Group of properties representing an item in the list."""
    name = bpy.props.StringProperty(
        name="Name",
        description="A name for this item",
        default="Untitled")
        
    random_prop = bpy.props.StringProperty(
        name="Any other property you want",
        description="",
        default="")
        
class MY_UL_List(bpy.types.UIList):
    """Demo UIList."""
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        # We could write some code to decide which icon to use here...
        custom_icon = 'OBJECT_DATAMODE'
        # Make sure your code supports all 3 layout types 
        if self.layout_type in {'DEFAULT', 'COMPACT'}: 
            layout.label(item.name, icon = custom_icon) 
        elif self.layout_type in {'GRID'}: 
            layout.alignment = 'CENTER' 
            layout.label("", icon = custom_icon)


class UnrealLiveLinkData(bpy.types.PropertyGroup):
    broadcast_port: bpy.props.IntProperty(
        name="Port",
        description="Port that blender broadcasts animation data from",
        default=8888)
        
    is_running: bpy.props.BoolProperty(
        name="Is Running",
        description="Is the Live Link server broadcasting?",
        default=False)
        
    streamed_objects: bpy.props.CollectionProperty(
        name="Streamed Objects",
        description="Objects that will be streamed to UE4",
        type=StreamObject)


class UnrealLiveLinkPanel(bpy.types.Panel):
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
        row.label(text="Online                       ")
        row.prop(scene.unreal_settings, 'is_running', text="")
        
        row = layout.row()
        row.alignment = "RIGHT"
        row.label(text="Broadcast Port")
        row.prop(scene.unreal_settings, 'broadcast_port', text="")
        
        row = layout.row()
        row.template_list("MY_UL_List", "The_List", scene, "unreal_list", scene, "list_index")


def register():
    bpy.utils.register_class(StreamObject)
    bpy.utils.register_class(UnrealLiveLinkData)
    bpy.utils.register_class(UnrealLiveLinkPanel)
    bpy.utils.register_class(ListItem)
    bpy.utils.register_class(MY_UL_List)
    
    
    bpy.types.Scene.list_index = bpy.props.IntProperty(name = "Index for my_list", default = 0)
    bpy.types.Scene.unreal_list = bpy.props.CollectionProperty(type=ListItem)
    bpy.types.Scene.unreal_settings = bpy.props.PointerProperty(type=UnrealLiveLinkData)


def unregister():
    bpy.utils.unregister_class(UnrealLiveLinkPanel)


if __name__ == "__main__":
    register()
