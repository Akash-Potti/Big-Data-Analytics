import sys

current_item = None
user_ratings = []
feat_values = []

def flush():
    for u, r in user_ratings:
        for f, v in feat_values:
            print("%s\t%s\t%f" % (u, f, float(r) * float(v)))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 4:
        continue
    item, tag, x, y = parts
    if current_item is not None and item != current_item:
        flush()
        user_ratings, feat_values = [], []
    current_item = item
    if tag == 'R':
        user_ratings.append((x, y))
    elif tag == 'F':
        feat_values.append((x, y))

if current_item is not None:
    flush()
