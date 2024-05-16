models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print(sorted(models, key=lambda x: x['color']))
print(sorted(models, key=lambda x: x['make']))


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("even number of list: ", list(filter(lambda x: x%2  ==0, lst)))