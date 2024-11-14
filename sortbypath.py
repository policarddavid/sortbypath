import csv
from collections import Counter

file_path = './example.csv'
def read_csv_as_list_of_rows(file_path):
	with open(file_path, mode='r', newline='') as file:
		reader = csv.reader(file)
		rows = list(reader)
	return rows

# Example usage
rows = read_csv_as_list_of_rows(file_path)
# Count the frequency of each path

path_counts = Counter(row[2] for row in rows)


# Sort the filtered rows by frequency first, then by path
sorted_rows = sorted(rows, key=lambda row: (path_counts[row[2]], row[2], row[1]))


# Print sorted rows for verification
for row in sorted_rows:
	print(row)