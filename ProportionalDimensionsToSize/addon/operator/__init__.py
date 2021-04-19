import bpy

from ..operator.proportionaldimensionstosize import register_maxsize, unregister_maxsize

def register_operators():
    register_maxsize()

def unregister_operators():
    unregister_maxsize()