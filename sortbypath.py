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


# Write sorted rows to a new CSV file
output_file_path = './sorted_example.csv'
with open(output_file_path, mode='w', newline='') as file:
	writer = csv.writer(file)
	writer.writerows(sorted_rows)