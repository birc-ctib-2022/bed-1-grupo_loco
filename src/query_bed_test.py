# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_


from query_bed import main
import filecmp
import os


def query1_test():
    input = 'data/query-1.txt'
    output = 'data/expected-1.txt'
    output_exp = 'data/output_query.txt'
    os.system(f"python src/query_bed.py {input}{output_exp}")
    assert filecmp.cmp(output_exp,output)

def query2_test():
    input = 'data/query-2.txt'
    output = 'data/expected-2.txt'
    output_exp = 'data/output_query.txt'
    os.system(f"python src/query_bed.py {input}{output_exp}")
    assert filecmp.cmp(output_exp,output)

def query3_test():
    input = 'data/query-3.txt'
    output = 'data/expected-3.txt'
    output_exp = 'data/output_query.txt'
    os.system(f"python src/query_bed.py {input}{output_exp}")
    assert filecmp.cmp(output_exp,output)

