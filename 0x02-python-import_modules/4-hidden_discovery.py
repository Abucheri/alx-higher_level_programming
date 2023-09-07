#!/usr/bin/python3
import dis
if __name__ == "__main__":
    import hidden_4
    for n in dir(hidden_4):
        if not n.startswith("__"):
            print("{}".format(n))
