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
        "version": (0, 7, 0),
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
    bl_label = "Set Render Engine to CYCLES"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):

        bpy.context.scene.render.engine = 'CYCLES'

        return {'FINISHED'}

class ds_render_engine_game(bpy.types.Operator):

    bl_idname = "ds_render_engine.game"
    bl_label = "Set Render Engine to BLENDER_GAME"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):

        bpy.context.scene.render.engine = 'BLENDER_GAME'

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

        if bpy.context.scene.render.engine != 'BLENDER_GAME':
                layout.operator('ds_render_engine.game')

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
        option_ic_templates_path = bpy.props.StringProperty(
                name="iClone Templates Path",
                subtype='DIR_PATH',
                default="",
        )     
        option_hide_info_screens = bpy.props.BoolProperty(
                name="Screens",
                default=True,
        )     
        option_hide_info_engines = bpy.props.BoolProperty(
                name="Engines",
                default=True,
        )     
        option_hide_info_scene = bpy.props.BoolProperty(
                name="Scene",
                default=True,
        )     
        option_hide_info_switcher = bpy.props.BoolProperty(
                name="Toolbar Switcher",
                default=True,
        )     
        option_hide_info_menus = bpy.props.BoolProperty(
                name="Menus",
                default=True,
        )     
        option_show_zbc = bpy.props.BoolProperty(
                name="Show ZBrushCore Buttons",
                default=True,
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
        option_show_save = bpy.props.BoolProperty(
                name="Save Button",
                default=True,
        )     
        option_show_save_as = bpy.props.BoolProperty(
                name="Save As Button",
                default=True,
        )     
        option_show_prefs = bpy.props.BoolProperty(
                name="Preferences",
                default=True,
        )     
        option_show_screen_3dview = bpy.props.BoolProperty(
                name="3D View Full",
                default=True,
        )     
        option_show_screen_anim = bpy.props.BoolProperty(
                name="Animation",
                default=True,
        )     
        option_show_screen_compositing = bpy.props.BoolProperty(
                name="Compositing",
                default=True,
        )     
        option_show_screen_default = bpy.props.BoolProperty(
                name="Default",
                default=True,
        )     
        option_show_screen_game = bpy.props.BoolProperty(
                name="Game Logic",
                default=True,
        )     
        option_show_screen_motion = bpy.props.BoolProperty(
                name="Motion Tracking",
                default=True,
        )     
        option_show_screen_scripting = bpy.props.BoolProperty(
                name="Scripting",
                default=False,
        )     
        option_show_screen_uv = bpy.props.BoolProperty(
                name="UV Editing",
                default=True,
        )     
        option_show_screen_video = bpy.props.BoolProperty(
                name="Video Editing",
                default=True,
        )     
        option_show_console = bpy.props.BoolProperty(
                name="Console Toggle",
                default=True,
        )     
        option_show_fullscreen = bpy.props.BoolProperty(
                name="Fullscreen",
                default=True,
        )     
        option_show_menu_toggle = bpy.props.BoolProperty(
                name="Menu Toggle",
                default=True,
        )     
        option_show_menu_toggle_btn = bpy.props.BoolProperty(
                name="Menu Toggle Button State",
                default=False,
        )     
        option_show_screens_toggle = bpy.props.BoolProperty(
                name="Screens Toggle",
                default=True,
        )     
        option_show_screens_toggle_btn = bpy.props.BoolProperty(
                name="Screens Toggle Button State",
                default=False,
        )     
        option_show_quit = bpy.props.BoolProperty(
                name="Quit",
                default=True,
        )     
        option_move_blender_left = bpy.props.BoolProperty(
                name="Blender Left",
                default=True,
        )     
        option_hide_info_stats = bpy.props.BoolProperty(
                name="Stats",
                default=False,
        )     

        def draw(self, context):

                layout = self.layout

                layout.label('Info toolbar',icon='PREFERENCES')
                
                row = layout.row(align=True)
                
                col = row.column()
                subrow = col.row()
                box=subrow.box()
                box.label('Hide',icon='UI')
                box.prop(self, 'option_hide_info_switcher')
                box.prop(self, 'option_hide_info_menus')
                box.prop(self, 'option_hide_info_screens')
                box.prop(self, 'option_hide_info_scene')
                box.prop(self, 'option_hide_info_engines')
                box.prop(self, 'option_hide_info_stats')
                
                subrow = col.row()

                box=subrow.box()
                box.label('Move',icon='UI')
                box.prop(self, 'option_move_blender_left')

                col = row.column()
                box=col.box()
                box.label('Show',icon='UI')
                box.prop(self, 'option_show_menu_toggle')
                box.prop(self, 'option_show_screens_toggle')
                box.prop(self, 'option_show_save')
                box.prop(self, 'option_show_save_as')
                box.prop(self, 'option_show_fullscreen')
                box.prop(self, 'option_show_prefs')
                box.prop(self, 'option_show_console')
                box.prop(self, 'option_show_quit')

                col = row.column()
                box=col.box()
                box.label('Screens',icon='UI')
                box.prop(self, 'option_show_screen_3dview')
                box.prop(self, 'option_show_screen_anim')
                box.prop(self, 'option_show_screen_compositing')
                box.prop(self, 'option_show_screen_default')
                box.prop(self, 'option_show_screen_game')
                box.prop(self, 'option_show_screen_motion')
                box.prop(self, 'option_show_screen_scripting')
                box.prop(self, 'option_show_screen_uv')
                box.prop(self, 'option_show_screen_video')

                box=layout.box()
                box.label('Export Folder',icon='PREFERENCES')
                box.label('* Do NOT include any "\\".',icon='INFO')
                box.prop(self, 'option_export_folder')
                box.label('Automatically created as a sub folder relative to the saved .blend file.',icon='INFO')
                
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


class ds_pipeline_console(bpy.types.Operator):
    bl_idname = "ds_pipeline.console"
    bl_label = "Toggle Console"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.ops.wm.console_toggle()
        return {'FINISHED'}

class ds_pipeline_fullscreen(bpy.types.Operator):
    bl_idname = "ds_pipeline.fullscreen"
    bl_label = "Toggle Fullscreen"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.ops.wm.window_fullscreen_toggle()
        return {'FINISHED'}

class ds_pipeline_menu_toggle(bpy.types.Operator):
    bl_idname = "ds_pipeline.menu_toggle"
    bl_label = "Menu"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):

        if not bpy.context.user_preferences.addons[__package__].preferences.option_show_menu_toggle_btn:
                bpy.context.user_preferences.addons[__package__].preferences.option_show_menu_toggle_btn=True
        else:
                bpy.context.user_preferences.addons[__package__].preferences.option_show_menu_toggle_btn=False
        return {'FINISHED'}

class ds_pipeline_screens_toggle(bpy.types.Operator):
    bl_idname = "ds_pipeline.screens_toggle"
    bl_label = "Screens"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):

        if not bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn:
                bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=True
        else:
                bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}

class ds_pipeline_quit(bpy.types.Operator):
    bl_idname = "ds_pipeline.quit"
    bl_label = "Quit"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.ops.wm.quit_blender()
        return {'FINISHED'}

class ds_pipeline_screen_default(bpy.types.Operator):

    bl_idname = "ds_pipeline.screen_default"
    bl_label = "Open Preferences"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):
        
        bpy.context.window.screen = bpy.data.screens['Default']

        return {'FINISHED'}

class ds_pipeline_screen_3dview(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_3dview"
    bl_label = "3D View"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['3D View Full']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_anim(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_anim"
    bl_label = "Animation"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['Animation']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_compositing(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_compositing"
    bl_label = "Compositing"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['Compositing']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_default(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_default"
    bl_label = "Default"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['Default']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_game(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_game"
    bl_label = "Game Logic"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['Game Logic']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_motion(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_motion"
    bl_label = "Motion Tracking"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['Motion Tracking']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_scripting(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_scripting"
    bl_label = "Scripting"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['Scripting']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_uv(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_uv"
    bl_label = "UV Editing"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['UV Editing']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}
class ds_pipeline_screen_video(bpy.types.Operator):
    bl_idname = "ds_pipeline.screen_video"
    bl_label = "Video Editing"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens['Video Editing']
        bpy.context.user_preferences.addons[__package__].preferences.option_show_screens_toggle_btn=False
        return {'FINISHED'}

class ds_pipeline_prefs_open(bpy.types.Operator):

    bl_idname = "ds_pipeline.prefs_open"
    bl_label = "Open Preferences"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):
        
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')

        return {'FINISHED'}

class ds_save(bpy.types.Operator):

    bl_idname = "ds.save"
    bl_label = "Save"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):

        bpy.ops.wm.save_mainfile()

        return {'FINISHED'}

class ds_save_as(bpy.types.Operator):

    bl_idname = "ds.save_as"
    bl_label = "Save As"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
 
    def execute(self, context):

        bpy.ops.wm.save_as_mainfile()

        return {'FINISHED'}

def register():

    from bpy.utils import register_class

    register_class(ds_pipeline_menu_toggle)
    register_class(ds_pipeline_screens_toggle)
    
    register_class(ds_save)
    register_class(ds_save_as)
    register_class(ds_pipeline_addon_prefs)
    register_class(ds_pipeline_prefs_open)
    register_class(ds_pipeline_console)
    register_class(ds_pipeline_fullscreen)
    register_class(ds_pipeline_quit)

    register_class(ds_render_engine_cycles)
    register_class(ds_render_engine_game)

    register_class(ds_pipeline_screen_3dview)
    register_class(ds_pipeline_screen_anim)
    register_class(ds_pipeline_screen_compositing)
    register_class(ds_pipeline_screen_default)
    register_class(ds_pipeline_screen_game)
    register_class(ds_pipeline_screen_motion)
    register_class(ds_pipeline_screen_scripting)
    register_class(ds_pipeline_screen_uv)
    register_class(ds_pipeline_screen_video)

    register_class(ds_scene)

    from . import space_info 

    register_class(space_info.INFO_HT_header)

    from . import ds_obj
    from . import ds_fbx

    ds_obj.register()
    ds_fbx.register()

    from . import ds_ic
    from . import ds_zbc
    from . import ds_sp
    from . import ds_daz3d

    ds_ic.register()
    ds_zbc.register()
    ds_sp.register()
    ds_daz3d.register()

def unregister():

    from bpy.utils import unregister_class
        
    unregister_class(ds_pipeline_menu_toggle)
    unregister_class(ds_pipeline_screens_toggle)

    unregister_class(ds_save)
    unregister_class(ds_save_as)
    unregister_class(ds_pipeline_addon_prefs)
    unregister_class(ds_pipeline_prefs_open)
    unregister_class(ds_pipeline_console)
    unregister_class(ds_pipeline_fullscreen)
    unregister_class(ds_pipeline_quit)

    unregister_class(ds_render_engine_cycles)
    unregister_class(ds_render_engine_game)
    unregister_class(ds_scene)

    unregister_class(ds_pipeline_screen_3dview)
    unregister_class(ds_pipeline_screen_anim)
    unregister_class(ds_pipeline_screen_compositing)
    unregister_class(ds_pipeline_screen_default)
    unregister_class(ds_pipeline_screen_game)
    unregister_class(ds_pipeline_screen_motion)
    unregister_class(ds_pipeline_screen_scripting)
    unregister_class(ds_pipeline_screen_uv)
    unregister_class(ds_pipeline_screen_video)

    from . import ds_obj
    from . import ds_fbx

    ds_obj.unregister()
    ds_fbx.unregister()

    from . import ds_ic
    from . import ds_zbc
    from . import ds_sp
    from . import ds_daz3d

    ds_ic.unregister()
    ds_zbc.unregister()
    ds_sp.unregister()
    ds_daz3d.unregister()

    from . import space_info 

    unregister_class(space_info.INFO_HT_header)

if __name__ == "__main__":

	register()