#!/bin/sh


#LAUNCHERS

#xrandr --output DP2 --primary --mode 1920x1080 --rate 60.00 --output LVDS1 --off &
#xrandr --output LVDS1 --mode 1366x768 --output DP3 --mode 1920x1080 --right-of LVDS1
nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }" &


feh --randomize --bg-scale ~/.config/qtile/Képek/*
#nm-applet &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#pasystray &
#conky -c $HOME/.config/conky/4-cpu-ET-Arcolinux-Fofo-LUA.conkyrc &
compton --config  ~/.config/qtile/compton.conf &
~/.config/polybar/launch.sh &
plank &
