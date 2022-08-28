#!/usr/bin/env python3

import os
import sys


config_dir = "/home/shawan/.config"

# install yay


def install_yay():
    try:
        os.system("sudo pacman -S --needed git base-devel")
        print("[+] installing yay...")
        os.system("git clone https://aur.archlinux.org/yay.git")
        os.system("mv ./yay/PKGBUILD ./")
        os.system("makepkg -si")
    except Exception:
        print(sys.exc_info())


# install apps


def install_apps():
    try:
        apps_data = open("./packages-list.txt", "r")

        for app in apps_data:
            print(f"[+] installing {app}")
            os.system(f"yay -S {app} ")
        apps_data.close()
    except Exception:
        print(sys.exc_info())


# config github-cli


def config_gh():
    try:
        print("Configuration of github-cli")
        os.system("gh auth login")
    except Exception:
        print(sys.exc_info())


# change default shell
def default_shell():
    print("[+] changing default shell")
    os.system("chsh -s /usr/bin/fish")


# setup my fish shell


def setup_fish():
    try:
        os.system("fish")
        os.chdir(config_dir)
        os.system("gh repo clone fish")
        os.chdir(f"{config_dir}/fish")
        os.system("./install_plugins.fish")
        default_shell()
        os.system("su root")
        default_shell()
    except Exception:
        print(sys.exc_info())


# clone my dotfiles from my github repositories


def clone_dotfiles():
    repo_names = open("./repository-names.txt", "r")
    try:
        os.chdir(config_dir)
        for repo in repo_names:
            print(f"Cloning {repo} from touhidulshawan/{repo}")
            os.system(f"gh repo clone {repo}")
    except Exception:
        print(sys.exc_info())


install_yay()
install_apps()
config_gh()
setup_fish()
clone_dotfiles()
