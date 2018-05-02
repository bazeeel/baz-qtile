#!/bin/sh
feh --bg-scale ~/Képek/1.jpeg &
nm-applet &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#pasystray &
compton --config  ~/.config/qtile/compton.conf &
