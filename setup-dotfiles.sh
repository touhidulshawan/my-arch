#!/usr/bin/env sh

mkdir "$HOME/dotfiles"

git clone --bare git@github.com:touhidulshawan/dotfiles.git "$HOME/dotfiles"

config() {
    /usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME $@
}

config checkout
config config status.showUntrackedFiles no
