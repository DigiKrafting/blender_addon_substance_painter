# Blender Addon Pipeline

Provides tools for a Blender + ZBrushCore + Substance Painter + iClone 3D pipeline.

# Features

- One click OBJ Import (Excluding manual file/path selection)
- One click OBJ Export (Exports selected object to Export Folder)

- One click FBX Import (Excluding manual file/path selection)
- One click FBX Export (Exports scene to export folder)

- One click iClone Base FBX Template Import (Copies "Base.fbxkey" to export folder and renames to your blender filename)
- One click iClone Female FBX Template Import (Copies "Base Female.fbxkey" to export folder and renames to your blender filename)
- One click iClone Male FBX Template Import (Copies "Base Male.fbxkey" to export folder and renames to your blender filename)

- One click ZBrushCore OBJ Export (Exports selected object to export folder and opens file in ZBrushCore)
- One click ZBrushCore OBJ Import (Imports exported obj and replaces vertices co-ordinates on selected object)

- Application Link to Open Substance Painter 
- Application Link to Open iClone Character Creator
- One click iClone 3DXchange FBX Export (Exports scene to export folder and opens file in 3DXchange)
- Application Link to Open iClone

- Customised 3D View toolbar (* WIP: Likely to be changed/tweaked)

# Required Blender Version

2.79 

\* May work in previous versions but untested, space_info.py and space_view3d.py will likely cause unexpected behaviour.

# IMPORTANT USAGE NOTES 

\* Make sure you save your .blend file before using the auto import/export features or the addon won't know where to import/export the files.

- File Naming Convention

File names are derived from the selected object name or your blender file name.

- ZBrushCore

When exporting from ZBrushCore be sure to export to the same obj file that was used for import.

# Installation

Download either the tar.gz or zip from [https://github.com/Digiography/blender_addon_pipeline/releases/latest](https://github.com/Digiography/blender_addon_pipeline/releases/latest)

Installing an Addon in Blender

- [File]->[User Preferences]
- Select [Add ons'] Tab.
- Click [Install Addon from File..].

# Screenshots

![alt](/screenshots/pipeline_prefs.png)

![alt](/screenshots/pipeline.png)
