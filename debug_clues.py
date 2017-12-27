import codenames
import sys
print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)

print("generating clue...")
clue = generate_clue("blue")
print("clue:")
print(clue)
print("decoding clue...")
decoded_clue = decode_clue(clue[0][0], clue[1])
print(decoded_clue)
print("blue words:")
print(team_words("blue"))
print("mismatch:") 
print(list(set([i[0] for i in decoded_clue]) - set(team_words("blue"))))
print("unfulfilled:") 
print(list(set(team_words("blue")) - set([i[0] for i in decoded_clue])))

