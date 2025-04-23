# read file
results = []
with open('t.csv', 'r') as f:
	next(f)
	for line in f:
		words = line.split(',')
		results.append(words)

# insert
newResults = []
csvFile = open("t.csv", "a")
newArray = []
newArray.append("\n3,")
newArray.append("Joshua,")
newArray.append("California")
csvFile.writelines(newArray)
csvFile.close()

# update file
updatedResults = []
with open('t.csv', 'r') as f:
	next(f)
	for line in f:
		words = line.split(',')
		updatedResults.append(words)

updatedResults[0][1] = "Kaja"

csvFile = open("t.csv", "w")
csvFile.writelines(['SN,','Name,','City\n'])
for result in updatedResults:
	updating = []
	updating.append(f"{result[0]},")
	updating.append(f"{result[1]},")
	updating.append(f"{result[2]}")
	print(updating)
	csvFile.writelines(updating)
csvFile.close()

# delete
with open("t.csv", "r") as f:
	lines = f.readlines()
	
	with open("t.csv", "w") as f:
		for line in lines:
			if line.find("3") == -1:
				f.write(line)
