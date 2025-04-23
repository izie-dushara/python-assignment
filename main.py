from file_handler import FileHandler

if __name__ == "__main__":
	filename = 't.csv'
	
	file_handler = FileHandler()

	# Read
	results = file_handler.read_csv(filename)
	print(f"Read results: {results}")

	# Insert
	file_handler.insert_row(filename, [3, "Joshua", "California"])
	results = file_handler.read_csv(filename)
	print(f"Row inserted: {results}")

	# Update
	results = file_handler.read_csv(filename)
	if results:
		results[0][1] = "Kaja"
	file_handler.update_csv(filename, results, ["SN", "Name", "City"])
	print(f"File update: {results}")

	# Delete
	file_handler.delete_row(filename, lambda row: row[0] == '2')
	results = file_handler.read_csv(filename)
	print(f"Row deleted: {results}")