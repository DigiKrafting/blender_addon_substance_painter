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

bl_info = {
        "name": "Pipeline",
        "description": "3D Pipeline Tools",
        "author": "Digiography.Studio",
        "version": (0, 5, 0),
        "blender": (2, 79, 0),
        "location": "Properties > Scene, Info Toolbar, 3D View Toolbar",
        "wiki_url":    "https://github.com/Digiography/blender_addon_pipeline/wiki",
        "tracker_url": "https://github.com/Digiography/blender_addon_pipeline/issues",
        "category": "System",
}

import bpy

from os import path, makedirs

class ds_render_engine_cycles(bpy.types.Operator):

    bl_idname = "ds_render_engine.cycles"
    bl_label = "Set Render Engine to Cycles"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):

        bpy.context.scene.render.engine = 'CYCLES'

        return {'FINISHED'}

class ds_scene(bpy.types.Panel):

    bl_idname = "ds.scene"
    bl_label = "Pipeline"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
   
    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def draw(self, context):

        layout = self.layout

        if bpy.context.blend_data and bpy.context.blend_data.filepath:

                _export_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_export_folder + '//' 
                if not path.exists(_export_path):
                        makedirs(_export_path)

        if bpy.context.scene.render.engine != 'CYCLES':

                layout.operator('ds_render_engine.cycles')

        layout.label('Current Render Engine: '+context.scene.render.engine)

class ds_pipeline_addon_prefs(bpy.types.AddonPreferences):

    bl_idname = __package__

    option_iclone_exe = bpy.props.StringProperty(
            name="iClone Executable",
            subtype='FILE_PATH',
            default="C:\Program Files\Reallusion\iClone 7\Bin64\iClone.exe",
    )    
    option_iclone_cc_exe = bpy.props.StringProperty(
            name="iClone Character Creator Executable",
            subtype='FILE_PATH',
            default="C:\Program Files\Reallusion\Character Creator 2 for iClone\Bin64\CharacterCreator.exe",
    )    
    option_iclone_3dx_exe = bpy.props.StringProperty(
            name="iClone 3DX Executable",
            subtype='FILE_PATH',
            default="C:\Program Files (x86)\Reallusion\iClone 3DXchange 7\Bin\iClone3DXchange.exe",
    )    
    option_substance_exe = bpy.props.StringProperty(
            name="Substance Executable",
            subtype='FILE_PATH',
            default="C:\Program Files\Allegorithmic\Substance Painter\Substance Painter.exe",
    )    
    option_zbc_exe = bpy.props.StringProperty(
            name="ZBrushCore Executable",
            subtype='FILE_PATH',
            default="C:\Program Files\Pixologic\ZBrushCore\ZBrushCore.exe",
    )     
    option_export_folder = bpy.props.StringProperty(
            name="Export Folder Name",
            default="eXport",
    )     
    option_iclone_templates_path = bpy.props.StringProperty(
            name="iClone Templates Path",
            subtype='DIR_PATH',
            default="",
    )     

    def draw(self, context):

        layout = self.layout

        layout.label('Defaults',icon='PREFERENCES')
        
        layout.prop(self, 'option_export_folder')
        layout.label('Automatically created as a sub folder relative to the saved .blend file.',icon='INFO')
        layout.label('* Do NOT include any "\\".',icon='INFO')

        layout.label('Applications',icon='PREFERENCES')

        layout.prop(self, 'option_zbc_exe')
        layout.prop(self, 'option_substance_exe')

        layout.prop(self, 'option_iclone_exe')
        layout.prop(self, 'option_iclone_3dx_exe')
        layout.prop(self, 'option_iclone_cc_exe')

        layout.label('iClone',icon='PREFERENCES')

        layout.prop(self, 'option_iclone_templates_path')

def register():

    from bpy.utils import register_class

    register_class(ds_pipeline_addon_prefs)

    register_class(ds_render_engine_cycles)
    register_class(ds_scene)

    from . import space_info 

    register_class(space_info.INFO_HT_header)

    from . import ds_obj
    from . import ds_fbx

    ds_obj.register()
    ds_fbx.register()

    from . import ds_iclone
    from . import ds_zbc
    from . import ds_substance

    ds_iclone.register()
    ds_zbc.register()
    ds_substance.register()

def unregister():

    from bpy.utils import unregister_class

    unregister_class(ds_pipeline_addon_prefs)

    unregister_class(ds_render_engine_cycles)
    unregister_class(ds_scene)

    from . import ds_obj
    from . import ds_fbx

    ds_obj.unregister()
    ds_fbx.unregister()

    from . import ds_iclone
    from . import ds_zbc
    from . import ds_substance

    ds_iclone.unregister()
    ds_zbc.unregister()
    ds_substance.unregister()

    from . import space_info 

    unregister_class(space_info.INFO_HT_header)

if __name__ == "__main__":

	register()