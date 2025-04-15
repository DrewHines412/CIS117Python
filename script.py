# CIS-117 Lab 4
# The module reads data from a CSV file, returning each row as a list of strings
# The writer writes data to a csv file in rows as lists of values
# DictReader reads data and maps each row to a dictionary
# the writer writes data to the csv file
#
# Version control is added to this project to track the changes and updates.
# This enables easier collaboration and management of the code.

import csv

try:
    with open("country_full.csv", 'r') as f:
        reader = csv.DictReader(f)
        regions = {}

        for row in reader:
            country = row.get("name")
            region = row.get("region")

            if not country or not region:
                continue  # Skip incomplete rows

            if region not in regions:
                regions[region] = []

            regions[region].append([country, region])

    # Write each region’s data to a new file
    for region, rows in regions.items():
        filename = f"{region}.csv"
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Country", "Region"])
                writer.writerows(rows)
            print(f"Saved {filename}")
        except Exception as e:
            print(f"Error saving {filename}: {e}")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error: {e}")

