_tuple = ('a', 'b', 'd', 'e')

# Thêm 'c' vào vị trí index = 2
new_tuple = _tuple[:2] + ('c',) + _tuple[2:]

print(new_tuple)