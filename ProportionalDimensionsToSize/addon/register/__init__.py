import bpy

def register_addon():
    from ..operator import register_operators
    from ..properties import register_properties
    register_operators()
    register_properties()

def unregister_addon():
    from ..operator import unregister_operators
    from ..properties import unregister_properties
    unregister_operators()
    unregister_properties()
