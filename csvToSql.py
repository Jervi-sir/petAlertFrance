import pandas as pd

def create_table_statement(df, table_name):
    column_data_types = []
    for column, dtype in zip(df.columns, df.dtypes):
        if dtype == 'object':
            sql_dtype = 'VARCHAR(255)'
        elif dtype in ['int64', 'int32']:
            sql_dtype = 'INT'
        elif dtype in ['float64', 'float32']:
            sql_dtype = 'FLOAT'
        else:
            sql_dtype = 'VARCHAR(255)'
        column_data_types.append(f"{column} {sql_dtype}")
    return f"CREATE TABLE {table_name} ({', '.join(column_data_types)});"

def insert_statements(df, table_name):
    inserts = []
    for _, row in df.iterrows():
        values = ["'{}'".format(str(v).replace("'", "''")) if not pd.isna(v) else 'NULL' for v in row]
        insert_statement = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(values)});"
        inserts.append(insert_statement)
    return inserts

if __name__ == '__main__':
    csv_file_path = 'alert.csv'
    table_name = 'Alert'
    sql_file_path = 'output.sql'
    
    df = pd.read_csv(csv_file_path)
    
    with open(sql_file_path, 'w', encoding='utf-8') as sql_file:
        # Write CREATE TABLE statement
        sql_file.write(create_table_statement(df, table_name))
        sql_file.write('\n')
        
        # Write INSERT INTO statements
        for insert_statement in insert_statements(df, table_name):
            sql_file.write(insert_statement)
            sql_file.write('\n')
