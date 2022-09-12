#!/usr/bin/env python3

import os
import sys

home_dir = os.path.expanduser("~")
config_dir = f"{home_dir}/.config"
print(config_dir)

# install yay


def install_yay():
    try:
        os.system("sudo pacman -S --needed git base-devel")
        print("[+] installing yay...")
        os.chdir(home_dir)
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


while True:
    print(
        """
    1. install yay
    2. install applications
    3. config github-cli
    4. exit the program
    """
    )

    user_choice = int(input("Enter choice: "))

    if user_choice == 1:
        install_yay()
    elif user_choice == 2:
        install_apps()
    elif user_choice == 3:
        config_gh()
    elif user_choice == 4:
        print("Exiting the program... bye!!")
        exit()
    else:
        print("Wrong choice!! Try again")
