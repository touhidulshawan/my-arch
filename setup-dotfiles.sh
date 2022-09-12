#!/usr/bin/env sh

mkdir $HOMR/dotfiles

git clone --bare git@github.com:touhidulshawan/dotfiles.git $HOME/dotfiles

echo alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME' >>$HOME/.bashrc

source ~/.bashrc

config checkout
config config status.showUntrackedFiles no
