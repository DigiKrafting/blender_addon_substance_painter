# Blender Addon Pipeline

Provides tools for a Blender + ZBrushCore + Substance Painter + iClone 3D pipeline.

# Features

- Customised Info toolbar

- One click OBJ Import (Excluding manual file/path selection)
- One click OBJ Export (Exports selected object to export folder)

- One click FBX Import (Excluding manual file/path selection)
- One click FBX Export (Exports scene to export folder)

- One click iClone Base FBX Template Import (Copies "Base.fbxkey" to export folder and renames it to the Blender "filename.fbxkey")
- One click iClone Female FBX Template Import (Copies "Base Female.fbxkey" to export folder and renames it to the Blender "filename.fbxkey")
- One click iClone Male FBX Template Import (Copies "Base Male.fbxkey" to export folder and renames it to the Blender "filename.fbxkey")

- One click ZBrushCore OBJ Export (Exports selected object to export folder and opens file in ZBrushCore)
- One click ZBrushCore OBJ Import (Imports exported obj and replaces vertices co-ordinates on selected object)

- Application Link to Open Substance Painter (Exports scene to export folder before opening Substance Painter)
- Application Link to Open iClone Character Creator (Exports scene to export folder before opening Character Creator for manual import)
- One click iClone 3DXchange FBX Export (Exports scene to export folder and opens file in 3DXchange)
- Application Link to Open iClone (Exports scene to export folder before opening iClone for manual import)

# Required Blender Version

2.79 

\* May work in previous versions but untested, space_info.py and space_view3d.py will likely cause issues/unexpected behaviour.

# IMPORTANT USAGE NOTES 

\* Make sure you save your .blend file before using the auto import/export features or the addon won't know where to import/export the files.

- File Naming Convention

    File names are derived from the selected object name or your blender file name.

- ZBrushCore

    When exporting from ZBrushCore be sure to export to the same obj file that was used for import.

# Installation

\* GitHub automatically appends the version number to the download filenames which causes blender not to load the addon, the easy fix for this is to remove the version number from the downloaded filename before installing in Blender. E.g. addon-0.5.zip to addon.zip.

Download either the tar.gz or zip from [https://github.com/Digiography/blender_addon_pipeline/releases/latest](https://github.com/Digiography/blender_addon_pipeline/releases/latest)

Installing an Addon in Blender

- [File]->[User Preferences]
- Select [Add-ons] Tab
- Click [Install Add-on from File..]

# Screenshots

![alt](/screenshots/pipeline_prefs.png)

![alt](/screenshots/pipeline.png)
