# Blender Addon Pipeline

Pipeline import/export/open for ZBrushCore, Substance Painter, iClone, Daz3D.

# Features

## ZBrushCore
- One click ZBrushCore OBJ Export (Exports selected object to export folder and opens file in ZBrushCore)
- One click ZBrushCore OBJ Import (Imports exported obj and replaces vertices co-ordinates on selected object)

\* When exporting from ZBrushCore be sure to export to the same obj file that was used for import.

## Substance Painter
- One Click Substance Painter OBJ Export (Exports selected object to export folder and opens file in Substance Painter)
- One Click Substance Painter FBX Export (Exports scene to export folder and opens file in Substance Painter)

\* Creates SPP Project File "filename.spp" and passes textures folder from preferences for export.

## iClone/Character Creator/3DXchange
- One click iClone Base FBX Template Import (Copies "Base.fbxkey" to export folder and renames it to the Blender "filename.fbxkey")
- One click iClone Female FBX Template Import (Copies "Base Female.fbxkey" to export folder and renames it to the Blender "filename.fbxkey")
- One click iClone Male FBX Template Import (Copies "Base Male.fbxkey" to export folder and renames it to the Blender "filename.fbxkey")
- One click iClone 3DXchange FBX Export (Exports scene to export folder and opens file in 3DXchange)
- Application Link to Open iClone Character Creator (Exports scene to export folder before opening Character Creator for manual import)
- Application Link to Open iClone
## Daz3D
- Application Link to Open Daz3D (Exports scene to export folder before opening Daz3D for manual import)

# Required Blender Version

2.79.0

\* Will likely work in previous versions but untested.

# IMPORTANT USAGE NOTES 

\* Make sure you have a saved .blend file before using the auto import/export features, then saving before import/export is then not required. The addon needs the file location to know where to create the export and textures folder used for import/export of the files.

- File Naming Convention

    File names are derived from the selected object name or your blender file name.

# Installation

Download either the tar.gz or zip from [https://github.com/Digiography/blender_addon_pipeline/releases/latest](https://github.com/Digiography/blender_addon_pipeline/releases/latest)

Installing an Addon in Blender

- [File]->[User Preferences]
- Select [Add-ons] Tab
- Click [Install Add-on from File..]

# Screenshots

![alt](/screenshots/pipeline_prefs.png)

![alt](/screenshots/pipeline.png)
