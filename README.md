# PsvChecker
A static checker to examine semantic unpreservation on code transpilation among Java, Python and C++

## Required Packages

Python >= 3.8

tree-sitter 0.20.1

z3-solver 4.13.0.0

## Project Structure

The project contains source code of tool, dataset and main results. There are four directories in the project:

- **dataset**: Contains parallel corpus for Java to CPP, Java to Python and Python to Java extracted from TransCoder. Also contains dataset used in BatFix.
- **result**: Contains result of transpilation and check and repair result of tools.
- **src**: Contains source code of tool. The main code is in src/psvchecker/check.py
- **supplement**: Contains some manually reviewed results, including details of false positives, inconsistencies in the original dataset, and the influence of noise in dataset of BatFix (corresponding to the section Threats to Validity in the paper).

## Running the Main Program

Run the main file **src/psvchecker/check.py** to run the tool:

`python3 src/psvchecker/check.py --src_lang "$1" --tgt_lang "$2" --src_code "$3" --tgt_code "$4" --typed_path "$5" --repair_path "$6" --changelog "$7"`

$1: Source language, $2: Target language. One can input 'Java', 'Python' or 'CPP'.

$3: Input path of source code. $4: Input path of transpiled code. 

$5: Output path of typed code for untyped Python code. $6: Output path of repaired code. 

$7(optional argument): Output path of change log of repairing.

The input and output paths can either be files or directories. If both are files, only that single file will be checked and repaired. If both are directories, all files within the input directory will be recursively checked and repaired.
