import bpy

class ds_3d_view_edit(bpy.types.Operator):

    bl_idname = "ds_3d_view.edit"
    bl_label = "ds_3d_view.edit"
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

        return {'FINISHED'}

def ds_3d_view_edit_button(self, context):
    self.layout.operator(ds_3d_view_edit.bl_idname,text="",icon="EDITMODE_HLT")

class ds_3d_view_object(bpy.types.Operator):

    bl_idname = "ds_3d_view.object"
    bl_label = "ds_3d_view.object"
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        return {'FINISHED'}

def ds_3d_view_object_button(self, context):
    self.layout.operator(ds_3d_view_object.bl_idname,text="",icon="OBJECT_DATAMODE")

####################################################################################################################################

def ds_3d_view_select_mode_vertex_button(self, context):
    self.layout.operator_context = 'INVOKE_REGION_WIN'
    self.layout.operator("mesh.select_mode", text="", icon='VERTEXSEL').type = 'VERT'

def ds_3d_view_select_mode_edge_button(self, context):
    self.layout.operator_context = 'INVOKE_REGION_WIN'
    self.layout.operator("mesh.select_mode", text="", icon='EDGESEL').type = 'EDGE'

def ds_3d_view_select_mode_face_button(self, context):
    self.layout.operator_context = 'INVOKE_REGION_WIN'
    self.layout.operator("mesh.select_mode", text="", icon='FACESEL').type = 'FACE'

class ds_3d_view_edit_face_delete(bpy.types.Operator):
    bl_idname = "ds_3d_view.edit_face_delete"
    bl_label = "ds_3d_view.edit_face_delete"
    def execute(self, context):
        bpy.ops.mesh.delete(type='FACE')
        return {'FINISHED'}

def ds_3d_view_edit_face_delete_button(self, context):
    self.layout.operator(ds_3d_view_edit_face_delete.bl_idname,text="",icon="FACESEL")

class ds_3d_view_edit_edge_delete(bpy.types.Operator):
    bl_idname = "ds_3d_view.edit_edge_delete"
    bl_label = "ds_3d_view.edit_edge_delete"
    def execute(self, context):
        bpy.ops.mesh.delete(type='EDGE')
        return {'FINISHED'}

def ds_3d_view_edit_edge_delete_button(self, context):
    self.layout.operator(ds_3d_view_edit_edge_delete.bl_idname,text="",icon="EDGESEL")

class ds_3d_view_edit_vertex_delete(bpy.types.Operator):
    bl_idname = "ds_3d_view.edit_vertex_delete"
    bl_label = "ds_3d_view.edit_vertex_delete"
    def execute(self, context):
        bpy.ops.mesh.delete(type='VERT')
        return {'FINISHED'}

def ds_3d_view_edit_vertex_delete_button(self, context):
    self.layout.operator(ds_3d_view_edit_vertex_delete.bl_idname,text="",icon="VERTEXSEL")

####################################################################################################################################

class ds_3d_view_select_all(bpy.types.Operator):

    bl_idname = "ds_3d_view.select_all"
    bl_label = "ds_3d_view.select_all"

    def execute(self, context):

        _scene = bpy.context.scene
        if bpy.context.active_object.mode=='OBJECT':
            for ob in _scene.objects:
                if ob.type == 'MESH':
                    ob.select = True
        elif bpy.context.active_object.mode=='EDIT':
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.select_all(action='SELECT')

        return {'FINISHED'}

def ds_3d_view_select_all_button(self, context):
    self.layout.operator(ds_3d_view_select_all.bl_idname, text="S")

class ds_3d_view_select_none(bpy.types.Operator):

    bl_idname = "ds_3d_view.select_none"
    bl_label = "ds_3d_view.select_none"

    def execute(self, context):

        _scene = bpy.context.scene
        if bpy.context.active_object.mode=='OBJECT':
            for ob in _scene.objects:
                if ob.type == 'MESH':
                    ob.select = False
        elif bpy.context.active_object.mode=='EDIT':
            bpy.ops.mesh.select_all(action='DESELECT')

        return {'FINISHED'}

def ds_3d_view_select_none_button(self, context):
    self.layout.operator(ds_3d_view_select_none.bl_idname, text="De")

####################################################################################################################################

def ds_3d_view_uvs_mark_button(self, context):
    self.layout.operator('mesh.mark_seam',text="M",icon="EDGESEL").clear = False

def ds_3d_view_uvs_clear_button(self, context):
    self.layout.operator('mesh.mark_seam',text="U",icon="EDGESEL").clear = True

def ds_3d_view_uvs_unwrap_button(self, context):
    self.layout.operator('uv.unwrap',text="UV Unwrap",icon="MOD_UVPROJECT")

def ds_3d_view_top_button(self, context):
    self.layout.operator("view3d.viewnumpad", text="T").type = 'TOP'

def ds_3d_view_bottom_button(self, context):
    self.layout.operator("view3d.viewnumpad", text="B").type = 'BOTTOM'

def ds_3d_view_front_button(self, context):
    self.layout.operator("view3d.viewnumpad", text="F").type = 'FRONT'

def ds_3d_view_back_button(self, context):
    self.layout.operator("view3d.viewnumpad", text="B").type = 'BACK'

def ds_3d_view_right_button(self, context):
    self.layout.operator("view3d.viewnumpad", text="R").type = 'RIGHT'

def ds_3d_view_left_button(self, context):
    self.layout.operator("view3d.viewnumpad", text="L").type = 'LEFT'

def ds_3d_view_selected_button(self, context):
    self.layout.operator("view3d.view_selected", text="C")

def ds_3d_view_wireframe_button(self, context):

    f = self.layout.operator("wm.context_set_enum", icon='WIRE', text='')
    f.data_path='space_data.viewport_shade'
    f.value = 'WIREFRAME'

def ds_3d_view_solid_button(self, context):

    f = self.layout.operator("wm.context_set_enum", icon='SOLID', text='')
    f.data_path='space_data.viewport_shade'
    f.value = 'SOLID'

def ds_3d_view_material_button(self, context):

    f = self.layout.operator("wm.context_set_enum", icon='MATERIAL', text='')
    f.data_path='space_data.viewport_shade'
    f.value = 'MATERIAL'    

def ds_3d_view_select_border(self, context):
    self.layout.operator("view3d.select_border", text='B')

def ds_3d_view_select_circle(self, context):
    self.layout.operator("view3d.select_circle", text='C')

def register():

    from bpy.utils import register_class
    from bpy.types import VIEW3D_HT_header as VIEW3D_HT_header

    register_class(ds_3d_view_edit)
    register_class(ds_3d_view_object)

    register_class(ds_3d_view_select_all)
    register_class(ds_3d_view_select_none)

    register_class(ds_3d_view_edit_vertex_delete)
    register_class(ds_3d_view_edit_edge_delete)
    register_class(ds_3d_view_edit_face_delete)

    VIEW3D_HT_header.append(ds_3d_view_selected_button)
    VIEW3D_HT_header.append(ds_3d_view_front_button)
    VIEW3D_HT_header.append(ds_3d_view_back_button)
    VIEW3D_HT_header.append(ds_3d_view_left_button)
    VIEW3D_HT_header.append(ds_3d_view_right_button)
    VIEW3D_HT_header.append(ds_3d_view_top_button)
    VIEW3D_HT_header.append(ds_3d_view_bottom_button)

    VIEW3D_HT_header.append(ds_3d_view_wireframe_button)
    VIEW3D_HT_header.append(ds_3d_view_solid_button)
    VIEW3D_HT_header.append(ds_3d_view_material_button)

    VIEW3D_HT_header.append(ds_3d_view_edit_button)
    VIEW3D_HT_header.append(ds_3d_view_object_button)

    VIEW3D_HT_header.append(ds_3d_view_select_all_button)
    VIEW3D_HT_header.append(ds_3d_view_select_none_button)
    VIEW3D_HT_header.append(ds_3d_view_select_circle)
    VIEW3D_HT_header.append(ds_3d_view_select_border)

    VIEW3D_HT_header.append(ds_3d_view_select_mode_vertex_button)
    VIEW3D_HT_header.append(ds_3d_view_select_mode_edge_button)
    VIEW3D_HT_header.append(ds_3d_view_select_mode_face_button)

    VIEW3D_HT_header.append(ds_3d_view_edit_vertex_delete_button)
    VIEW3D_HT_header.append(ds_3d_view_edit_edge_delete_button)
    VIEW3D_HT_header.append(ds_3d_view_edit_face_delete_button)

    VIEW3D_HT_header.append(ds_3d_view_uvs_mark_button)
    VIEW3D_HT_header.append(ds_3d_view_uvs_clear_button)
    VIEW3D_HT_header.append(ds_3d_view_uvs_unwrap_button)

def unregister():

    from bpy.utils import unregister_class
    from bpy.types import VIEW3D_HT_header as VIEW3D_HT_header

    unregister_class(ds_3d_view_edit)
    unregister_class(ds_3d_view_object)

    unregister_class(ds_3d_view_select_all)
    unregister_class(ds_3d_view_select_none)

    unregister_class(ds_3d_view_edit_vertex_delete)
    unregister_class(ds_3d_view_edit_edge_delete)
    unregister_class(ds_3d_view_edit_face_delete)

    VIEW3D_HT_header.remove(ds_3d_view_selected_button)
    VIEW3D_HT_header.remove(ds_3d_view_front_button)
    VIEW3D_HT_header.remove(ds_3d_view_back_button)
    VIEW3D_HT_header.remove(ds_3d_view_left_button)
    VIEW3D_HT_header.remove(ds_3d_view_right_button)
    VIEW3D_HT_header.remove(ds_3d_view_top_button)
    VIEW3D_HT_header.remove(ds_3d_view_bottom_button)

    VIEW3D_HT_header.remove(ds_3d_view_wireframe_button)
    VIEW3D_HT_header.remove(ds_3d_view_solid_button)
    VIEW3D_HT_header.remove(ds_3d_view_material_button)

    VIEW3D_HT_header.remove(ds_3d_view_edit_button)
    VIEW3D_HT_header.remove(ds_3d_view_object_button)

    VIEW3D_HT_header.remove(ds_3d_view_select_all_button)
    VIEW3D_HT_header.remove(ds_3d_view_select_none_button)
    VIEW3D_HT_header.remove(ds_3d_view_select_circle)
    VIEW3D_HT_header.remove(ds_3d_view_select_border)

    VIEW3D_HT_header.remove(ds_3d_view_select_mode_vertex_button)
    VIEW3D_HT_header.remove(ds_3d_view_select_mode_edge_button)
    VIEW3D_HT_header.remove(ds_3d_view_select_mode_face_button)

    VIEW3D_HT_header.remove(ds_3d_view_edit_vertex_delete_button)
    VIEW3D_HT_header.remove(ds_3d_view_edit_edge_delete_button)
    VIEW3D_HT_header.remove(ds_3d_view_edit_face_delete_button)

    VIEW3D_HT_header.remove(ds_3d_view_uvs_mark_button)
    VIEW3D_HT_header.remove(ds_3d_view_uvs_clear_button)
    VIEW3D_HT_header.remove(ds_3d_view_uvs_unwrap_button)    