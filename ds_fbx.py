import bpy

from os import path, makedirs

def ds_fbx_export(self, context):

    export_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')
    export_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_export_folder + '//'
    if not path.exists(export_path):
        makedirs(export_path)
    export_file = export_path + export_name + '.fbx'

    bpy.ops.export_scene.fbx(filepath=export_file, check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", version='BIN7400', ui_tab='MAIN', use_selection=False, global_scale=1.0, apply_unit_scale=True, bake_space_transform=False, object_types={'ARMATURE', 'MESH'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=False, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, use_anim=True, use_anim_action_all=True, use_default_take=True, use_anim_optimize=True, anim_optimize_precision=6.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)
    
    return export_file

class ds_fbx_export_execute(bpy.types.Operator):

    bl_idname = "ds_fbx.export"
    bl_label = "Export FBX."

    def execute(self, context):

        export_file = ds_fbx_export(self, context)

        return {'FINISHED'}
    
def register():

    from bpy.utils import register_class

    register_class(ds_fbx_export_execute)

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_fbx_export_execute)
