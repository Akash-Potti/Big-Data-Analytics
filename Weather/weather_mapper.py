import sys

for line in sys.stdin:
	line=line.strip()

	if not line:
		continue
	date,temp=line.split(",")
	temp=int(temp)
	if temp>30:
		message="Hot Day"
	elif temp<10:
		message="cold day"
	else:
		message="pleasent day"
	print "%s\t%s"%(date,message)
