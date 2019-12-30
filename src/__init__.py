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
if "bpy" in locals():
    from UE4LiveLink.LiveLinkWrapper.BlenderLiveLinkLib import BlenderLiveLinkLib
    from UE4LiveLink.LiveLinkWrapper.BlenderLiveLinkDevice import BlenderLiveLinkDevice
    from UE4LiveLink.LiveLinkWrapper.LiveLinkWrapper import LiveLinkWrapper
    from UE4LiveLink.Operators.ToggleServerOperator import ToggleServerOperator
    from UE4LiveLink.Operators.TrackObjectsOperator import TrackObjectsOperator
    from UE4LiveLink.Operators.UntrackObjectsOperator import UntrackObjectsOperator
    from UE4LiveLink.Panels.MyList import MyList
    from UE4LiveLink.Panels.UnrealLiveLinkPanel import UnrealLiveLinkPanel
    from UE4LiveLink.PropertyGroups.ListItemPropertyGroup import ListItemPropertyGroup
    from UE4LiveLink.PropertyGroups.UnrealLiveLinkData import UnrealLiveLinkData
else:
    import bpy
    from UE4LiveLink.LiveLinkWrapper.BlenderLiveLinkLib import BlenderLiveLinkLib
    from UE4LiveLink.LiveLinkWrapper.BlenderLiveLinkDevice import BlenderLiveLinkDevice
    from UE4LiveLink.LiveLinkWrapper.LiveLinkWrapper import LiveLinkWrapper
    from UE4LiveLink.Operators.ToggleServerOperator import UELL_OT_toggle_server
    from UE4LiveLink.Operators.TrackObjectsOperator import UELL_OT_track_objects
    from UE4LiveLink.Operators.UntrackObjectsOperator import UELL_OT_untrack_objects
    from UE4LiveLink.Panels.MyList import MY_UL_List
    from UE4LiveLink.Panels.UnrealLiveLinkPanel import SCENE_PT_UnrealLiveLinkPanel
    from UE4LiveLink.PropertyGroups.ListItemPropertyGroup import ListItem
    from UE4LiveLink.PropertyGroups.UnrealLiveLinkData import UnrealLiveLinkData


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
