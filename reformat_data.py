import sys


core = "Boom Prefetch"
design = "16 Fetch Unit, 4 Rank"
db_size = "27MB"



import pandas as pd

def reformat_csv(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Example reformatting operations (uncomment and modify as needed)

        df.columns = [col.strip() for col in df.columns]
        #Remove columns
        df = df.drop(['bench'], axis=1)
        df = df.drop(['temp'], axis=1)
        df = df.drop(['row_count'], axis=1)
        df = df.drop(['l1_references'], axis=1)
        df = df.drop(['l1_refills'], axis=1)
        df = df.drop(['time'], axis=1)


        # Add Column
        df['Core'] = core
        df["Design"] = design
        df["DB Size"] = db_size

         #Rename columns
        df = df.rename(columns={
            'mem': 'DB Organization',
            'cycles': 'Time(Cycles)',
            'col_width': 'Column Size',
            'inst_retired': 'InstRet',
            'row_size': 'Row Size',
            'enabled_col_num': "Num Columns",
            'stall_ctrl_trapper': 'ctrl-trapper',
            'stall_fetch_ctrl': 'fetch-ctrl',
            'stall_fetch_full': 'fetch-full',
            'stall_fetch_memory': 'fetch-mem',
            'stall_req_fetch': 'req-fetch',
            'l2_refills': 'llc-out',
            'l2_references': 'llc-access'
         })


        
         #Reorder columns
        columns_order = ['Core', 'DB Size', 'DB Organization', "Column Size", 'Num Columns', 'Row Size',\
             'Time(Cycles)', 'InstRet', 'ctrl-trapper', 'fetch-ctrl', 'fetch-full', 'fetch-mem', 'req-fetch', 'llc-access', 'llc-out', 'Design']
        df = df[columns_order]
        
        df['DB Organization'] = df['DB Organization'].replace(' r', 'rme').replace(' c', 'col').replace(' d', 'row')
        # 3. Convert date format
        # df['date_column'] = pd.to_datetime(df['date_column']).dt.strftime('%Y-%m-%d')
        
        # 4. Filter rows
        # df = df[df['column_name'] > some_value]
        
        # 5. Add new column
        # 
        
       
        
        # Save the reformatted CSV
        df.to_csv(output_file, index=False)
        print(f"Successfully reformatted CSV and saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found")
    except Exception as e:
        print(f"Error occurred: {str(e)}")



if __name__ == "__main__":
    file = sys.argv[1]
    reformat_csv(file, file.split(".csv")[0]+"_reformat.csv")