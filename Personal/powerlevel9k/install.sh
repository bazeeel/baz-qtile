#!/usr/bin/env bash

set -e

# Install zsh

sudo pacman -S zsh

# oh-my-zsh install

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Powerlevel9k

git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

# Copy

cp .zshrc ~
sudo cp HackRegularNerdFontComplete.ttf /usr/share/fonts/TTF/
cp icons.zsh ~/.oh-my-zsh1/custom/themes/powerlevel9k/functions/

# Refresh font cache

sudo fc-cache -fv

# Set terminal font Hack Nerd Font Regular
