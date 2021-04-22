import bpy
from bpy.props import IntProperty
from ..operator.proportionaldimensionstosize import update_types

class PROPORTIONALDIMENSIONSTO_Settings(bpy.types.PropertyGroup):

    precision: IntProperty(
        name = 'Precision', description = 'precision of units',
        min = 3, max = 10, default = 3,
        update = update_types
    )

def draw_settings(prefs, layout):
    layout.label(text='General Settings', icon='TOOL_SETTINGS')

    box = layout.box()
    row = box.row()
    row.label(text='Precision of units')
    row.prop(prefs.settings, 'precision', text='')