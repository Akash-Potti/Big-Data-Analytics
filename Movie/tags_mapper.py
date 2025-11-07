import sys

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("userId"):
        continue
    try:
        fields = line.split(",")
        movieId = fields[1].strip()
        tag = fields[2].strip()
        print("%s\t%s" % (movieId, tag))
    except Exception:
        continue
