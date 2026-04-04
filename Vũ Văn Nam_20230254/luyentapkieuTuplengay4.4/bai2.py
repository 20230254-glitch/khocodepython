_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

new_tuple = ()

for item in _tuple:
    if _tuple.count(item) == 1:
        new_tuple += (item,)

print(new_tuple)