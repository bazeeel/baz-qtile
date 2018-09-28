export POWERLEVEL9K_INSTALLATION_PATH=$HOME/.antigen/repos/https-COLON--SLASH--SLASH-github.com-SLASH-bhilburn-SLASH-powerlevel9k.git

#ZSH_THEME="powerlevel9k/powerlevel9k"

#zstyle ':prezto:module:prompt' theme 'powerlevel9k'

source ~/.antigen.zsh
export POWERLEVEL9K_INSTALLATION_PATH=$ANTIGEN_BUNDLES/bhilburn/powerlevel9k

antigen use oh-my-zsh

antigen theme bhilburn/powerlevel9k powerlevel9k
antigen bundle git
antigen bundle heroku
antigen bundle pip
antigen bundle lein
antigen bundle command-not-found

antigen apply

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status os_icon  root_indicator
background_jobs history time)


#zplug "bhilburn/powerlevel9k", use:powerlevel9k.zsh-theme
neofetch




# Aliases for software managment
# pacman or pm
alias pmsyu="sudo pacman -Syu --color=auto"
alias pacman='sudo pacman --color auto'
alias update='sudo pacman -Syu'
alias remove='sudo pacman -R'
# pacaur or pc
alias pcsyu="pacaur -Syu"

#ps
alias ps="ps auxf"
alias psgrep="ps aux | grep -v grep | grep -i -e VSZ -e"
alias skel='cp -rf /etc/skel/* ~'

# yay keeps tmp folder cleaner than packer
alias install="yay -S --noconfirm "
alias pksyu="yay -Syu --noconfirm"
alias pksyua="yay -Syyu  --aur --noconfirm"

#grub update
alias update-grub="sudo grub-mkconfig -o /boot/grub/grub.cfg"

#improve png
#alias fixpng="find . -type f -name "*.png" -exec convert {} -strip {} \;"

#add new fonts
alias fc='sudo fc-cache -fv'

#get fastest mirrors in your neighborhood 
alias mirror="sudo reflector --protocol https --latest 50 --number 20 --sort rate --save /etc/pacman.d/mirrorlist"
alias mirrors=mirror
