import subprocess
import sys
import pandas as pd
import glob
import os
import shutil

def call_analyze_FEP(folder_path):
    try:
        # Call analyze_FEP_2.py using subprocess and capture the output
        result = subprocess.run(['python', 'analyze_FEP.py', '-F', folder_path, '-C', 'CSB'], capture_output=True, text=True)

        # Return the standard output of analyze_FEP_2.py and the generated .csv filename
        print(result.stdout)
        csv_name = os.path.basename(folder_path) + '.csv'
        return csv_name

    except Exception as e:
        print(f"Error occurred for folder: {folder_path}, Error: {e}")
        return "", ""

path_list = []
# Check if there are arguments provided in the command line
if len(sys.argv) >= 4:  # Check if there are at least 4 arguments (script name, desired folder, and python) provided in the command line
    # Skip the first 2 elements of sys.argv, as they contain the script name and desired folder
    for new_argument in sys.argv[2:]:
        path_list.append(new_argument)
        print(f"Argument '{new_argument}' added to path_list.")
else:
    print("Insufficient arguments provided. The path_list remains unchanged.")

# Create a new folder with the name given in the command line
output_folder = ""
if len(sys.argv) >= 2:
    output_folder = sys.argv[1]
    os.makedirs(output_folder, exist_ok=True)


# Loop through the list of folders and call analyze_FEP_2.py for each folder
for folder_path in path_list:
    # Call the function to run analyze_FEP_2.py for the current folder
    call = call_analyze_FEP(folder_path)

# List to store the generated .csv filenames
csv_filenames = glob.glob('*.{}'.format('csv'))
print(csv_filenames)

# Move the .csv files inside the output folder
for csv_file in csv_filenames:
    print('this is csv_file', csv_file)
    if os.path.exists(csv_file):  # Check if the .csv file exists before moving
        try:
            shutil.move(csv_file, os.path.join(output_folder, csv_file))
        except Exception as e:
            print(f"Error occurred while moving {csv_file} to {output_folder}. Error: {e}")

# List all .csv files only in the current directory (excluding the moved files)
csv_files = glob.glob('*.{}'.format('csv'))
print(type(csv_files))
