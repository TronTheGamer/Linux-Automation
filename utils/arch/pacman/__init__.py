import string
import os

def install(PACKAGE: string):
    """
    Installs Packages using PACMAN:
    -----------------------------------------
    PACKAGE: 
    Package name in repo as String
    -----------------------------------------
    """
    os.system(f"pacman -S --noconfirm {PACKAGE}")

def systemupdate():
    """
    Updates the system including all the non-AUR packages
    """
    os.system(f"pacman --noconfirm -Syu")