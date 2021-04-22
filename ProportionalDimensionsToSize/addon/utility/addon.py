import bpy
import bpy.types
from bpy.props import FloatProperty, FloatVectorProperty, IntProperty, BoolProperty, PointerProperty, StringProperty, EnumProperty

addon_name = __name__.partition('.')[0]

def get_prefs():
    return bpy.context.preferences.addons[addon_name].preferences