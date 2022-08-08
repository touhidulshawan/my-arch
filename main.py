#!/usr/bin/env python3

import os
from collpy import cprint

# install yay


def install_yay():
    try:
        os.system("sudo pacman -S --needed git base-devel")
        cprint(txt="[+] installing yay...", color="green")
        os.system("git clone https://aur.archlinux.org/yay.git")
        os.system("mv ./yay/PKGBUILD ./")
        os.system("makepkg -si")
    except Exception:
        cprint(txt=Exception, color="red")


# install apps


def install_apps():
    try:
        apps_data = open("./packages-list.txt", "r")

        for app in apps_data:
            cprint(txt=f"[+] installing {app}", color="green")
            os.system(f"yay --noconfirm -S {app} ")
        apps_data.close()
    except Exception:
        cprint(txt=Exception, color="red")


# config github-cli


def config_gh():
    try:
        cprint(txt="Configuration of github-cli", color="orange")
        os.system("gh auth login")
    except Exception:
        cprint(txt=Exception, color="red")


# clone my dotfiles from my github repositories


def clone_dotfiles():
    repo_names = open("./repository-names.txt", "r")
    try:
        os.chdir("/home/shawan/.config")
        for repo in repo_names:
            cprint(txt=f"Cloning {repo} from touhidulshawan/{repo}", color="green")
            os.system(f"gh repo clone {repo}")
    except Exception:
        cprint(txt=Exception, color="red")


install_yay()
install_apps()
config_gh()
clone_dotfiles()
