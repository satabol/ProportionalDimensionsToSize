import bpy
from bpy.props import FloatProperty, FloatVectorProperty, IntProperty, BoolProperty, PointerProperty, StringProperty, EnumProperty
from ..utility.addon import get_prefs
from ... import draw_call_settings_button


def get_MaxSize(self):
    max_size = max( self.dimensions )
    return max_size

def set_MaxSize(self, value):
    max_size = max( self.dimensions )
    if value!=0:
        k = max_size / value
        if k!=0:
            self.scale[0] = self.scale[0] / k
            self.scale[1] = self.scale[1] / k
            self.scale[2] = self.scale[2] / k

            for obj in bpy.context.selected_objects:
                if hasattr(obj, "scale")==True and obj is not self:
                    obj.scale[0] = obj.scale[0] / k
                    obj.scale[1] = obj.scale[1] / k
                    obj.scale[2] = obj.scale[2] / k

    return None

def get_pdimensions(self):
    return self.dimensions

def set_pdimensions(self, value):
    if value is not None:
        k=0
        if self.dimensions[0]!=value[0]:
            k = self.dimensions[0] / value[0]
        elif self.dimensions[1]!=value[1]:
            k = self.dimensions[1] / value[1]
        elif self.dimensions[2]!=value[2]:
            k = self.dimensions[2] / value[2]

        if k!=0:
            self.scale[0] = self.scale[0] / k
            self.scale[1] = self.scale[1] / k
            self.scale[2] = self.scale[2] / k
    
            for obj in bpy.context.selected_objects:
                if hasattr(obj, "scale")==True and obj is not self:
                    obj.scale[0] = obj.scale[0] / k
                    obj.scale[1] = obj.scale[1] / k
                    obj.scale[2] = obj.scale[2] / k

    return None

class PROPORTIONALDIMENSIONSTO_PT_MaxSize(bpy.types.Panel):
    """Panel Proportional Dimensions to new Size"""
    bl_idname = "PROPORTIONALDIMENSIONSTO_PT_MaxSize"
    bl_label = "Proportional Dimensions"
    bl_order = 0
    #bl_options = {"DEFAULT_CLOSED"}

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"

    @classmethod
    def poll(self, context):
        res = False
        #if context.mode=='OBJECT' and context.active_object is not None and context.active_object.type=="MESH":
        if context.mode=='OBJECT' and context.active_object is not None and hasattr(context.active_object, "dimensions")==True:
            res = True
        return res

    def draw(self, context):
        global draw_call_settings_button

        ob = context.active_object
        max_size = max(context.active_object.dimensions)
        layout = self.layout
        row = layout.row(align=True) 
        split = row.split(factor=0.8)
        split.column().prop(ob, 'pdimensions', text="Proportional Dimensions")
        #split = split.split(factor=0.2)
        #col1 = row.column()
        col1 = split.column()
        col1.scale_y = .9
        col1.row().label(text="")
        col1.row().operator("proportionaldimensionsto.setx1", text="1")
        col1.row().operator("proportionaldimensionsto.sety1", text="1")
        col1.row().operator("proportionaldimensionsto.setz1", text="1")
        
        row = layout.row(align=True)
        split = row.split(factor=0.8)
        split.column().prop(ob, 'MaxSize')
        col1 = split.column()
        col1.scale_y = 1
        col1.row().operator("proportionaldimensionsto.setmaxsize1", text="1")

        row = layout.row(align=True)
        row.label(text="addon: Proportional Dimensions, settings:")
        draw_call_settings_button(row)

class PROPORTIONALDIMENSIONSTO_OP_SetX1(bpy.types.Operator):
    """Set object dimension X=1"""
    bl_idname = "proportionaldimensionsto.setx1"
    bl_label  = "Set object's dimension X=1"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        res = False
        if context.mode=='OBJECT' and context.active_object is not None and hasattr(context.active_object, "dimensions")==True:
            res = True
        return res

    def execute(self, context):
        ob = context.active_object
        ob.pdimensions[0]=1.0
        return {"FINISHED"}

class PROPORTIONALDIMENSIONSTO_OP_SetY1(bpy.types.Operator):
    """Set object dimension Y=1"""
    bl_idname = "proportionaldimensionsto.sety1"
    bl_label  = "Set object's dimension Y=1"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        res = False
        if context.mode=='OBJECT' and context.active_object is not None and hasattr(context.active_object, "dimensions")==True:
            res = True
        return res

    def execute(self, context):
        ob = context.active_object
        ob.pdimensions[1]=1.0
        return {"FINISHED"}

class PROPORTIONALDIMENSIONSTO_OP_SetZ1(bpy.types.Operator):
    """Set object dimension Z=1"""
    bl_idname = "proportionaldimensionsto.setz1"
    bl_label  = "Set object's dimension Z=1"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        res = False
        if context.mode=='OBJECT' and context.active_object is not None and hasattr(context.active_object, "dimensions")==True:
            res = True
        return res

    def execute(self, context):
        ob = context.active_object
        ob.pdimensions[2]=1.0
        return {"FINISHED"}

class PROPORTIONALDIMENSIONSTO_OP_SetMaxSize1(bpy.types.Operator):
    """Set object's max dimension =1"""
    bl_idname = "proportionaldimensionsto.setmaxsize1"
    bl_label  = "Set object's max dimension =1"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        res = False
        if context.mode=='OBJECT' and context.active_object is not None and hasattr(context.active_object, "dimensions")==True:
            res = True
        return res

    def execute(self, context):
        ob = context.active_object
        ob.MaxSize=1.0
        return {"FINISHED"}


classes = (PROPORTIONALDIMENSIONSTO_PT_MaxSize,
    PROPORTIONALDIMENSIONSTO_OP_SetX1,PROPORTIONALDIMENSIONSTO_OP_SetY1,PROPORTIONALDIMENSIONSTO_OP_SetZ1,
    PROPORTIONALDIMENSIONSTO_OP_SetMaxSize1,
    )

def register_object_props(precision):
    bpy.types.Object.pdimensions = FloatVectorProperty(name="pdimensions", description="Max size by axis X/Y/Z", get=get_pdimensions, set=set_pdimensions, subtype="XYZ_LENGTH", precision=precision)
    bpy.types.Object.MaxSize     = FloatProperty(name="Max Size", description="Max size of object", get=get_MaxSize, set=set_MaxSize, unit="LENGTH", precision=precision)

def update_types(self, context):
    pref = get_prefs()
    precision = pref.settings.precision
    register_object_props(precision)


def register_maxsize():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    register_object_props(3)

def unregister_maxsize():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)