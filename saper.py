import sys

if not (sys.version_info.major == 3 and sys.version_info.minor >= 5):
    print("This script requires Python 3.5 or higher!")
print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
