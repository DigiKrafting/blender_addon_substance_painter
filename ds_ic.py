import bpy
from subprocess import Popen
from .ds_fbx import (ds_fbx_export,)
from os import system, path, makedirs
from . import ds_pipeline

class ds_ic_import_base(bpy.types.Operator):

    bl_idname = "ds_ic.import_base"
    bl_label = "iClone Base Template (FBX)"

    def execute(self, context):

        _export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
        _export_path = ds_pipeline.get_export_path()

        system('copy "' + bpy.context.user_preferences.addons[__package__].preferences.option_ic_templates_path + "Base.fbxkey" + '" "' + _export_path + _export_name + '.fbxkey"')

        bpy.ops.import_scene.fbx(filepath = bpy.context.user_preferences.addons[__package__].preferences.option_ic_templates_path + "Base.fbx", axis_forward='-Z', axis_up='Y', global_scale=1.0)
        bpy.ops.object.transform_apply( location=True, rotation = True, scale = True )

        return {'FINISHED'}

class ds_ic_import_female(bpy.types.Operator):

    bl_idname = "ds_ic.import_female"
    bl_label = "iClone Female Template (FBX)"

    def execute(self, context):

        _export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
        _export_path = ds_pipeline.get_export_path()

        system('copy "' + bpy.context.user_preferences.addons[__package__].preferences.option_ic_templates_path + "Base Female.fbxkey" + '" "' + _export_path + _export_name + '.fbxkey"')
        
        bpy.ops.import_scene.fbx(filepath = bpy.context.user_preferences.addons[__package__].preferences.option_ic_templates_path + "Base Female.fbx", axis_forward='-Z', axis_up='Y', global_scale=1.0)
        bpy.ops.object.transform_apply( location=True, rotation = True, scale = True )

        return {'FINISHED'}

class ds_ic_import_male(bpy.types.Operator):

    bl_idname = "ds_ic.import_male"
    bl_label = "iClone Male Template (FBX)"

    def execute(self, context):

        _export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
        _export_path = ds_pipeline.get_export_path()

        system('copy "' + bpy.context.user_preferences.addons[__package__].preferences.option_ic_templates_path + "Base Male.fbxkey" + '" "' + _export_path + _export_name + '.fbxkey"')

        bpy.ops.import_scene.fbx(filepath = bpy.context.user_preferences.addons[__package__].preferences.option_ic_templates_path + "Base Male.fbx", axis_forward='-Z', axis_up='Y', global_scale=1.0)
        bpy.ops.object.transform_apply( location=True, rotation = True, scale = True )

        return {'FINISHED'}

class ds_ic_export_3dx(bpy.types.Operator):

    bl_idname = "ds_ic.export_3dx"
    bl_label = "3DXchange (FBX)"

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_ic_3dx_exe, export_file])

        return {'FINISHED'}

class ds_ic_export_ic(bpy.types.Operator):

    bl_idname = "ds_ic.export_ic"
    bl_label = "Open iClone"

    def execute(self, context):

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_ic_exe])

        return {'FINISHED'}

class ds_ic_export_cc(bpy.types.Operator):

    bl_idname = "ds_ic.export_cc"
    bl_label = "Character Creator (FBX)"

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_ic_cc_exe])

        return {'FINISHED'}

def menu_func_import_base(self, context):
    self.layout.operator(ds_ic_import_base.bl_idname)
def menu_func_import_female(self, context):
    self.layout.operator(ds_ic_import_female.bl_idname)
def menu_func_import_male(self, context):
    self.layout.operator(ds_ic_import_male.bl_idname)
def menu_func_export_cc(self, context):
    self.layout.operator(ds_ic_export_cc.bl_idname)
def menu_func_export_3dx(self, context):
    self.layout.operator(ds_ic_export_3dx.bl_idname)

def toolbar_btn_base(self, context):
    self.layout.operator('ds_ic.import_base',text="Base",icon="IMPORT")
def toolbar_btn_female(self, context):
    self.layout.operator('ds_ic.import_female',text="Female",icon="IMPORT")
def toolbar_btn_male(self, context):
    self.layout.operator('ds_ic.import_male',text="Male",icon="IMPORT")
def toolbar_btn_cc(self, context):
    self.layout.operator('ds_ic.export_cc',text="CC",icon="LINK_BLEND")
def toolbar_btn_3dx(self, context):
    self.layout.operator('ds_ic.export_3dx',text="3DX",icon="EXPORT")
def toolbar_btn_ic(self, context):
    self.layout.operator('ds_ic.export_ic',text="IC",icon="LINK_BLEND")

def register():

    from bpy.utils import register_class

    register_class(ds_ic_import_base)
    register_class(ds_ic_import_female)
    register_class(ds_ic_import_male)
    register_class(ds_ic_export_cc)
    register_class(ds_ic_export_3dx)
    register_class(ds_ic_export_ic)

    bpy.types.INFO_MT_file_import.append(menu_func_import_base)
    bpy.types.INFO_MT_file_import.append(menu_func_import_female)
    bpy.types.INFO_MT_file_import.append(menu_func_import_male)
    bpy.types.INFO_MT_file_export.append(menu_func_export_cc)
    bpy.types.INFO_MT_file_export.append(menu_func_export_3dx)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':

        bpy.types.INFO_HT_header.append(toolbar_btn_base)
        bpy.types.INFO_HT_header.append(toolbar_btn_female)
        bpy.types.INFO_HT_header.append(toolbar_btn_male)
        bpy.types.INFO_HT_header.append(toolbar_btn_cc)
        bpy.types.INFO_HT_header.append(toolbar_btn_3dx)
        bpy.types.INFO_HT_header.append(toolbar_btn_ic)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_ic_import_base)
    unregister_class(ds_ic_import_female)
    unregister_class(ds_ic_import_male)
    unregister_class(ds_ic_export_cc)
    unregister_class(ds_ic_export_3dx)
    unregister_class(ds_ic_export_ic)

    bpy.types.INFO_MT_file_import.remove(menu_func_import_base)
    bpy.types.INFO_MT_file_import.remove(menu_func_import_female)
    bpy.types.INFO_MT_file_import.remove(menu_func_import_male)
    bpy.types.INFO_MT_file_export.remove(menu_func_export_cc)
    bpy.types.INFO_MT_file_export.remove(menu_func_export_3dx)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':

        bpy.types.INFO_HT_header.remove(toolbar_btn_base)
        bpy.types.INFO_HT_header.remove(toolbar_btn_female)
        bpy.types.INFO_HT_header.remove(toolbar_btn_male)
        bpy.types.INFO_HT_header.remove(toolbar_btn_cc)
        bpy.types.INFO_HT_header.remove(toolbar_btn_3dx)
        bpy.types.INFO_HT_header.remove(toolbar_btn_ic)    