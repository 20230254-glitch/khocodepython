_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

new_tuple = ()

for item in _tuple:
    if item not in new_tuple:
        new_tuple += (item,)

print(new_tuple)