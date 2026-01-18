import itertools
import os
import platform

# Configuration
chars = 'BCDFGHJKMPQRTVWXYZ2346789'
prefix = "qthxk-rykm9-jtgwq-9"
suffix = "p-9j47z"

# Generate combinations with the extra text
results = [f"{prefix}{''.join(p)}{suffix}" for p in itertools.product(chars, repeat=3)]

# Save to Desktop for easy access
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop, "combinations_final.txt")

with open(file_path, 'w') as f:
    f.write('\n'.join(results))

print(f"Done! Created {len(results)} combinations.")
print(f"File saved to: {file_path}")

# This part tries to open the folder automatically
if platform.system() == "Windows":
    os.startfile(desktop)
elif platform.system() == "Darwin": # macOS
    import subprocess
    subprocess.Popen(["open", desktop])