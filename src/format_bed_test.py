# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from format_bed import main
import filecmp
from difflib import Differ

exp_output = "data/output.bed"
input = "data/output.bed"
output = main(input)

def format_test():
    assert filecmp.cmp(output,exp_output)


