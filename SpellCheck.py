import time
import re

#Keeping track of time
t0 = time.time()

#Open the files
dfile = open('./DICTIONARIES/Large Dictionary.txt', 'r')
tfile = open('./TEXTS/bible.txt', 'r')

#Set Up Dictionary
d = dfile.read()
dictionary = d.split("\n")

#Set Up Text
t = tfile.read()
pattern = re.compile(r"[a-zA-Z]+('s)?") # re.I)
ourmatches = pattern.finditer(t)

#Closing Out the Files
dfile.close()
tfile.close()


#Creating the Trie Node
class TrieNode:
  def __init__(self, letter):
    self.letter = letter
    self.children = {}
    self.is_end_of_word = False

#Creating the Trie Logic
class Trie:
  def __init__(self):
    self.root = TrieNode("*")

  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        curr_node.children[letter] = TrieNode(letter)
      curr_node = curr_node.children[letter]
    curr_node.is_end_of_word = True

  def does_word_exist(self, word):
    if word == "":
      return True
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        return False
      curr_node = curr_node.children[letter]
    return curr_node.is_end_of_word


"""
class Trie:
  def __init__(self):
    self.root = {"*":"*"}

  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        curr_node[letter] = {}
      curr_node = curr_node[letter]
    curr_node["*"] = "*"

  def does_word_exist(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        return False
      curr_node = curr_node[letter]
    return "*" in curr_node
"""

#Running Trie
trie = Trie()
count = 0
for word in dictionary:
    count +=1
    trie.add_word(word)

# Running the Trie
mispelledwords = 0
analyzedwords = 0
for match in ourmatches:
    analyzedwords += 1
    string = match[0]
    string = string.lower()
    if not trie.does_word_exist(string):
        mispelledwords += 1
        # print (match[0])

print ()
print ("Total Analyzed Words:", analyzedwords)
print ("MisspelledWords:", mispelledwords)
print ()

#Keeping Track of Time
t1 = time.time()
total = t1-t0
print(total)
