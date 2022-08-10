import os

def install(PACKAGE: string):
    os.system(f"yay -S --noconfirm {PACKAGE}")

def systemupdate():
    os.system(f"yay --noconfirm -Syu")