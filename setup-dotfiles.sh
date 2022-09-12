#!/usr/bin/env sh

mkdir "$HOME/dotfiles"

git clone --bare git@github.com:touhidulshawan/dotfiles.git "$HOME/dotfiles"

echo alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME' >>"$HOME/.bashrc"

source "$HOME/.bashrc"

config checkout
config config status.showUntrackedFiles no
