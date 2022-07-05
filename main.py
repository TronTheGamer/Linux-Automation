import os
import utils.arch.pacman as pacman


if __name__ == "__main__":
    if (not os.path.isdir("TEMP")):
        os.system(""""echo "Creating TEMP directory: " """)
        os.mkdir("TEMP")
    os.system(r"""echo -e "\nInstalling yay\n" """)
    os.system("sudo /bin/bash scripts/yay-install.sh")
    

