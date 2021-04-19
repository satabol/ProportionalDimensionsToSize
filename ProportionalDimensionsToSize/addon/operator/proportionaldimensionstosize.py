import bpy
from bpy.props import FloatProperty, FloatVectorProperty, IntProperty, BoolProperty, PointerProperty, StringProperty, EnumProperty

def get_MaxSize(self):
    max_size = max( self.dimensions )
    return max_size

def set_MaxSize(self, value):
    max_size = max( self.dimensions )
    #print("scale:",self.scale)
    if value!=0:
        k = max_size / value
        if k!=0:
            self.scale[0] = self.scale[0] / k
            self.scale[1] = self.scale[1] / k
            self.scale[2] = self.scale[2] / k
    
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
        ob = context.active_object
        max_size = max(context.active_object.dimensions)
        layout = self.layout
        layout.column().prop(ob, 'pdimensions', text="Proportional Dimensions")
        layout.prop(ob, 'MaxSize')
        layout.label(text="addon: Proporional Dimenstions")

classes = (PROPORTIONALDIMENSIONSTO_PT_MaxSize,)

def register_maxsize():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Object.pdimensions = FloatVectorProperty(name="pdimensions", description="Max size by axis X/Y/Z", get=get_pdimensions, set=set_pdimensions, subtype="XYZ_LENGTH")
    bpy.types.Object.MaxSize = FloatProperty(name="Max Size", description="Max size of object", get=get_MaxSize, set=set_MaxSize, unit="LENGTH")

def unregister_maxsize():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)