# codenames
solving the "Code Names" party game using word2vec embeddings

# Usage

1. Download and extract the word2vec dictionary file from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
2. edit 'word_layout.csv' and 'team_layout.csv' to match your game
3. run 'python generate_clue.py blue' to generate a CLUE and NUMBER for the blue side
4. run 'python decode_clue.py CLUE NUMBER' to find the list of words associated with the clue
5. delete any covered words from word_layout.csv and their associated entries team_layout.csv
6. return to step 3
