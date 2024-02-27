lst = ['prakash',"pandit","pooja","mayuri","ranveer","baburao","ratan"]
print(lst)

def letter(lst):
    count = 0
    for name in lst:
        l = 0
        for letter in name:
            l+=1
        if l > 5:
            count +=1
        else:
            continue
    return count

result = letter(lst)
print(result)