bl_info = {
    "name": "ProportionalDimensionsToSize",
    "description" : "Proportional Dimensions to new size", 
    "author": "satabol@yandex.ru",
    "version": (1,0,6),
    "blender": (2,90,0),
    "location": "View3D",
    "category": "3D View",
    "wiki_url": "https://github.com/satabol/ProportionalDimensionsToSize",
}

def draw_call_settings_button(layout):
    layout.operator(
                "preferences.addon_show", icon="SETTINGS"
            ).module = __package__

def register():
    from .addon.register import register_addon
    register_addon()
    print("__package__:", __package__)

def unregister():
    from .addon.register import unregister_addon
    unregister_addon()