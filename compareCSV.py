import pandas as pd

def compare_csv_and_save_updated_rows(old_csv_path, updated_csv_path, id_column):
    # Read the CSV files
    old_df = pd.read_csv(old_csv_path)
    new_df = pd.read_csv(updated_csv_path)

    # Ensure they have the same columns
    assert(old_df.columns.equals(new_df.columns))
    
    # Set the index to be the ID column for easier comparison
    old_df.set_index(id_column, inplace=True)
    new_df.set_index(id_column, inplace=True)
    
    # Use compare function
    changes = old_df.compare(new_df)

    # Get the updated IDs
    updated_ids = changes.index.get_level_values(id_column).unique()

    # Extract the updated rows from the new DataFrame
    updated_rows = new_df.loc[updated_ids]
    
    # Save the updated rows to a new CSV file
    updated_rows.to_csv('updated_rows.csv')

    # Return the count of updated IDs
    return len(updated_ids)

old_csv_path = 'previous_july.csv'
updated_csv_path = 'current_july.csv'
id_column = 'id' # replace with your actual id column name

updated_count = compare_csv_and_save_updated_rows(old_csv_path, updated_csv_path, id_column)

# Print count of updated rows
print(f"Count of updated rows: {updated_count}")


# Specify the columns to compare
"""
columns_to_compare = ['isFound', 'message', 'Alert_type',
'postOnFb', 'archive', 'isSharedOnFb', 'boFixed', 
'isDeleted', 'deletedBy', 'isPaid', 'isBoosted', 'tab_option']
"""

