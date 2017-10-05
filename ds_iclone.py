import bpy
from subprocess import Popen
from os import system
from .ds_fbx import (ds_fbx_export,)

class ds_iclone_import_base(bpy.types.Operator):

    bl_idname = "ds_iclone.import_base"
    bl_label = "Import Base FBX."

    def execute(self, context):

        _export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
        _export_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_export_folder + '\\'
        system('copy "' + bpy.context.user_preferences.addons[__package__].preferences.option_iclone_templates_path + "Base.fbxkey" + '" "' + _export_path + _export_name + '.fbxkey"')

        bpy.ops.import_scene.fbx(filepath = bpy.context.user_preferences.addons[__package__].preferences.option_iclone_templates_path + "Base.fbx", axis_forward='-Z', axis_up='Y')

        return {'FINISHED'}

class ds_iclone_import_female(bpy.types.Operator):

    bl_idname = "ds_iclone.import_female"
    bl_label = "Import Base Female FBX."

    def execute(self, context):

        _export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
        _export_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_export_folder + '\\'
        system('copy "' + bpy.context.user_preferences.addons[__package__].preferences.option_iclone_templates_path + "Base Female.fbxkey" + '" "' + _export_path + _export_name + '.fbxkey"')
        
        bpy.ops.import_scene.fbx(filepath = bpy.context.user_preferences.addons[__package__].preferences.option_iclone_templates_path + "Base Female.fbx", axis_forward='-Z', axis_up='Y')

        return {'FINISHED'}

class ds_iclone_import_male(bpy.types.Operator):

    bl_idname = "ds_iclone.import_male"
    bl_label = "Import Base Male FBX."

    def execute(self, context):

        _export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
        _export_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_export_folder + '\\'
        system('copy "' + bpy.context.user_preferences.addons[__package__].preferences.option_iclone_templates_path + "Base Male.fbxkey" + '" "' + _export_path + _export_name + '.fbxkey"')

        bpy.ops.import_scene.fbx(filepath = bpy.context.user_preferences.addons[__package__].preferences.option_iclone_templates_path + "Base Male.fbx", axis_forward='-Z', axis_up='Y')

        return {'FINISHED'}

class ds_iclone_export_3dx(bpy.types.Operator):

    bl_idname = "ds_iclone.export_3dx"
    bl_label = "Export FBX and open in 3DXchange."

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_iclone_3dx_exe, export_file])

        return {'FINISHED'}

class ds_iclone_export_ic(bpy.types.Operator):

    bl_idname = "ds_iclone.export_ic"
    bl_label = "Export FBX and open iClone."

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_iclone_exe])

        return {'FINISHED'}

class ds_iclone_export_cc(bpy.types.Operator):

    bl_idname = "ds_iclone.export_cc"
    bl_label = "Export FBX and Open Character Creator."

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_iclone_cc_exe])

        return {'FINISHED'}

def register():

    from bpy.utils import register_class

    register_class(ds_iclone_import_base)
    register_class(ds_iclone_import_female)
    register_class(ds_iclone_import_male)
    register_class(ds_iclone_export_cc)
    register_class(ds_iclone_export_3dx)
    register_class(ds_iclone_export_ic)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_iclone_import_base)
    unregister_class(ds_iclone_import_female)
    unregister_class(ds_iclone_import_male)
    unregister_class(ds_iclone_export_cc)
    unregister_class(ds_iclone_export_3dx)
    unregister_class(ds_iclone_export_ic)
