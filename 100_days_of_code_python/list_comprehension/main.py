sentence = 'Hello prakash, I am raksha, I am here to help people, how can i help you?'

#create dictonary to count the letters in the word
new_list = {word:len(word) for word in [words for words in sentence.split(" ")]}
print(new_list)