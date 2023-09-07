#!/usr/bin/python3
import sys
if __name__ == "__main__":
    cmds = len(sys.argv) - 1
    if cmds == 0:
        print("0 arguments.")
    elif cmds == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cmds))
    for i, cmd in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, cmd))
