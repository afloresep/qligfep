'''
Python script to clean files after FEP.
Should be called from the 3.setupFEP folder
'''
import os
import shutil

# Define the root directory where FEP folders are located
curdir = os.path.abspath('.')
# List of file names to preserve
preserve = ['md_1000_0000.dcd', 'md_0000_1000.dcd', 'eq5.re', 'eq1.re', 'eq3.re', 'eq5.dcd', 'qfep.inp', 'qfep.out']
for i in os.listdir(curdir):
    if i.startswith('1.protein') or i.startswith('2.water'):
        root_directory = os.path.abspath(i)
        # Loop through all directories starting with 'FEP_'
        for fep_folder in os.listdir(root_directory):
            if fep_folder.startswith('FEP_'):
                fep_folder_path = os.path.join(root_directory, fep_folder)
                print(f'Cleaning {fep_folder}...')
                # Inside each FEP folder, navigate to the 'FEP1' folder
                fep1_path = os.path.join(fep_folder_path, 'FEP1', '298')

                # Check if the 'FEP1/298' folder exists
                if os.path.exists(fep1_path):

                    # Loop through replica folders (1, 2, 3, ..., 10)
                    for replica_folder in os.listdir(fep1_path):
                        replica_path = os.path.join(fep1_path, replica_folder)

                        # Check if the replica folder exists
                        if os.path.isdir(replica_path):

                            # Create the 'outfile' folder inside the replica folder
                            outfile_path = os.path.join(replica_path, 'outfile')
                            os.makedirs(outfile_path, exist_ok=True)

                            # Loop through files in the replica folder
                            for file_name in os.listdir(replica_path):
                                file_path = os.path.join(replica_path, file_name)

                                # Check if the file should be preserved
                                if file_name in preserve:
                                    shutil.move(file_path, os.path.join(outfile_path, file_name))
                                else:
                                    # Remove files with extensions .log and .dcd
                                    if file_name.endswith(('.log', '.dcd', '.inp')):
                                        os.remove(file_path)

