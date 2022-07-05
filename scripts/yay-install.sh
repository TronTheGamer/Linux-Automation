#!/bin/bash
pacman -S base-devel
pacman -S git
cd TEMP
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si