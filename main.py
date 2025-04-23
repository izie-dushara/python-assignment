# read file
def read_csv(filename):
	results = []
	with open(filename, 'r') as f:
		next(f) # skip header
		for line in f:
			words = line.strip().split(',')
			results.append(words)
	return results

# insert new row
def insert_row(filename, values):
	with open(filename, "a") as f:
		f.write(f"\n{','.join(str(val) for val in values)}")

# update file
def update_csv(filename, updated_data, headers):
	with open(filename, "w") as f:
		# write headers
		f.write(','.join(headers))

		for row in updated_data:
			f.write(f"\n{','.join(str(val) for val in row)}")

# delete row
def delete_row(filename, condition_func):
	# read all content
	with open(filename, "r") as f:
		lines = f.readlines()
		header = lines[0]

	# write back filtered content
	with open(filename, "w") as f:
		f.write(header)
		for line in lines[1:]:
			row = line.strip().split(',')
			if not condition_func(row):
				f.write(line)

if __name__ == "__main__":
	filename = 't.csv'

	# Read
	results = read_csv(filename)
	print(f"Read results: {results}")

	# Insert
	insert_row(filename, [3, "Joshua", "California"])
	results = read_csv(filename)
	print(f"Row inserted: {results}")

	# Update
	results = read_csv(filename)
	if results:
		results[0][1] = "Kaja"
	update_csv(filename, results, ["SN", "Name", "City"])
	print(f"File update: {results}")

	# Delete
	delete_row(filename, lambda row: row[0] == '3')
	results = read_csv(filename)
	print(f"Row deleted: {results}")