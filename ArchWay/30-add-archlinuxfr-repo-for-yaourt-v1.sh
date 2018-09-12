#!/bin/bash
#set -e
##################################################################################################################
# Author	:	Erik Dubois
# Website	:	https://www.erikdubois.be
# Website	:	https://www.arcolinux.info
# Website	:	https://www.arcolinux.com
# Website	:	https://www.arcolinuxd.com
# Website	:	https://www.arcolinuxforum.com
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################


echo '

[archlinuxfr]
SigLevel = Never
Server = http://repo.archlinux.fr/$arch' | sudo tee --append /etc/pacman.conf

echo "################################################################"
echo "###                 archlinuxfr repo added                  ####"
echo "################################################################"
