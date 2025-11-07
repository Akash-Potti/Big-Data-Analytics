import sys
import csv

movies={}

with open("movies.csv","r") as f:
	reader=csv.reader(f)
	next(reader)
	for row in reader:
		movies[row[0]]=row[1]

	current_movie=None
	tags=[]

	for line in sys.stdin:
		line=line.strip()
		if not line:
			continue
		movieId,tag=line.split("\t",1)
		if current_movie==movieId:
			tags.append(tag)

		else:
			if current_movie:
				title=movies.get(current_movie,current_movie)
				print "%s\t%s"%(title,",".join(tags))
			current_movie=movieId
			tags=[tag]


	if current_movie:
		title=movies.get(current_movie,current_movie)
		print "%s\t%s"% (title, ",".join(tags))
