#!/usr/bin/python3
import sys
if __name__ == "__main__":
    tot = 0
    cmds = sys.argv[1:]
    for x in cmds:
        tot += int(x)
    print("{}".format(tot))
