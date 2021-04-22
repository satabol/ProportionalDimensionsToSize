bl_info = {
    "name": "ProportionalDimensionsToSize",
    "description" : "Proportional Dimensions to new size", 
    "author": "satabol@yandex.ru",
    "version": (1,0,5),
    "blender": (2,90,0),
    "location": "View3D",
    "category": "3D View",
    "wiki_url": "https://github.com/satabol/ProportionalDimensionsToSize",
}

def register():
    from .addon.register import register_addon
    register_addon()

def unregister():
    from .addon.register import unregister_addon
    unregister_addon()