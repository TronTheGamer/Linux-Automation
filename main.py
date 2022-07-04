import os
import sys


if __name__ == "__main__":
    if (not os.path.isdir("TEMP")):
        os.system(""""echo "Creating TEMP directory: " """)
        os.mkdir("TEMP")

    
