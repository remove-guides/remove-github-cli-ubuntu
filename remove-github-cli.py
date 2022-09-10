#!/bin/python3

import os
import sys

USER = os.environ.get("SUDO_USER")
HOME = f'/home/{USER}'
RED = "\033[31m"


def remove_from_packages():
    try:
        os.system('apt-get purge gh -y')
        os.system('apt autoremove -y')

        os.system('brew uninstall gh')
    except:
        print(f"\n{RED} Failed on remove packages! \n")


def remove_files():
    try:
        os.system('rm -rf /etc/apt/sources.list.d/github-cli.list')
        os.system(f'rm -rf {HOME}/.config/gh')

    except:
        print(f"\n{RED} Failed on remove files! \n")


def main():
    remove_from_packages()
    remove_files()


if __name__ == '__main__':
    user_type = os.getuid()

    if(user_type != 0):
        print(f"\n{RED} Please Run as Root! \n")
        sys.exit(1)

    main()
