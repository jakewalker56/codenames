import codenames
import sys
if len(sys.argv) is not 2:
    print(sys.argv)
    print("usage: generate_clue.py team_name")
    exit()

codenames.init()
clue = codenames.generate_clue(sys.argv[1])
print(str(clue[0][0]) + " " + str(clue[1]))
