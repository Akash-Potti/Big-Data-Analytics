import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) != 3:
        continue
    a, b, val = parts

    if a.startswith('U'):
        # User-Item-Rating
        print("%s\tR\t%s\t%s" % (b, a, val))  # key=item
    elif a.startswith('I'):
        # Item-Feature-Value
        print("%s\tF\t%s\t%s" % (a, b, val))  # key=item
