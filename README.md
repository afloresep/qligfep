
# Changes in this repository: 
1. Collect_dG.py:
Introduced a new python script called collect_dG.py to view dG values in CSV formats, making it easier to analyze data from both 1.protein and 2.water. Now, you can achieve this functionality using just a single line of code. For more specific usage instructions, please refer to the updated README.md in the tutorial folder.

2. Improved README.md in Tutorial:
Revised the README.md file in the tutorial section, making it more coherent and user-friendly. It now contains updated commands and provides clearer instructions for users to follow.

3. Modified setup.py: Made several enhancements to setup.py for a smoother user experience:
    1. Now, setup.py automatically copies files from 1.ligprep to 3.setup, eliminating the need for manual intervention.
    2. If there is an existing folder from previous runs (e.g., 1.protein), setup.py creates a new folder (e.g., 1.protein-2) to avoid conflicts.
    3. Implemented an intelligent search in qprep.inp to find the cys bond that requires adding. It then references the atom number in protein.pdb file and incorporates it when calling QligFEP.
    4. Enhanced QligFEP.py: Introduced dynamic generation of submit.sh files in QligFEP.py based on the cluster specified as an argument (CSB/TETRA). This improvement ensures seamless compatibility with different cluster environments.

5. Added Template with Comprehensive Scripts: Included a template containing all the necessary scripts for each step of the process. This comprehensive template streamlines the execution of the workflow, enhancing overall efficiency.


## QligFEP v2.0 and QresFEP v1.0

This collection of python command line functions is designed with the
aim to facilitate a robust and fast setup of FEP calculations for the
software package **Q**. These modules use python 3, python 2 is no 
longer supported, and an old version of the code using python 2
is now only available in the python2 branch.

This package includes at the moment two main modules:  
- QligFEP.py: module to generate ligand FEP calculations using a
dual topology approach, 
see Jespers et al. (https://doi.org/10.1186/s13321-019-0348-5).  

- QresFEP.py: module to generate protein FEP calculations using a
single topology approach, 
see Jespers et al. (https://doi.org/10.1021/acs.jctc.9b00538). 

Future versions will include QLIE, dual topology QresFEP and several
translation tools for new forcefields (at the moment we support opls,
charmm,amber and openFF).

A few toplevel scripts are included in the scripts folder to facilitate
high throughput setup. Additionally, a tutorials folder is included
with a detailed description of the setup procedure as published in
Jespers et al. (QresFEP/QligFEP). This tutorial includes the generation
of ligand parameters using OPLS, how to prepare a protein system, and
how to run ligand and protein FEP calculations. These examples are 
based on ligand binding of CDk2 inhibitors.

## Installing QligFEP and QresFEP  

- Install a working version of Q, e.g.:  

    <https://github.com/esguerra/Q6>  

  
- Clone this repository:  

    git clone https://github.com/qusers/qligfep.git

- Create the shipped conda environment

    conda env create -f environment.yml

In settings.py:  

- Change SCHROD_DIR to the Schrodinger location, if you want to be
able to generate OPLS ligand parameters using ffld_server.  

- Change Q_DIR to the location of the q executables. This can be
particularly useful if you use setupFEP from a local machine on
a mounted directory. (In which case, the executables of the preparation
part and running part of Q are at several places).  

- You can add slurm specific parameters in the CLUSTER INPUTS section,
according to the given example.   

## Requirements  
- ffld_server  
- cgenff  
- Protein Preparation Wizard  
- Python3.10  
- Q  

contact: [Willem Jespers (PhD)](mailto:w.jespers@lacdr.leidenuniv.nl?subject=[QLigFEP]%20[QResFEP])

