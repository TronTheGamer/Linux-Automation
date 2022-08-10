import os
import utils.arch.pacman as pacman
import utils.arch.yay as yay

if __name__ == "__main__":
    if (not os.path.isdir("TEMP")):
        os.system(""""echo "Creating TEMP directory: " """)
        os.mkdir("TEMP")
    os.system(r"""echo -e "\nInstalling yay\n" """)
    os.system("sudo /bin/bash scripts/yay-install.sh")
    
    os.system(r"""echo -e "\nUpdating System\n" """)
    yay.systemupdate()

    os.system(r"""echo -e "\nInstalling Packages From Applist:\n" """)
    with open('applist.txt','r') as applist:
        for PACKAGE in applist:
            yay.install(PACKAGE=PACKAGE)
