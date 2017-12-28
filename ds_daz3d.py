import bpy
from subprocess import Popen

from .ds_fbx import (ds_fbx_export,)

class ds_daz3d_export(bpy.types.Operator):

    bl_idname = "ds_daz3d.export"
    bl_label = "Daz3D (FBX)"

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_daz3d_exe])

        return {'FINISHED'}

def menu_func_export(self, context):
    self.layout.operator(ds_daz3d_export.bl_idname)

def toolbar_btn_export(self, context):
    self.layout.operator('ds_daz3d.export',text="Daz3D",icon="LINK_BLEND")

def register():

    from bpy.utils import register_class

    register_class(ds_daz3d_export)

    bpy.types.INFO_MT_file_export.append(menu_func_export)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':

        bpy.types.INFO_HT_header.append(toolbar_btn_export)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_daz3d_export)

    bpy.types.INFO_MT_file_export.remove(menu_func_export)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':

        bpy.types.INFO_HT_header.remove(toolbar_btn_export)
