from pandas.io.common import dedup_names
# from sqlalchemy import distinct

_list = [1,2,3,4,5,5]

# remove duplicates
deduped_list = list(set(_list))
print(deduped_list)

if len(deduped_list) != len(_list):
    print("Duplicates found and removed")

# reverse a list
# print(_list.reverse())

print(_list[::-1])



print(([n for n in _list if n % 2 == 0]).count())