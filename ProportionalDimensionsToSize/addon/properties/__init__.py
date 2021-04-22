import bpy

from .settings import PROPORTIONALDIMENSIONSTO_Settings
from .addon import PROPORTIONALDIMENSIONSTO_Props

classes = (
    PROPORTIONALDIMENSIONSTO_Settings,
    PROPORTIONALDIMENSIONSTO_Props,
)

def register_properties():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister_properties():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)