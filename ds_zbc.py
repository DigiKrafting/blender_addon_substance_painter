import bpy

from subprocess import Popen

from .ds_obj import (ds_obj_filename, ds_obj_export,)

class ds_zbc_export(bpy.types.Operator):

    bl_idname = "ds_zbc.export"
    bl_label = "Export Selected Object to ZBC."

    def execute(self, context):

        export_file = ds_obj_export(self, context)

        Popen([bpy.context.user_preferences.addons[__package__].preferences.option_zbc_exe,export_file])

        return {'FINISHED'}

class ds_zbc_import(bpy.types.Operator):

    bl_idname = "ds_zbc.import"
    bl_label = "Import ZBC Object."

    def execute(self, context):

        obj_selected = bpy.context.object
        obj_selected_mesh = obj_selected.data
        
        bpy.ops.import_scene.obj(filepath = ds_obj_filename(self, context), axis_forward='-Z', axis_up='Y',split_mode='OFF', use_image_search=False)

        obj_imported =  bpy.context.selected_objects[0]
        obj_imported_mesh =  obj_imported.data
        
        bpy.ops.object.transform_apply( rotation = True, scale = True )

        _vertices=obj_selected_mesh.vertices
        for _vertice in _vertices:
            _vertice.co=obj_imported_mesh.vertices[_vertice.index].co

        bpy.ops.object.delete() 

        obj_selected.scale = (1.0, 1.0, 1.0)
        obj_selected.select = True
        bpy.ops.object.transform_apply( rotation = True, scale = True )

        return {'FINISHED'}

def register():

    from bpy.utils import register_class

    register_class(ds_zbc_import)
    register_class(ds_zbc_export)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_zbc_import)
    unregister_class(ds_zbc_export)
