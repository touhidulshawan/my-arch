#!/usr/bin/env python3

import os

# install yay


def install_yay():
    try:
        os.system("sudo pacman -S --needed git base-devel")
        print("[+] installing yay...")
        os.system("git clone https://aur.archlinux.org/yay.git")
        os.system("mv ./yay/PKGBUILD ./")
        os.system("makepkg -si")
    except Exception:
        print(Exception)


# install apps


def install_apps():
    try:
        apps_data = open("./packages-list.txt", "r")

        for app in apps_data:
            print("[+] installing {app}")
            os.system(f"yay --noconfirm -S {app} ")
        apps_data.close()
    except Exception:
        print(Exception)


# config github-cli


def config_gh():
    try:
        print("Configuration of github-cli")
        os.system("gh auth login")
    except Exception:
        print(Exception)


# clone my dotfiles from my github repositories


def clone_dotfiles():
    repo_names = open("./repository-names.txt", "r")
    try:
        os.chdir("/home/shawan/.config")
        for repo in repo_names:
            print(f"Cloning {repo} from touhidulshawan/{repo}")
            os.system(f"gh repo clone {repo}")
    except Exception:
        print(Exception)


install_yay()
install_apps()
config_gh()
clone_dotfiles()
