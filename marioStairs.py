from sys import argv

size = int(argv[1]) if len(argv) >= 2 else 0

def mario(size):
    if (size == 0):
        print("Please call this file as: 'python marioStairs.py (desired size)'")
        return
    for i in range(1, size + 1):
        cur = "*" * i
        print(cur)

mario(size)