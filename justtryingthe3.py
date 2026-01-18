import itertools
import os

# Your specific allowed characters
chars = 'BCDFGHJKMPQRTVWXYZ2346789'

# Generate the combinations
combinations = [''.join(p) for p in itertools.product(chars, repeat=3)]

# Define the filename and get the full path
filename = 'combinations_list.csv'
file_path = os.path.abspath(filename)

# Write the file
with open(filename, 'w') as f:
    f.write('Combination\n') # Header
    f.write('\n'.join(combinations))

print("--- SUCCESS ---")
print(f"Total combinations created: {len(combinations)}")
print(f"The file is saved at: {file_path}")
print("--- Check that folder on your computer! ---")