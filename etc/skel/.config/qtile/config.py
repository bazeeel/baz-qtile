# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Match, Rule, ScratchPad, DropDown
from libqtile.command import lazy, Client
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer
from libqtile.dgroups import simple_key_binder
from libqtile.manager import Qtile


try:
    from typing import List  # noqa: F401
except ImportError:
    pass

mod = "mod4"
#myTerm="urxvt"
myBrowser="chromium"


cls_grp_dict = {
    "luakit": "1", "Firefox": "1", "Opera": "1", "Google-chrome": "1",
    "Chromium": "1", "Vivaldi-stable": "1", "Midori": "2", "Dillo": "2",
    "Netsurf-gtk3": "2", "QupZilla": "2", "Uget-gtk": "2", "Tor Browser": "1",
    "Waterfox": "1", "UXTerm": "3", "Termite": "3", "Terminator": "3",
    "URxvt": "3", "mlterm": "3", "Lxterminal": "3",
    "XTerm": "3", "discord": "4", "Pcmanfm": "8", "Thunar": "8", "dolphin": "8", "Caja": "8",
    "Catfish": "8", "Zathura": "5", "libreoffice-writer": "5", "libreoffice": "5",
    "Leafpad": "5", "kate": "5", "Pluma": "5", "Mousepad": "5",
    "kwrite": "5", "Geany": "5", "Gedit": "5", "Code": "5",
    "Atom": "5", "Gimp": "6", "Gthumb": "6", "org.kde.gwenview": "6",
    "Ristretto": "6", "lximage-qt": "6", "Eom": "6", "Gpicview": "6",
    "vlc": "7", "xv/mplayer": "7", "Clementine": "7", "MPlayer": "7",
    "smplayer": "7", "mpv": "7", "Gnome-mpv": "7", "Rhythmbotx": "7",
    "Pragha": "7", "Steam": "8", "Wine": "8", "thunar": "8",
    "PlayOnLinux": "8", "VirtualBox": "9", "okular": "9", "calibre": "9",
    "octopi": "9", "Pamac-updater": "9", "Pamac-manager": "9", "Lxtask": "9",
    "Dukto": "9", "QuiteRss": "9", "Filezilla": "9",
    "jetbrains-pycharm-ce": "5",
}

role_grp_dict = {
    "browser": "1", "gimp-image-window": "5", "filemanager": "8",

}

group_exclusives = [
    False, False, False,
    False, False, False,
    False, False, False,
    False,
]

group_persists = [
    True, True, True,
    True, True, True,
    True, True, True,
    True,
]
group_inits = [
    True, True, True,
    True, True, True,
    True, True, True,
    True,
]


group_matches = [

    [Match(wm_class=[
        "luakit", "Firefox", "Opera", "Google-chrome",
        "Chromium", "Vivaldi-stable", "Midori",
        "Dillo", "Netsurf-gtk3", "QupZilla",
        "Uget-gtk", "Tor Browser", "Waterfox",
    ], role=["browser"]), ],

    [Match(wm_class=[
        "Zathura", "libreoffice-writer", "libreoffice",
        "Leafpad", "kate", "Pluma", "Mousepad", "kwrite",
        "Geany", "Gedit", "Code", "Atom",
        "jetbrains-pycharm-ce",
    ]), ],

    [Match(wm_class=[
        "UXTerm", "Termite", "Terminator",
        "URxvt",
        "XTerm", "mlterm", "Lxterminal",
    ]), ],

    [Match(wm_class=[
        "discord",
    ]), ],

    [Match(wm_class=[
        "Gimp", "Gthumb", "org.kde.gwenview",
        "Ristretto", "lximage-qt", "Eom",
        "Gpicview",
    ], role=["gimp-image-window"]), ],

    None,

    [Match(wm_class=[
        "VirtualBox", "okular", "calibre",
        "octopi", "Pamac-updater",
        "Pamac-manager", "Lxtask",
        "Dukto", "QuiteRss",
        "Filezilla",
    ]), ],

    [Match(wm_class=[
        "Pcmanfm", "Thunar", "thunar", "dolphin",
        "Caja", "Catfish",
    ], role=["filemanager"]), ],

    [Match(wm_class=[
        "vlc", "xv/mplayer", "Clementine",
        "MPlayer", "smplayer", "mpv",
        "Gnome-mpv", "Rhythmbox", "Pragha",
    ]), ],

    [Match(wm_class=[
        "Steam", "Wine", "Zenity",
        "PlayOnLinux",
    ]), ],

]


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

    @hook.subscribe.client_managed
    def go_to_group(window):
        if (window.window.get_wm_class()[1] in cls_grp_dict.keys()
                or window.window.get_wm_window_role() in role_grp_dict.keys()):
            window.group.cmd_toscreen()



keys = [
           Key([], 'F11', lazy.group['s'].dropdown_toggle('term')),
     Key([], 'F12', lazy.group['s'].dropdown_toggle('qshell')),

            
            Key(
                [mod], "Up",
                lazy.window.up_opacity()),


            Key(
                [mod], "Return", 
                lazy.spawn("urxvt")                        # Open terminal
                ),
            Key(
                [mod], "Tab", 
                lazy.next_layout()                        # Toggle through layouts
                ),
            Key(
                [mod], "q", 
                lazy.window.kill()                        # Kill active window
                ),
            Key(
                [mod, "shift"], "r", 
                lazy.restart()                            # Restart Qtile
                ),
            Key(
                [mod, "shift"], "q", 
                lazy.shutdown()                           # Oblogout
                ),
            Key([mod], "i",
                lazy.to_screen(0)                         # Keyboard focus screen(0)
                ),
            Key([mod], "o",
                lazy.to_screen(1)                         # Keyboard focus screen(1)
                ),
            Key([mod], "p",
                lazy.to_screen(2)                         # Keyboard focus screen(2)
                ),
            # Window controls
            Key(
                [mod], "k", 
                lazy.layout.down()                        # Switch between windows in current stack pane
                ),
            Key(
                [mod], "j", 
                lazy.layout.up()                          # Switch between windows in current stack pane
                ),
            Key(
                [mod, "shift"], "k", 
                lazy.layout.shuffle_down()                # Move windows down in current stack
                ),
            Key(
                [mod, "shift"], "j", 
                lazy.layout.shuffle_up()                  # Move windows up in current stack
                ),
            Key(
                [mod, "shift"], "l", 
                lazy.layout.grow(),                       # Grow size of current window (XmonadTall)
                lazy.layout.increase_nmaster(),           # Increase number in master pane (Tile)
                ),
            Key(
                [mod, "shift"], "h", 
                lazy.layout.shrink(),                     # Shrink size of current window (XmonadTall)
                lazy.layout.decrease_nmaster(),           # Decrease number in master pane (Tile)
                ),
             Key(
                [mod], "Left", 
                lazy.screen.prev_group()
                ),
            Key([mod], "Right", 
                lazy.screen.next_group()
                ),
             Key(
                [mod, "shift"], "Left",                   # Move window to workspace to the left
                window_to_prev_group
                ),
            Key(
                [mod, "shift"], "Right",                  # Move window to workspace to the right
                window_to_next_group
                ),
            Key(
                [mod], "n", 
                lazy.layout.normalize(),                   # Restore all windows to default size ratios 
                ),
            Key(
                [mod], "m", 
                lazy.layout.maximize()                    # Toggle a window between minimum and maximum sizes
                ),
                
            Key(
                [mod, "shift"], "KP_Enter", 
                lazy.window.toggle_floating()             # Toggle floating
                ),
            Key(
                [mod, "shift"], "space", 
                lazy.layout.rotate(),                     # Swap panes of split stack (Stack)
                lazy.layout.flip()                        # Switch which side main pane occupies (XmonadTall)
                ),
            # Stack controls
            Key(
                [mod], "space", 
                lazy.layout.next()                        # Switch window focus to other pane(s) of stack
                ),
            Key(
                [mod, "control"], "Return", 
                lazy.layout.toggle_split()                # Toggle between split and unsplit sides of stack
                ),
            # GUI Apps
            Key(
                [mod], "w", lazy.spawn(myBrowser)),   # , Match(title=["Chromium"])
            Key(
                [mod], "Print", 
                lazy.spawn("spectacle")
                ),    
            Key(
                [mod], "c", 
                lazy.spawn("discord")),
            Key(
                [mod], "t", 
                lazy.spawn("spotify")
                ),
            Key(
                [mod], "f", 
                lazy.spawn("thunar")
                ),
            Key(
                [mod], "F1", 
                lazy.spawn("pamac-manager")
                ),
            Key(
                [mod], "g", 
                lazy.spawn("subl3",)),
            # Terminal Apps
            Key(
                [mod], "d", lazy.spawn("rofi -show run"), desc=("[Run Rofi]")),
            Key(
                [mod], "x",                                 
                lazy.spawn('oblogout')),
            Key(
                [mod], "KP_End",                                     # Keypad 1
                lazy.spawn("urxvt -e ranger")),
            Key(
                [mod], "KP_Down",                                    # Keypad 2
                lazy.spawn("urxvt -e htop")
                ),
            Key(
                [mod], "KP_Page_Down",                               # Keypad 3
                lazy.spawn("urxvt -e irssi") 
                ), 
            Key(
                [mod], "KP_Left",                                    # Keypad 4
                lazy.spawn("urxvt -e lynx http://www.omgubuntu.co.uk")
                ),
            Key(
                [mod], "KP_Begin",                                   # Keypad 5
                lazy.spawn("urxvt -e mutt")
                ), 
            Key(
                [mod], "KP_Right",                                   # Keypad 6
                lazy.spawn("urxvt -e canto-curses")
                ),
            Key(
                [mod], "KP_Home",                                    # Keypad 7
                lazy.spawn("urxvt -e alsamixer")
                ),
            Key(
                [mod], "KP_Up",                                      # Keypad 8
                lazy.spawn("urxvt -e ncmpcpp")
                ),
            Key(
                [mod], "KP_Page_Up",                                 # Keypad 9
                lazy.spawn("urxvt -e mpsyt")
                ),
            ]


groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = ["", "", "", "", "", "", "", "", "", "",]

group_layouts = ["monadtall", "monadtall", "bsp", "max", "max", "max", "max", "max", "max", 
"max",]


for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            matches=group_matches[i],
            exclusive=group_exclusives[i],
            layout=group_layouts[i].lower(),
            persist=group_persists[i],
            init=group_inits[i],
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])



#my_group = ["", "", "", "", "", "", "",]

# group layout

#for i in my_group:
#    if i == "":
#        groups.append(Group(i, layout = "monadtall"))
#    elif i == "":
#        groups.append(Group(i, layout = "monadtall"))
#    elif i == "":
#        groups.append(Group(i, layout = "bsp"))
#    else:
#        groups.append(Group(i, layout = "max"))

#groups.append(ScratchPad("s", [
#        # define a drop down terminal.
#        # it is placed in the upper third of screen by default.
#        DropDown("term", "urxvt", opacity=0.8),

        # define another terminal exclusively for qshell at different position
#        DropDown("qshell", "urxvt -hold -e qshell",
#                 x=0.05, y=0.4, width=0.9, height=0.6, opacity=0.9,
#                 on_focus_lost_hide=True)
#        
#         ])), 

# Add numeric key Group
#for c, name in enumerate(my_group, 1):
#    keys.append(
#            Key([mod], str(c), lazy.group[name].toscreen())
#            )
#    keys.append(
#            Key([mod, "shift"], str(c), lazy.window.togroup(name))
#            )



def init_layout_theme():
    return {"border_width": 3,
            "margin": 3,
            "border_focus": "#800000",
            "border_normal": "#50EDCE"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2, **layout_theme)
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

  

def init_screens():
    return [Screen(bottom=bar.Gap(size=35),
                   top=bar.Gap(size=35))
            ]
            #Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=35)), 
            #Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=35))]
screens = init_screens()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': "Openbox Logout"},
    {'wname': 'branchdialog'},      # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = "qtile"