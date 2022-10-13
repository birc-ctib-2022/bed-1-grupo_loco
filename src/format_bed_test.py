# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from format_bed import main
import filecmp
import os
#from difflib import Differ

#exp_output = "data/output.bed"
#input = "data/output.bed"
#output = main(input)

def format_test():
    input = 'data/input.bed'
    output = 'data/output.bed'
    output_format = 'data/output_format.bed'
    os.system(f"python src/format_bed.py {input}{output_format}")
    assert filecmp.cmp(output_format,output)


