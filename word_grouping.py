'''takes a list of words as input. The function should return a dictionary where
the keys are the word lengths, and the values are
lists containing all the words of that length'''
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
words = literal_eval(input())

def group_words_by_length(words):
   # Write your code here
  new_dict={}
  for i in range(len(words)):
    length=len(words[i])
    if length in new_dict:
      new_dict[length].append(words[i])
      continue
    new_dict[length]=[words[i]]
  return new_dict


# Print the output
print(group_words_by_length(words))
