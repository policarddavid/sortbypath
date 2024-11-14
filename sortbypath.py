import csv
from collections import Counter

file_path = "./example.csv"


def read_csv_as_list_of_rows(file_path):
    with open(file_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
    return rows


# Example usage
rows = read_csv_as_list_of_rows(file_path)

# Count the frequency of each path
path_counts = Counter(row[2] for row in rows)

# Sort the filtered rows by frequency first, then by path, then by the second column
sorted_rows = sorted(rows, key=lambda row: (path_counts[row[2]], row[2], row[1]))

# Prepare a list for rows with empty lines inserted between different groups
rows_with_empty_lines = []

# Track the previous group keys
previous_path = None
previous_category = None

for row in sorted_rows:
    current_path = row[2]
    current_category = row[1]

    # Check for group change. Add an empty line for a new group based on the path or category
    if previous_path is not None:
        if current_path != previous_path:
            # Major group change based on path
            rows_with_empty_lines.append([])  # Insert empty row for new path group
        elif current_category != previous_category:
            # Sub-group change within the same path
            rows_with_empty_lines.append([])  # Insert empty row for new category group

    # Add the current row to the list
    rows_with_empty_lines.append(row)

    # Update the previous keys
    previous_path = current_path
    previous_category = current_category

# Write sorted rows with empty lines to a new CSV file
output_file_path = "./sorted_example_with_grouped_empty_rows.csv"

# Sort the rows_with_empty_lines based on the size of each group
grouped_rows = []
current_group = []
current_path = None

for row in rows_with_empty_lines:
	if not row:
		if current_group:
			grouped_rows.append(current_group)
			current_group = []
		grouped_rows.append([])
	else:
		if current_path is None:
			current_path = row[2]
		elif row[2] != current_path:
			grouped_rows.append(current_group)
			current_group = []
			current_path = row[2]
		current_group.append(row)

if current_group:
	grouped_rows.append(current_group)

# Sort groups by size (ascending) and flatten the list
sorted_grouped_rows = sorted(grouped_rows, key=lambda group: len(group) if group else float('inf'))
rows_with_empty_lines = [row for group in sorted_grouped_rows for row in (group + [[]] if group else [])]
with open(output_file_path, mode="w", newline="") as file:
	writer = csv.writer(file)
	writer.writerows(rows_with_empty_lines)