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

