import os
import string

def install(PACKAGE: string):
    """
    Installs Packages using yay - AUR helper:
    -----------------------------------------
    PACKAGE: 
    Package name in AUR as String
    -----------------------------------------
    """
    os.system(f"yay -S --noconfirm {PACKAGE}")

def systemupdate():
    """
    Updates the system including all the packages
    """
    os.system(f"yay --noconfirm -Syu")