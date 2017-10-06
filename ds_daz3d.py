import bpy
from subprocess import Popen

from .ds_fbx import (ds_fbx_export,)

class ds_daz3d_export(bpy.types.Operator):

    bl_idname = "ds_daz3d.export"
    bl_label = "Open Daz3D."

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_daz3d_exe])

        return {'FINISHED'}

def register():

    from bpy.utils import register_class

    register_class(ds_daz3d_export)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_daz3d_export)
