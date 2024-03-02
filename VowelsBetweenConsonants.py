import re
string = (re.findall(r'\w','This is prakasheee and i amiou trying to serch the vowels in between consonent'))
print(string)

vowel = ['a','e','i','o','u']
len1= len(string)
# print(len1)
for i in range(len1):
    # print(string[i-5])
    if string[i] in vowel and string[i-1] not in vowel:     #check if the char is in vowel
        for j in range(i+1,len1):
            if string[j] in vowel:
                continue
            else:
                break
        print(string[i:j])