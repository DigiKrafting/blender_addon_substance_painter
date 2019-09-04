# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

from subprocess import Popen
from os import system, path, makedirs, sep

def dks_sp_get_export_path():

    _export_path = bpy.path.abspath('//') + bpy.context.preferences.addons[__package__].preferences.option_export_folder + sep

    if not path.exists(_export_path):
        makedirs(_export_path)

    return _export_path

def dks_sp_get_textures_path():

    _textures_path = bpy.path.abspath('//') + bpy.context.preferences.addons[__package__].preferences.option_textures_folder + sep

    if not path.exists(_textures_path):
        makedirs(_textures_path)

    return _textures_path

def dks_sp_get_object_name():

    return bpy.context.active_object.name

def dks_sp_get_file_name():

    return bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend','')

def dks_sp_get_texture_file(texture_path,mesh_name,mat_name,texture_name,texture_ext):

    if path.exists(texture_path+mesh_name+'_'+mat_name+'_'+texture_name+'.'+texture_ext):
        if bpy.context.preferences.addons[__package__].preferences.option_relative:
            texture_path=bpy.path.relpath(texture_path)+sep
        return texture_path+mesh_name+'_'+mat_name+'_'+texture_name+'.'+texture_ext
    elif path.exists(texture_path+mat_name+'_'+texture_name+'.'+texture_ext):
        if bpy.context.preferences.addons[__package__].preferences.option_relative:
            texture_path=bpy.path.relpath(texture_path)+sep
        return texture_path+mat_name+'_'+texture_name+'.'+texture_ext
    else:
        _blend=dks_sp_get_file_name()
        if path.exists(texture_path+_blend+'_'+mesh_name+'_'+texture_name+'.'+texture_ext):
            if bpy.context.preferences.addons[__package__].preferences.option_relative:
                texture_path=bpy.path.relpath(texture_path)+sep
            return texture_path+_blend+'_'+mesh_name+'_'+texture_name+'.'+texture_ext
        elif path.exists(texture_path+_blend+'_'+mat_name+'_'+texture_name+'.'+texture_ext):
            if bpy.context.preferences.addons[__package__].preferences.option_relative:
                texture_path=bpy.path.relpath(texture_path)+sep
            return texture_path+_blend+'_'+mat_name+'_'+texture_name+'.'+texture_ext
        else:
            return ""

class dks_sp_pbr_nodes(bpy.types.Operator):

    bl_idname = "dks_sp.pbr_nodes"
    bl_label = "Import Textures"
    bl_context = "material"
    bl_description = "Import from Substance Painter"

    import_setting : bpy.props.StringProperty(
        name="import_setting",
        default = 'scene'
    )

    def execute(self, context):

        if self.import_setting == 'scene':

            _objects = bpy.context.scene.objects

        elif bpy.context.active_object:

            _objects = {bpy.context.active_object}

        _textures_path = dks_sp_get_textures_path()

        _texture_ext=bpy.context.preferences.addons[__package__].preferences.option_import_ext

        for _obj in _objects:

            if _obj.type=='MESH':

                _obj_name = _obj.name

                _materials = _obj.data.materials

                for _material in _materials:

                    _material_name = _material.name

                    _file_Base_Color = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Base_Color',_texture_ext)

                    if _file_Base_Color=="":
                        _file_Base_Color = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'BaseColor',_texture_ext)

                    _file_Diffuse = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Diffuse',_texture_ext)
                    _file_Ambient_occlusion = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Ambient_occlusion',_texture_ext)
                    _file_Metallic = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Metallic',_texture_ext)
                    _file_Specular = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Specular',_texture_ext)
                    _file_Glossiness = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Glossiness',_texture_ext)
                    _file_Roughness = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Roughness',_texture_ext)
                    _file_ORM = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'OcclusionRoughnessMetallic',_texture_ext)
                    _file_Opacity = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Opacity',_texture_ext)

                    _file_Height = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Height',_texture_ext)
                    _file_Normal = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Normal_OpenGL',_texture_ext)

                    if _file_Normal=="":
                        _file_Normal = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Normal',_texture_ext)

                    _file_Emissive = dks_sp_get_texture_file(_textures_path,_obj_name,_material_name,'Emissive',_texture_ext)

                    if _file_Base_Color or _file_Diffuse:

                        if _material:

                            _material.use_nodes = True

                        # Clear Nodes

                        if _material and _material.node_tree:

                            _nodes = _material.node_tree.nodes

                            for node in _nodes:
                                _nodes.remove(node)

                        _material_links = _material.node_tree.links

                        _nodes = _material.node_tree.nodes

                        # Output Material

                        _material_output = _nodes.new('ShaderNodeOutputMaterial')

                        if not _file_Emissive:
                            _material_output.location = 800,0
                        else:
                            _material_output.location = 1600,0

                        _material_output.name='dks_pbr_output'

                        if _file_Emissive:

                            # Add Shader

                            _node_add_shader=_nodes.new('ShaderNodeAddShader')
                            _node_add_shader.location = 1400,0
                            _node_add_shader.name = 'dks_pbr_add_shader'
                            _material_links.new(_node_add_shader.outputs['Shader'], _material_output.inputs['Surface'])

                            # Shader Emission

                            _node_emission=_nodes.new('ShaderNodeEmission')
                            _node_emission.location = 1200,-100
                            _node_emission.name = 'dks_pbr_emission'
                            _material_links.new(_node_emission.outputs['Emission'], _node_add_shader.inputs[1])

                            # Emissive

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = 800,-100
                            node.name='dks_pbr_texture_emissive'
                            _material_links.new(node.outputs['Color'], _node_emission.inputs['Color'])
                            node.image = bpy.data.images.load(_file_Emissive)

                        # Shader

                        node_shader = _nodes.new('ShaderNodeBsdfPrincipled')
                        node_shader.location = 400,0
                        node_shader.name='dks_pbr_shader'

                        if not _file_Emissive:
                            _material_links.new(node_shader.outputs['BSDF'], _material_output.inputs['Surface'])
                        else:
                            _material_links.new(node_shader.outputs['BSDF'], _node_add_shader.inputs[0])

                        # UE4 - Occlusion, Roughness, Metallic

                        if _file_ORM:

                            # Mix RGB

                            node_mix=_nodes.new('ShaderNodeMixRGB')
                            node_mix.location = 200,100
                            node_mix.blend_type = 'MULTIPLY'
                            node_mix.name='dks_pbr_mix_rgb'
                            _material_links.new(node_mix.outputs['Color'], node_shader.inputs['Base Color'])

                            # Base Color

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = -200,250
                            node.name='dks_pbr_texture_base_color'
                            _material_links.new(node.outputs['Color'], node_mix.inputs['Color1'])

                            node.image = bpy.data.images.load(_file_Base_Color)
                            node.image.colorspace_settings.name = 'sRGB'

                            node_orm=_nodes.new('ShaderNodeTexImage')
                            node_orm.location = -500,-200
                            node_orm.name='dks_pbr_texture_orm'

                            node_orm.image = bpy.data.images.load(_file_ORM)
                            node_orm.image.colorspace_settings.name = 'Non-Color'

                            node_sep_rgb=_nodes.new('ShaderNodeSeparateRGB')
                            node_sep_rgb.location = -200,-200
                            node_sep_rgb.name='dks_pbr_texture_sep_rgb'

                            _material_links.new(node_orm.outputs['Color'], node_sep_rgb.inputs['Image'])

                            _material_links.new(node_sep_rgb.outputs['R'], node_mix.inputs['Color2'])
                            _material_links.new(node_sep_rgb.outputs['G'], node_shader.inputs['Roughness'])
                            _material_links.new(node_sep_rgb.outputs['B'], node_shader.inputs['Metallic'])

                        elif _file_Ambient_occlusion:

                            # Mix RGB

                            node_mix=_nodes.new('ShaderNodeMixRGB')
                            node_mix.location = 200,100
                            node_mix.blend_type = 'MULTIPLY'
                            node_mix.name='dks_pbr_mix_rgb'
                            _material_links.new(node_mix.outputs['Color'], node_shader.inputs['Base Color'])

                            # Base Color

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = -140,261
                            node.name='dks_pbr_texture_base_color'
                            _material_links.new(node.outputs['Color'], node_mix.inputs['Color1'])

                            if _file_Base_Color:
                                node.image = bpy.data.images.load(_file_Base_Color)
                            elif _file_Diffuse:
                                node.image = bpy.data.images.load(_file_Diffuse)

                            node.image.colorspace_settings.name = 'sRGB'

                            # Ambient Occlusion

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = -140,0
                            node.name='dks_pbr_texture_ao'
                            _material_links.new(node.outputs['Color'], node_mix.inputs['Color2'])
                            node.image = bpy.data.images.load(_file_Ambient_occlusion)
                            node.image.colorspace_settings.name = 'Non-Color'

                        else:

                            # Base Color

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = 0,250
                            node.name='dks_pbr_texture_base_color'
                            _material_links.new(node.outputs['Color'], node_shader.inputs['Base Color'])

                            if _file_Base_Color:
                                node.image = bpy.data.images.load(_file_Base_Color)
                            elif _file_Diffuse:
                                node.image = bpy.data.images.load(_file_Diffuse)

                            node.image.colorspace_settings.name = 'sRGB'

                        # Metallic

                        if _file_Metallic:

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = 0,-250
                            node.name='dks_pbr_texture_metallic'
                            _material_links.new(node.outputs['Color'], node_shader.inputs['Metallic'])
                            node.image = bpy.data.images.load(_file_Metallic)
                            node.image.colorspace_settings.name = 'Non-Color'

                        # Specular

                        if _file_Specular:

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = -280,-180
                            node.name='dks_pbr_texture_Specular'
                            _material_links.new(node.outputs['Color'], node_shader.inputs['Specular'])
                            node.image = bpy.data.images.load(_file_Specular)

                        if _file_Glossiness:

                            # Roughness Invert

                            node_invert=_nodes.new('ShaderNodeInvert')
                            node_invert.location = 100,-520
                            node_invert.name='dks_pbr_invert'
                            _material_links.new(node_invert.outputs['Color'], node_shader.inputs['Roughness'])

                            # Roughness

                            if _file_Roughness!="":

                                node=_nodes.new('ShaderNodeTexImage')
                                node.location = -280,-520
                                node.name='dks_pbr_texture_roughness'
                                _material_links.new(node.outputs['Color'], node_invert.inputs['Color'])
                                node.image = bpy.data.images.load(_file_Glossiness)

                        else:

                            # Roughness

                            if _file_Roughness:

                                node=_nodes.new('ShaderNodeTexImage')
                                node.location = 0,-500
                                node.name='dks_pbr_texture_roughness'
                                _material_links.new(node.outputs['Color'], node_shader.inputs['Roughness'])
                                node.image = bpy.data.images.load(_file_Roughness)
                                node.image.colorspace_settings.name = 'Non-Color'

                        # Opacity

                        if _file_Opacity:

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = 0,-600
                            node.name='dks_pbr_texture_opacity'
                            _material_links.new(node.outputs['Color'], node_shader.inputs['Alpha'])
                            node.image = bpy.data.images.load(_file_Opacity)
                            node.image.colorspace_settings.name = 'Non-Color'

                            _material.blend_method = 'CLIP'

                        # Height

                        if bpy.context.preferences.addons[__package__].preferences.option_use_height_maps and _file_Height:

                            frame_1= _nodes.new('NodeFrame')
                            frame_1.location = -390, -837
                            frame_1.width = 802
                            frame_1.height = 628
                            frame_1.label = 'Normal and Height'

                            node_Bump=_nodes.new('ShaderNodeBump')
                            node_Bump.location = 250,-870
                            node_Bump.name='dks_pbr_Bump'
                            _material_links.new(node_Bump.outputs['Normal'], node_shader.inputs['Normal'])

                            node_map=_nodes.new('ShaderNodeNormalMap')
                            node_map.location = -20,-1150
                            node_map.name='dks_pbr_normal_map'
                            _material_links.new(node_map.outputs['Normal'], node_Bump.inputs['Normal'])

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = -360,-1180
                            node.name='dks_pbr_texture_normal'
                            _material_links.new(node.outputs['Color'], node_map.inputs['Color'])
                            node.image = bpy.data.images.load(_file_Normal)
                            node.image.colorspace_settings.name = 'Non-Color'

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = -360,-870
                            node.name='dks_pbr_texture_Height'
                            _material_links.new(node.outputs['Color'], node_Bump.inputs['Height'])
                            node.image = bpy.data.images.load(_file_Height)
                            node.image.colorspace_settings.name = 'Non-Color'

                        else:

                            # Normal

                            node_map=_nodes.new('ShaderNodeNormalMap')
                            node_map.location = 200,-700
                            node_map.name='dks_pbr_normal_map'
                            _material_links.new(node_map.outputs['Normal'], node_shader.inputs['Normal'])

                            node=_nodes.new('ShaderNodeTexImage')
                            node.location = -100,-750
                            node.name='dks_pbr_texture_normal'
                            _material_links.new(node.outputs['Color'], node_map.inputs['Color'])
                            node.image = bpy.data.images.load(_file_Normal)
                            node.image.colorspace_settings.name = 'Non-Color'

        return {'FINISHED'}

def dks_sp_fbx_export_sel(self, context):

    _export_name = dks_sp_get_object_name()
    _export_path = dks_sp_get_export_path()
    _export_file = _export_path + _export_name + '.fbx'

    if bpy.context.preferences.addons[__package__].preferences.option_save_before_export:
        bpy.ops.wm.save_mainfile()

    bpy.ops.export_scene.fbx(filepath=_export_file, use_selection=True, check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", global_scale=1.0, apply_unit_scale=True, bake_space_transform=False, object_types={'ARMATURE', 'MESH'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=False, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)

    return _export_file

class dks_sp_fbx_export_sel_execute(bpy.types.Operator):

    bl_idname = "dks_sp.fbx_export_sel"
    bl_label = "Export FBX."

    def execute(self, context):

        _export_file = dks_sp_fbx_export_sel(self, context)

        return {'FINISHED'}

def dks_sp_fbx_export_scene(self, context):

    _export_name = dks_sp_get_file_name()
    _export_path = dks_sp_get_export_path()
    _export_file = _export_path + _export_name + '.fbx'

    if bpy.context.preferences.addons[__package__].preferences.option_save_before_export:
        bpy.ops.wm.save_mainfile()

    bpy.ops.export_scene.fbx(filepath=_export_file, use_selection=False, check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", global_scale=1.0, apply_unit_scale=True, bake_space_transform=False, object_types={'ARMATURE', 'MESH'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=False, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)

    return _export_file

class dks_sp_fbx_export_scene_execute(bpy.types.Operator):

    bl_idname = "dks_sp.fbx_export_scene"
    bl_label = "Export FBX."

    def execute(self, context):

        _export_file = dks_sp_fbx_export_scene(self, context)

        return {'FINISHED'}

def dks_sp_obj_export_sel(self, context):

    _export_name = dks_sp_get_object_name()
    _export_path = dks_sp_get_export_path()
    _export_file = _export_path + _export_name + '.obj'

    if bpy.context.preferences.addons[__package__].preferences.option_save_before_export:
        bpy.ops.wm.save_mainfile()

    bpy.ops.export_scene.obj(filepath=_export_file, check_existing=False, use_selection=True, axis_forward='-Z', axis_up='Y', global_scale=1.0, keep_vertex_order=True)

    return _export_file

class dks_sp_obj_export_sel_execute(bpy.types.Operator):

    bl_idname = "dks_sp.obj_export_sel"
    bl_label = "Export OBJ."

    def execute(self, context):

        _export_file = dks_sp_obj_export_sel(self, context)

        return {'FINISHED'}

def dks_sp_obj_export_scene(self, context):

    _export_name = dks_sp_get_file_name()
    _export_path = dks_sp_get_export_path()
    _export_file = _export_path + _export_name + '.obj'

    if not bpy.context.preferences.addons[__package__].preferences.option_save_before_export:
        bpy.ops.wm.save_mainfile()

    bpy.ops.export_scene.obj(filepath=_export_file, check_existing=False, use_selection=False, axis_forward='-Z', axis_up='Y', global_scale=1.0, keep_vertex_order=True)

    return _export_file

class dks_sp_obj_export_scene_execute(bpy.types.Operator):

    bl_idname = "dks_sp.obj_export_scene"
    bl_label = "Export OBJ."

    def execute(self, context):

        _export_file = dks_sp_obj_export_scene(self, context)

        return {'FINISHED'}

class dks_sp_export_sel(bpy.types.Operator):

    bl_idname = "dks_sp.export_sel"
    bl_label = "Substance Painter (Selected)"
    bl_description = "Export to Substance Painter (Selected)"

    def execute(self, context):

        _object_name = dks_sp_get_object_name()
        _export_path = bpy.path.abspath('//')
        _export_project = _export_path + _object_name + '.spp'
        _textures_path = dks_sp_get_textures_path()

        if bpy.context.preferences.addons[__package__].preferences.option_export_type=='obj':
            _export_file = dks_sp_obj_export_sel(self, context)
        elif bpy.context.preferences.addons[__package__].preferences.option_export_type=='fbx':
            _export_file = dks_sp_fbx_export_sel(self, context)

        if bpy.context.preferences.addons[__package__].preferences.option_no_new:

            if not path.exists(_export_project):
                Popen([bpy.context.preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path])
            else:
                Popen([bpy.context.preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path, _export_project])

        else:

            Popen([bpy.context.preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path, _export_project])

        return {'FINISHED'}

class dks_sp_export_scene(bpy.types.Operator):

    bl_idname = "dks_sp.export_scene"
    bl_label = "Substance Painter (Scene)"
    bl_description = "Export to Substance Painter (Scene)"

    def execute(self, context):

        _export_name = dks_sp_get_file_name()
        _export_path = bpy.path.abspath('//')
        _export_project = _export_path + _export_name + '.spp'
        _textures_path = dks_sp_get_textures_path()

        if bpy.context.preferences.addons[__package__].preferences.option_export_type=='obj':
            _export_file = dks_sp_obj_export_scene(self, context)
        elif bpy.context.preferences.addons[__package__].preferences.option_export_type=='fbx':
            _export_file = dks_sp_fbx_export_scene(self, context)

        if bpy.context.preferences.addons[__package__].preferences.option_no_new:

            if not path.exists(_export_project):
                Popen([bpy.context.preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path])
            else:
                Popen([bpy.context.preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path, _export_project])

        else:

            Popen([bpy.context.preferences.addons[__package__].preferences.option_sp_exe, "--disable-version-checking", "--mesh", _export_file, "--export-path", _textures_path, _export_project])

        return {'FINISHED'}



classes = (
    dks_sp_fbx_export_sel_execute,
    dks_sp_fbx_export_scene_execute,
    dks_sp_obj_export_sel_execute,
    dks_sp_obj_export_scene_execute,
    dks_sp_export_scene,
    dks_sp_export_sel,
    dks_sp_pbr_nodes,
)

def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
