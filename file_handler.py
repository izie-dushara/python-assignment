class FileHandler:
# read file
	def read_csv(self, filename):
		results = []
		with open(filename, 'r') as f:
			next(f) # skip header
			for line in f:
				words = line.strip().split(',')
				results.append(words)
		return results

	# insert new row
	def insert_row(self, filename, values):
		with open(filename, "a") as f:
			f.write(f"\n{','.join(str(val) for val in values)}")

	# update file
	def update_csv(self, filename, updated_data, headers):
		with open(filename, "w") as f:
			# write headers
			f.write(','.join(headers))

			for row in updated_data:
				f.write(f"\n{','.join(str(val) for val in row)}")

	# delete row
	def delete_row(self, filename, condition_func):
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
					if line.endswith('\n'):
						f.write(line)
					else:	
						f.write(line)