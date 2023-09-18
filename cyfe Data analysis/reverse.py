import csv

def reverse_csv(input_file, output_file):
    # Read rows from the input CSV file
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            rows = list(reader)
    except UnicodeDecodeError:
        print("Failed to decode the file. Please check its encoding.")
        return

    # Reverse the rows (keeping the header in place if it exists)
    header, data_rows = rows[0], rows[1:]
    reversed_rows = [header] + data_rows[::-1]

    # Write reversed rows to the output CSV file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(reversed_rows)
    except UnicodeEncodeError:
        print("Failed to encode the reversed file. Please check its encoding.")
        return

    print("CSV files successfully reversed!")

    
reverse_csv('alert.csv', 'reversed_output.csv')