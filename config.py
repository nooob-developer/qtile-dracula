# python libraries
import subprocess

#  qtile built-in libraries
from libqtile import bar, hook, qtile
from libqtile.config import Screen

# Config files and other libraries
from cfg.bindings import (init_apps_run, init_groups_keys, init_keys,
                          init_mouse_keys)
from cfg.groups import Groups_name_creator, init_group_mappings
from cfg.layouts import init_layouts
from cfg.widgets import init_widgets
from colors.dracula import Dracula


# Set up the hooks
@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "x11":
        subprocess.Popen(["picom", "-b"])
    subprocess.Popen("nm-applet")


# Set your default widget styles
colors = Dracula()
widget_themes = dict(
    font="Fira Code Nerd Font",
    fontsize=14,
    fontshadow=None,
)

# Merge the theme dictionary with the widget_defaults dictionary
widget_themes.update(colors)

layoutConfig = dict(
    margin=[10, 5, 5, 10],
    border_width=2,
    border_focus=colors["pink"],
    border_normal=colors["cyan"],
)

# Set the Vars objects
keys = init_keys()
mouse = init_mouse_keys()
apps = init_apps_run()
keys.extend(apps)
layouts = init_layouts(layoutConfig)
groups = Groups_name_creator()
groups_bind = init_groups_keys()
keys.extend(groups_bind)
group_mappings = init_group_mappings()


# Define the bar
def init_bar():
    return bar.Bar(
        init_widgets(widget_themes),
        24,
        opacity=0.66,
        background=widget_themes["background"],
        floating=True,  # allow the bar to have a shadow effect
        border_width=0,  # remove the default border
        margin=[0, 5, 5, 10],  # add some margin for the shadow effect
        draw_shadow=True,  # enable the shadow effect
        shadow_offset=[0, 3],  # set the shadow offset
    )


# Set up the screens
screens = [
    Screen(
        top=init_bar(),
        wallpaper="~/.config/qtile/wallpapers/dracula_qtile.png",
        wallpaper_mode="stretch",
    )
]

focus_on_window_activation = "smart"
drag = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
wmname = "qtile"
