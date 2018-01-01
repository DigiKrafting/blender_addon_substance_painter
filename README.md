# Blender Addon Substance Painter

Pipeline/Workflow import/export for Substance Painter.

# Features

- One Click Substance Painter Object Export (Exports selected object to export folder and opens file in Substance Painter)
- One Click Import of created Textures for Object (Imports from set folder and creates Nodes using the Principled BSDF shader)
- One Click Substance Painter Scene Export (Exports scene to export folder and opens file in Substance Painter)
- One Click Import of created Textures for Scene (Imports from set folder and creates Nodes using the Principled BSDF shader)
- Export in either FBX or OBJ

\* Creates SPP Project File "filename.spp" and passes textures folder from preferences for export.

# Required Blender Version

2.79.0

\* Will likely work in previous versions but untested.

# IMPORTANT USAGE NOTES 

\* Make sure you have a saved .blend file before using the auto import/export features, then saving before import/export is then not required. The addon needs the file location to know where to create the export and textures folder used for import/export of the files.

- File Naming Convention

    File names are derived from the selected object name or your blender file name.

# Installation

Download either the tar.gz or zip from [https://github.com/Digiography/blender_addon_substance_painter/releases/latest](https://github.com/Digiography/blender_addon_substance_painter/releases/latest)

Installing an Addon in Blender

- [File]->[User Preferences]
- Select [Add-ons] Tab
- Click [Install Add-on from File..]

# Screenshots

![alt](/screenshots/pipeline_prefs.png)

![alt](/screenshots/pipeline.png)
