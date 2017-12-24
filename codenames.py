#solving Code Names with word2vec embeddings 

import gensim
import csv
import operator

#https://radimrehurek.com/gensim/models/keyedvectors.html
# Load Google's pre-trained Word2Vec model.  
# Download from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

word_vectors = None
word_layout = None
team_layout = None

def init():
  load_model('~/Downloads/GoogleNews-vectors-negative300.bin', 700000)
  load_word_layout("word_layout.csv")
  load_team_layout("team_layout.csv")

def load_model(name, size):
  global word_vectors
  model = gensim.models.KeyedVectors.load_word2vec_format(name, binary=True, limit=size)  
  word_vectors = model.wv
  #delete the model to avoid excessive memory usage
  del model

def load_word_layout(file):
  global word_layout
  word_layout = list(csv.reader(open(file), skipinitialspace=True)) 

def load_team_layout(file):
  global team_layout
  team_layout = list(csv.reader(open(file), skipinitialspace=True)) 

def team_words(team):
  result = list()
  for i in range(len(word_layout)):
    for j in range(len(word_layout[i])):
      if team_layout[i][j] == team:
        result.append(word_layout[i][j])
  return(filter(None, result))

def not_team_words(team):
  flat_word_list = get_flat_word_list()
  return filter(None, list(set(flat_word_list) - set(team_words(team))))

def get_flat_word_list():
  return filter(None, [item for sublist in word_layout for item in sublist])

def generate_clue(team, try_n = 1000):    
  clues = word_vectors.most_similar(positive=team_words(team), negative=not_team_words(team), topn=try_n)
  best_result = 0
  best_result_n = 0
  for clue_n in range(len(clues)):
    if len(clues[clue_n][0].split('_')) > 1:
      #if the clue is actually multiple words, skip it
      continue
    decoded_clue = decode_clue(clues[clue_n][0], len(team_words(team)))
    if decoded_clue is None:
      #not sure how this would happen...
      print("unexpected empty list:")
      print(clues[clue_n])
      continue
    for i in range(len(decoded_clue)):
      if decoded_clue[i] not in team_words(team):
        #the ith word is incorrect; only return i-1
        if (i) > best_result_n:
          # print("new best:")
          # print(clues[clue_n][0])
          # print(decoded_clue)
          # print(clue_n)
          # print(i)
          best_result = clue_n
          best_result_n = i
        break
  return([clues[best_result], best_result_n])

def decode_clue(word, n):
  n = int(n)
  flat_word_list = get_flat_word_list()
  word_distances = {}
  for test_word in flat_word_list:
      word_distances[test_word] = word_vectors.similarity(word, test_word)

  sorted_word_distances = sorted(word_distances.items(), key=operator.itemgetter(1))[::-1]
  return ([item[0] for item in sorted_word_distances][:n])

