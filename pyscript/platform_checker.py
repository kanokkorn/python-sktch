import sys

if sys.platform == "win32":
    print("you are using windows")
elif sys.platform == "linux":
    print("you are using Linux")
elif sys.platform == "darwin":
    print("you are using MacOS")
