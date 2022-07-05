import os
import string
# import sys

def clone(LINK: string):
    os.system("echo '-----------------------------------------'")
    os.system(f"echo 'Cloning from {LINK}'")
    os.system("echo '-----------------------------------------'")
    os.system(f"git clone {LINK}")