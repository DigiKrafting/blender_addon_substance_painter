import bpy

from os import path, makedirs

def get_export_path():

    _export_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_export_folder + '\\'

    if not path.exists(_export_path):
        makedirs(_export_path)

    return _export_path

def get_textures_path():

    _textures_path = bpy.path.abspath('//') + bpy.context.user_preferences.addons[__package__].preferences.option_textures_folder + '\\'

    if not path.exists(_textures_path):
        makedirs(_textures_path)

    return _textures_path