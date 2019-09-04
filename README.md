# Blender Addon Substance Painter

Pipeline/Workflow import/export for Substance Painter.

# Features

- Blender 2.80 (Tested on Linux/Windows)

- Export in either FBX or OBJ.
- Exports to export folder and opens Substance Painter.
- Creates SPP Project File "{mesh}.spp" or "{filename}.spp". * (Excludes 2018.1.0-2018.3.0)
- Passes textures folder from preferences to Substance Painter.
- Creates Nodes using the Principled BSDF shader.
- Autosave before export option.
- Use Relative Paths option.
- Creates nodes for Unreal Engine Textures. * (On detection of OcclusionRoughnessMetallic texture)
- Optional Height Maps (Combines Height and Normal maps using the Bump Node, use with care, see screenshots below)

## Selected Mesh

- One Click Export
- One Click Textures Import

## Scene

- One Click Export
- One Click Textures Import

# IMPORTANT USAGE NOTES

\* Make sure you have a **"saved"** .blend file before using the import/export features, then saving before import/export is then not required. The addon needs the file location to know where to create the export and textures folder used for import/export of the files.

- File Naming Convention

    File names are derived from the selected object name or your blender file name.

\* For Substance Painter 2018.1.0-2018.3.0 be sure to tick "2018.1.0-2018.3.0 Project File Fix" in the addon preferences. (See "Preferences" screenshot below)

# Installation

Download either the tar.gz or zip from [https://github.com/DigiKrafting/blender_addon_substance_painter/releases/latest](https://github.com/DigiKrafting/blender_addon_substance_painter/releases/latest)

Installing an Addon in Blender

- [Edit]->[Preferences]
- Select [Add-ons] Tab
- Click [Install]
- Browse to download location of ZIP.
- Click [Install Add-on from File..]

# Min Required Blender Version

2.79.0 (1.4.0)

\* Mesh Export will likely work in previous versions but untested.
\* Texture Import requires the Principled BSDF shader in 2.79.0+.

2.80.0+ (1.5.0+)

# Screenshots

![alt](/screenshots/sp_debian.png)

![alt](/screenshots/sp_2_8_0_rc_1.png)

## Opacity

![alt](/screenshots/sp_opacity.png)

## UE4 Nodes

![alt](/screenshots/sp_unreal.png)

## Emissive

![alt](/screenshots/sp_emissive.png)

## Nostalgia

![alt](/screenshots/sp.png)

## Preferences

![alt](/screenshots/sp_prefs.png)

# Normal / Normal + Height Comparision

## Substance Painter Viewport

![alt](/screenshots/sp_normals_sp.png)

## Normal Map (* Eevee with Ambient Occlusion enabled)

![alt](/screenshots/sp_Map_Normal.png)

## Height Map combined with Normal Map (* Eevee with Ambient Occlusion enabled)

![alt](/screenshots/sp_Map_Normal_Height.png)
