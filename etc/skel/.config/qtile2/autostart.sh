#!/bin/sh
feh --bg-scale ~/.config/qtile/Infra-Embedded-Chaos-Unrest-1920x1080-HD.jpg 
#nm-applet &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#pasystray &
compton --config  ~/.config/qtile/compton.conf &
~/.config/polybar/launch.sh &
