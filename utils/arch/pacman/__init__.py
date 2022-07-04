import string
import os

def install(PACKAGE: string):
    os.system(f"pacman -S --noconfirm {PACKAGE}")

def systemupdate():
    os.system(f"pacman -Syu")