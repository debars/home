#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ -f ~/.alias ]] && . ~/.alias

#PS1='[\u@\h \W]\$ '
PS1='\[\033[01;32m\]\u@\h \[\033[01;34m\]\W \$ \[\033[00m\]'
#PS1='\[\033[01;32m\]\u@\h \[\033[01;33m\]\W \$ \[\033[00m\]'

# Change the window title of X terminals
case $TERM in
screen)
    PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/$HOME/~}\033\\"'
;;
esac

if [ -n "$DISPLAY" ]; then
	BROWSER=chromium
fi

set -o vi
