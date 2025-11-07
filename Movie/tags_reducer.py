import sys
import csv

# Load movie titles into dictionary
movies = {}
with open("movies.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        movies[row[0]] = row[1]  # movieId -> title

current_movie = None
tags = []

# Process tags from mapper
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        movieId, tag = line.split("\t", 1)
    except ValueError:
        continue

    if current_movie == movieId:
        tags.append(tag)
    else:
        if current_movie:
            title = movies.get(current_movie, current_movie)
            print("%s\t%s" % (title, ",".join(tags)))
        current_movie = movieId
        tags = [tag]

# Flush last movie
if current_movie:
    title = movies.get(current_movie, current_movie)
    print("%s\t%s" % (title, ",".join(tags)))
