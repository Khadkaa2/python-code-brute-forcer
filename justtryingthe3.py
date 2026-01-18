import itertools
chars = 'BCDFGHJKMPQRTVWXYZ2346789'
combinations = [''.join(p) for p in itertools.product(chars, repeat=3)]
with open('my_list.csv', 'w') as f:
    f.write('\n'.join(combinations))