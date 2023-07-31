import os
import shutil
import glob

# Get the path to the '1.ligprep' directory
current_folder = os.path.dirname(os.path.abspath(__file__))
ligandprep_folder = os.path.join(current_folder, '..', '1.ligprep')

# Check if the '1.ligprep' directory exists
if not os.path.exists(ligandprep_folder):
    print("Error: '1.ligprep' directory not found.")
else:
    lig_files = glob.glob(os.path.join(ligandprep_folder, '*.pdb')) + \
                glob.glob(os.path.join(ligandprep_folder, '*.lib')) + \
                glob.glob(os.path.join(ligandprep_folder, '*.prm'))

    for file in lig_files:
        shutil.copy(file, '.')

systems = ['protein', 'water']
cnt = 0
# Change this to where you installed QligFEP
setupFEP = 'python /home/USER/QLIGFEP/qligfep/QligFEP.py'
cysbond = ''
windows = '100'
for system in systems:
    cnt += 1
    directory = str(cnt) + '.' + system

    # Check if the directory already exists and create a new one with a different name if needed
    new_directory = directory
    suffix = 2
    while os.path.exists(new_directory):
        new_directory = f"{directory}-{suffix}"
        suffix += 1

    os.mkdir(new_directory)

    with open('pairs.txt') as infile:
        for line in infile:
            line = line.split()
            mol1 = line[0]
            mol2 = line[1]
            if system == 'water':
                call = setupFEP + ' -l1 ' + mol1 + ' -l2 ' + mol2 + ' -FF OPLS2015 -s water -S sigmoidal -c CSB -r 25 -l 1  -w' + windows
            if system == 'protein':
                call = setupFEP + ' -l1 ' + mol1 + ' -l2 ' + mol2 + ' -FF OPLS2015 -b' + cysbond + ' -S sigmoidal -s protein -c CSB -r 25 -l 1 -w' + windows
            src = 'FEP_' + mol1 + '-' + mol2
            dst = os.path.join(new_directory, 'FEP_' + mol1 + '-' + mol2)
            os.system(call)
            shutil.move(src, dst)
