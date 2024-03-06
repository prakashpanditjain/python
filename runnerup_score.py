incr = 0
str = ''
k=1
string = 'AABCsdfasdakjglksadfiasidufbausdfibasidbfiweiubfuabsdbfiaeifgwiefk͟hḥkhkhkbhbuibiuuvuugigi'
for i in range(len(string)):
    incr += 1
    if string[i] not in str:
        str += string[i]
    if incr == k or i == len(string) -1:
        incr = 0
        print(str,i)
        str = ''
# print(len(string))