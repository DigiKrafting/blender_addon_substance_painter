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
        "version": (0, 9, 5),
        "blender": (2, 79, 0),
        "location": "Info Toolbar, File -> Import, File -> Export",
        "wiki_url":    "https://github.com/Digiography/blender_addon_pipeline/wiki",
        "tracker_url": "https://github.com/Digiography/blender_addon_pipeline/issues",
        "category": "System",
}

import bpy

from bpy.types import Header, Menu
from os import path, makedirs

class ds_pipeline_addon_prefs(bpy.types.AddonPreferences):

        bl_idname = __package__

        option_ic_exe = bpy.props.StringProperty(
                name="iClone Executable",
                subtype='FILE_PATH',
                default="C:\Program Files\Reallusion\iClone 7\Bin64\iClone.exe",
        )    
        option_ic_cc_exe = bpy.props.StringProperty(
                name="iClone Character Creator Executable",
                subtype='FILE_PATH',
                default="C:\Program Files\Reallusion\Character Creator 2 for iClone\Bin64\CharacterCreator.exe",
        )    
        option_ic_3dx_exe = bpy.props.StringProperty(
                name="iClone 3DX Executable",
                subtype='FILE_PATH',
                default="C:\Program Files (x86)\Reallusion\iClone 3DXchange 7\Bin\iClone3DXchange.exe",
        )    
        option_sp_exe = bpy.props.StringProperty(
                name="Substance Executable",
                subtype='FILE_PATH',
                default="C:\Program Files\Allegorithmic\Substance Painter\Substance Painter.exe",
        )    
        option_zbc_exe = bpy.props.StringProperty(
                name="ZBrushCore Executable",
                subtype='FILE_PATH',
                default="C:\Program Files\Pixologic\ZBrushCore\ZBrushCore.exe",
        )     
        option_daz3d_exe = bpy.props.StringProperty(
                name="Daz3D Executable",
                subtype='FILE_PATH',
                default="C:\Program Files\DAZ 3D\DAZStudio4\DAZStudio.exe",
        )       
        option_export_folder = bpy.props.StringProperty(
                name="Export Folder Name",
                default="eXport",
        )     
        option_textures_folder = bpy.props.StringProperty(
                name="Textures Folder Name",
                default="Textures",
        )     
        option_ic_templates_path = bpy.props.StringProperty(
                name="iClone Templates Path",
                subtype='DIR_PATH',
                default="",
        )     
        option_show_zbc = bpy.props.BoolProperty(
                name="Show ZBrushCore Buttons",
                default=True,
        )
        option_show_iclone_toggle = bpy.props.BoolProperty(
                name="iClone Toggle",
                default=True,
        )
        option_show_iclone_toggle_state = bpy.props.BoolProperty(
                name="iClone Toggle Button State",
                default=False,
        )                          
        option_show_ic = bpy.props.BoolProperty(
                name="Show iClone Buttons",
                default=True,
        )     
        option_show_sp = bpy.props.BoolProperty(
                name="Show Substance Painter Button",
                default=True,
        )     
        option_show_daz3d = bpy.props.BoolProperty(
                name="Show Daz3D Button",
                default=True,
        )     
        option_show_file_icons = bpy.props.BoolProperty(
                name="File Icons Only",
                default=True,
        )     
        option_save_before_export = bpy.props.BoolProperty(
                name="Save Before Export",
                default=True,
        )     
        options_display_types = [('Buttons', "Buttons", "Buttons"),('Menu', "Menu", "Menu"),('Hide', "Hide", "Hide"),]        
        option_display_type = bpy.props.EnumProperty(
                items=options_display_types,
                name="Display Type",
                default='Buttons',
        )
        def draw(self, context):

                layout = self.layout

                box=layout.box()
                box.prop(self, 'option_display_type')
                box=layout.box()
                box.label("Folders",icon='PREFERENCES')
                box.prop(self, 'option_export_folder')
                box.prop(self, 'option_textures_folder')
                box.label('* Do NOT include any "\\".',icon='INFO')
                box.label('Automatically created as a sub folder relative to the saved .blend file.',icon='INFO')
                box.prop(self, 'option_save_before_export')
                box=layout.box()
                box.label('Applications',icon='PREFERENCES')
                box.prop(self, 'option_show_zbc')
                box.prop(self, 'option_zbc_exe')
                box.prop(self, 'option_show_sp')
                box.prop(self, 'option_sp_exe')
                box.prop(self, 'option_show_ic')
                box.prop(self, 'option_ic_exe')
                box.prop(self, 'option_ic_3dx_exe')
                box.prop(self, 'option_ic_cc_exe')
                box.prop(self, 'option_ic_templates_path')
                box.prop(self, 'option_show_daz3d')
                box.prop(self, 'option_daz3d_exe')

class ds_pipeline_prefs_open(bpy.types.Operator):

    bl_idname = "ds_pipeline.prefs_open"
    bl_label = "Open Preferences"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):
        
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')

        return {'FINISHED'}

class Pipeline_Menu(bpy.types.Menu):
    bl_label = " Pipeline"
    bl_idname = "OBJECT_MT_Pipeline_Menu"

    def draw(self, context):
            
        layout = self.layout

        if bpy.context.user_preferences.addons[__package__].preferences.option_show_zbc:

            self.layout.operator('ds_zbc.export',icon="EXPORT")
            self.layout.operator('ds_zbc.import',icon="IMPORT")
            self.layout.separator()

        if bpy.context.user_preferences.addons[__package__].preferences.option_show_sp:

            self.layout.operator('ds_sp.export_all',icon="LINK_BLEND")
            self.layout.operator('ds_sp.export_obj',icon="LINK_BLEND")
            self.layout.separator()

        if bpy.context.user_preferences.addons[__package__].preferences.option_show_ic:

            layout.operator('ds_ic.import_base',icon="IMPORT")
            layout.operator('ds_ic.import_female',icon="IMPORT")
            layout.operator('ds_ic.import_male',icon="IMPORT")
            self.layout.separator()

            layout.operator('ds_ic.export_cc',icon="LINK_BLEND")
            layout.operator('ds_ic.export_3dx',icon="EXPORT")
            layout.operator('ds_ic.export_ic',icon="LINK_BLEND")
            self.layout.separator()

        if bpy.context.user_preferences.addons[__package__].preferences.option_show_daz3d:

            layout.operator('ds_daz3d.export',text="Daz3D",icon="LINK_BLEND")

def Draw_Pipeline_Menu(self, context):

        layout = self.layout
        layout.menu(Pipeline_Menu.bl_idname,icon="EXPORT")

class ds_pipeline_iclone_toggle(bpy.types.Operator):
    bl_idname = "ds_pipeline.iclone_toggle"
    bl_label = "iClone"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):

        if not bpy.context.user_preferences.addons[__package__].preferences.option_show_iclone_toggle_state:
                bpy.context.user_preferences.addons[__package__].preferences.option_show_iclone_toggle_state=True
        else:
                bpy.context.user_preferences.addons[__package__].preferences.option_show_iclone_toggle_state=False
        return {'FINISHED'}

def register():

    from bpy.utils import register_class

    register_class(ds_pipeline_addon_prefs)
    register_class(ds_pipeline_prefs_open)
    register_class(ds_pipeline_iclone_toggle)

    from . import ds_obj
    from . import ds_fbx

    ds_obj.register()
    ds_fbx.register()
    
    if bpy.context.user_preferences.addons[__package__].preferences.option_show_ic:

        from . import ds_ic
        ds_ic.register()

    if bpy.context.user_preferences.addons[__package__].preferences.option_show_zbc:
        
        from . import ds_zbc
        ds_zbc.register()

    if bpy.context.user_preferences.addons[__package__].preferences.option_show_sp:

        from . import ds_sp
        ds_sp.register()

    if bpy.context.user_preferences.addons[__package__].preferences.option_show_daz3d:

        from . import ds_daz3d
        ds_daz3d.register()

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Menu':

        register_class(Pipeline_Menu)
        bpy.types.INFO_HT_header.append(Draw_Pipeline_Menu)

def unregister():

    from bpy.utils import unregister_class
        
    unregister_class(ds_pipeline_addon_prefs)
    unregister_class(ds_pipeline_prefs_open)
    unregister_class(ds_pipeline_iclone_toggle)

    from . import ds_obj
    from . import ds_fbx

    ds_obj.unregister()
    ds_fbx.unregister()

    if bpy.context.user_preferences.addons[__package__].preferences.option_show_ic:

        from . import ds_ic
        ds_ic.unregister()

    if bpy.context.user_preferences.addons[__package__].preferences.option_show_zbc:
        
        from . import ds_zbc
        ds_zbc.unregister()

    if bpy.context.user_preferences.addons[__package__].preferences.option_show_sp:

        from . import ds_sp
        ds_sp.unregister()

    if bpy.context.user_preferences.addons[__package__].preferences.option_show_daz3d:

        from . import ds_daz3d
        ds_daz3d.unregister()

    if bpy.context.user_preferences.addons[__package__].preferences.option_display_type=='Menu':

        unregister_class(Pipeline_Menu)
        bpy.types.INFO_HT_header.remove(Draw_Pipeline_Menu)

if __name__ == "__main__":

	register()