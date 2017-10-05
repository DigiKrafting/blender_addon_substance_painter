import bpy
from subprocess import Popen

class ds_substance_open(bpy.types.Operator):

    bl_idname = "ds_substance.export"
    bl_label = "Open Substance Painter."

    def execute(self, context):

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_substance_exe])

        return {'FINISHED'}

def register():

    from bpy.utils import register_class

    register_class(ds_substance_open)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_substance_open)
