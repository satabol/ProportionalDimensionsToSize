import bpy

def register_addon():
    from ..operator import register_operators
    register_operators()

def unregister_addon():
    from ..operator import unregister_operators
    unregister_operators()