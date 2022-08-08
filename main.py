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

    except Exception:
        cprint(txt=Exception, color="red")


install_yay()
install_apps()
