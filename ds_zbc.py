import bpy

from subprocess import Popen

from .ds_obj import (ds_obj_filename, ds_obj_export,)

class ds_zbc_export(bpy.types.Operator):

    bl_idname = "ds_zbc.export"
    bl_label = "ZBrushCore (OBJ)"

    def execute(self, context):

        _export_file = ds_obj_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_zbc_exe,_export_file])

        return {'FINISHED'}

class ds_zbc_import(bpy.types.Operator):

    bl_idname = "ds_zbc.import"
    bl_label = "ZBrushCore (OBJ)"

    def execute(self, context):

        obj_selected = bpy.context.object
        obj_selected_mesh = obj_selected.data
        
        bpy.ops.object.transform_apply( location=True, rotation = True, scale = True )

        bpy.ops.import_scene.obj(filepath = ds_obj_filename(self, context), axis_forward='-Z', axis_up='Y',split_mode='OFF', use_image_search=False, use_groups_as_vgroups=False, use_smooth_groups=True)

        obj_imported =  bpy.context.selected_objects[0]
        obj_imported_mesh =  obj_imported.data
        
        bpy.ops.object.transform_apply( location=True, rotation = True, scale = True )

        _vertices=obj_selected_mesh.vertices
        for _vertice in _vertices:
            _vertice.co=obj_imported_mesh.vertices[_vertice.index].co
        
        bpy.ops.object.delete() 

        return {'FINISHED'}

def menu_func_export(self, context):
    self.layout.operator(ds_zbc_export.bl_idname)

def menu_func_import(self, context):
    self.layout.operator(ds_zbc_import.bl_idname)

def toolbar_btn_import(self, context):
    self.layout.operator('ds_zbc.import',text="ZBC",icon="IMPORT")

def toolbar_btn_export(self, context):
    self.layout.operator('ds_zbc.export',text="ZBC",icon="EXPORT")

def register():

    from bpy.utils import register_class

    register_class(ds_zbc_import)
    register_class(ds_zbc_export)

    bpy.types.INFO_MT_file_export.append(menu_func_export)
    bpy.types.INFO_MT_file_import.append(menu_func_import)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':
    
        bpy.types.INFO_HT_header.append(toolbar_btn_export)
        bpy.types.INFO_HT_header.append(toolbar_btn_import)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_zbc_import)
    unregister_class(ds_zbc_export)

    bpy.types.INFO_MT_file_import.remove(menu_func_import)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Buttons':

        bpy.types.INFO_HT_header.remove(toolbar_btn_import)
        bpy.types.INFO_HT_header.remove(toolbar_btn_export)