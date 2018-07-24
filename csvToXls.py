import pandas as pd
import os

folder = raw_input('Path to folder with csv files (use / in Windows): ')
result_filename = raw_input('Name of output file .xlsx: ')

os.chdir(folder)
files_in_folder = os.listdir(os.curdir)

# get only csv's in folder
csv_files = []
for f in files_in_folder:
    if f.endswith('.csv'):
        csv_files.append(f)

writer = pd.ExcelWriter(result_filename)

for csv in csv_files:
    df = pd.read_csv(csv)
    sheetname = csv.split('.')[0]
    df.to_excel(writer, sheet_name=sheetname, index=False)
writer.save()
