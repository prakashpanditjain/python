#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('../Mail Merge Project Start/Input/Names/invited_names.txt') as file:
    name_list = file.readlines()

# new_list =[]
for _ in name_list:
    # new_list.append(_.replace('\n',''))
    with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as file:
        starting_letter = file.read()
        name = _.strip()
        # print(name)
        new_text = starting_letter.replace('[name]', f'{name}')

    with open(f'../Mail Merge Project Start/Output/ReadyToSend/{_}.txt','w') as file:
        file.write(new_text)

# print(new_text)



