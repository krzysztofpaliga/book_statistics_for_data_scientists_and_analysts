import pandas as pd
import numpy as np
import glob
path = './TransactionNarrative'
files = glob.glob(path + '/*.txt')
files
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        print(f.read())
import os
import glob
def check_file_quality(content):
    required_fields = ['Date:', 'Merchant:', 'Amount:', 'Description:']
    missing_fields = [field for field in required_fields if field not in content]
def check_file_quality(content):
    required_fields = ['Date:', 'Merchant:', 'Amount:', 'Description:']
    missing_fields = [field for field in required_fields if field not in content]
    file_size = len(content.encode('utf-8'))
    line_count = content.count('\n') + 1
    qualit_assessment = {
        'file_name': file,
        'file_size_bytes': file_size,
        'line_count': line_count,
        'missing_fields': missing_fields
    }
    return quality_assessment
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
        quality_result = check_file_quality(content)
        print(quality_result)
        print("=" * 40)
def check_file_quality(content):
    required_fields = ['Date:', 'Merchant:', 'Amount:', 'Description:']
    missing_fields = [field for field in required_fields if field not in content]
    file_size = len(content.encode('utf-8'))
    line_count = content.count('\n') + 1
    quality_assessment = {
        'file_name': file,
        'file_size_bytes': file_size,
        'line_count': line_count,
        'missing_fields': missing_fields
    }
    return quality_assessment
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
        quality_result = check_file_quality(content)
        print(quality_result)
        print("=" * 40)
%history -f ipython.py
