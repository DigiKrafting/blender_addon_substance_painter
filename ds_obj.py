import bpy

from os import path, makedirs

def ds_obj_filename(self, context):

    _object_name = bpy.context.scene.objects.active.name
    _export_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_export_folder + '//'
    _filename = _export_path + _object_name + '.obj'
  
    return _filename

def ds_obj_export(self, context):

    _export_file = ds_obj_filename(self, context)

    bpy.ops.export_scene.obj(filepath=_export_file, use_selection=True, axis_forward='-Z', axis_up='Y', global_scale=100.0, keep_vertex_order=True)

    return _export_file

class ds_obj_export_execute(bpy.types.Operator):

    bl_idname = "ds_obj.export"
    bl_label = "Export OBJ."

    def execute(self, context):

        _export_file = ds_obj_export(self, context)

        return {'FINISHED'}
    
def register():

    from bpy.utils import register_class

    register_class(ds_obj_export_execute)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_obj_export_execute)