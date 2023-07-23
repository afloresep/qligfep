import subprocess
import csv
import sys

def call_analyze_FEP_2(folder_path):
    try:
        # Call analyze_FEP_2.py using subprocess and capture the output
        result = subprocess.run(['python', 'analyze_FEP.py', '-F', folder_path, '-C', 'CSB'], capture_output=True, text=True)

        # Return the standard output of analyze_FEP_2.py
        return result.stdout
    except Exception as e:
        print(f"Error occurred for folder: {folder_path}, Error: {e}")
        return ""

path_list = []
# Check if there are arguments provided in the command line
if len(sys.argv) >= 3:
    # Skip the first 2 element of sys.argv, as it contains the script name and python
    for new_argument in sys.argv[1:]:
        path_list.append(new_argument)
        print(f"Argument '{new_argument}' added to path_list.")
        csv_name = new_argument.split("/")[-1] + '.csv'
else:
    print("No arguments provided. The path_list remains unchanged.")


# Open dG.csv file for writing
print(csv_name)
with open(csv_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the CSV header
    csv_writer.writerow(['Folder Path', 'Results'])

    # Loop through the list of folders and call analyze_FEP_2.py for each folder
    for folder_path in path_list:
        # Call the function to run analyze_FEP_2.py for the current folder
        results = call_analyze_FEP_2(folder_path)

        # Write the results to the CSV file
        csv_writer.writerow([folder_path, results.strip()])  # strip() removes leading/trailing whitespaces

print("All folders analyzed and results written to dG.csv.")
