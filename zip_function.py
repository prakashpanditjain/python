string = 'BANANA'
stuart = 0
kevin = 0
vowels = ['A','E','I','O','U']
for i in range(len(string)):
    if string[i] in vowels:
        kevin += len(string) - i
    else:
        stuart += len(string) - i

if(kevin<stuart):
    print('Stuart',stuart)
else:
    print('Kevin',kevin)