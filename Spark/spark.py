from pyspark import SparkContext
from pyspark.sql import SQLContext,Row
from pyspark.sql.functions import count


sc=SparkContext()
sqlContext=SQLContext(sc)

rdd=sc.textFile("file:///home/cloudera/posts.txt")

cleaned_rdd=rdd.map(lambda line: ''.join(ch.lower() if ch.isalnum() or ch.isspace() else ' '  for ch in line))

words_rdd=cleaned_rdd.flatMap(lambda line: line.split())

stopwords=set([
"the","is","and","to","of","in","a","for","on","with","this","that","it","as","at","be","by","an","are","from","or","was","were","has","have","had","not","but","so","if"
])

filtered_rdd=words_rdd.filter(lambda w: w not in stopwords and w!="")

row_rdd=filtered_rdd.map(lambda w:Row(word=w))

df=sqlContext.createDataFrame(row_rdd)

df=df.groupBy("word").count()

df=df.sort(df['count'].desc())

top_n=10

results=df.take(top_n)

print("Result")
for w,c in results:
	print "%s\t%d" % (w,c)


