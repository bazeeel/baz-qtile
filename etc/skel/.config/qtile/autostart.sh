#!/bin/sh
feh --bg-scale ~/.config/qtile/4.jpg &
nm-applet &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#pasystray &
compton --config  ~/.config/qtile/compton.conf &
~/.config/polybar/launch.sh $
