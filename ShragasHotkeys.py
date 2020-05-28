bl_info = {
    "name": "Shragas Hotkeys",
    "author": "Shraga the Mighty Sky Worm",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "3D View",
    "description": "My custom hotkeys.",
    "warning": "",
    "wiki_url": "http://ShragasServer.ddns.net",
    "category": "Hotkeys",
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import bpy
from bpy.types import Operator


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ToggleMeasurement(Operator):
    bl_idname = "hotkeys.edgelength"
    bl_label = "Toggle edge length display"
    bl_description = "Toggles the edge length display in edit mode."



    def execute(self, context):
        bpy.context.space_data.overlay.show_extra_edge_length = not bpy.context.space_data.overlay.show_extra_edge_length
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ToggleMeasurement)



def unregister():
    bpy.utils.unregister_class(ToggleMeasurement)



if __name__ == "__main__":
    register()

# bpy.context.space_data.overlay.show_extra_edge_length = False
