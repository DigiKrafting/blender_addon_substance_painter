import bpy
from subprocess import Popen

from .ds_fbx import (ds_fbx_export,)
from .ds_obj import (ds_obj_export,)

from . import ds_pipeline

class ds_substance_export_obj(bpy.types.Operator):

    bl_idname = "ds_sp.export_obj" 
    bl_label = "Substance Painter (OBJ)"

    def execute(self, context):

        _object_name = bpy.context.scene.objects.active.name
        _export_path = bpy.path.abspath('//')
        _export_project = _export_path + _object_name + '.spp'
        _textures_path = ds_pipeline.get_textures_path()
        _export_file = ds_obj_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path, _export_project])

        return {'FINISHED'}

class ds_substance_export_all(bpy.types.Operator):

    bl_idname = "ds_sp.export_all" 
    bl_label = "Substance Painter (FBX)"

    def execute(self, context):

        _export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
        _export_path = bpy.path.abspath('//')
        _export_project = _export_path + _export_name + '.spp'
        _textures_path = ds_pipeline.get_textures_path()
        _export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path, _export_project])

        return {'FINISHED'}

def menu_func_export_all(self, context):
    self.layout.operator(ds_substance_export_all.bl_idname)
def menu_func_export_obj(self, context):
    self.layout.operator(ds_substance_export_obj.bl_idname)

def toolbar_btn_export_all(self, context):
    self.layout.operator('ds_sp.export_all',text="SP:All",icon="EXPORT")
def toolbar_btn_export_obj(self, context):
    self.layout.operator('ds_sp.export_obj',text="SP:OBJ",icon="EXPORT")

def register():

    from bpy.utils import register_class

    register_class(ds_substance_export_all)
    register_class(ds_substance_export_obj)

    bpy.types.INFO_MT_file_export.append(menu_func_export_all)
    bpy.types.INFO_MT_file_export.append(menu_func_export_obj)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':

        bpy.types.INFO_HT_header.append(toolbar_btn_export_all)
        bpy.types.INFO_HT_header.append(toolbar_btn_export_obj)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_substance_export_all)
    unregister_class(ds_substance_export_obj)

    bpy.types.INFO_MT_file_export.remove(menu_func_export_all)
    bpy.types.INFO_MT_file_export.remove(menu_func_export_obj)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':

        bpy.types.INFO_HT_header.remove(toolbar_btn_export_all)
        bpy.types.INFO_HT_header.remove(toolbar_btn_export_obj)