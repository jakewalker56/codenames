import codenames
import sys

if len(sys.argv) is not 3:
    print(sys.argv)
    print("usage: decode_clue.py word number")
    exit()
else:
    word = sys.argv[1]
    n = sys.argv[2]

codenames.init()
decoded_clue = codenames.decode_clue(word, n)
print(decoded_clue)
