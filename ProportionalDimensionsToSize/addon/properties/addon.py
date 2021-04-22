import bpy
from ..utility.addon import addon_name, get_prefs
from bpy.props import PointerProperty

from .settings import PROPORTIONALDIMENSIONSTO_Settings, draw_settings

class PROPORTIONALDIMENSIONSTO_Props(bpy.types.AddonPreferences):
    bl_idname = addon_name

    settings: PointerProperty(type=PROPORTIONALDIMENSIONSTO_Settings)

    def draw(self, context):
        prefs = get_prefs()
        layout = self.layout

        box = layout.box()
        draw_settings(prefs, box)