# read the CSV file and generate the zip files
import os
import csv

import sys

from zipfile import ZipFile

from itertools import islice

def chunk_list(iterable, size):
    iterator = iter(iterable)
    for first in iterator:
        yield [first] + list(islice(iterator, size - 1))

CSV_FILE = 'attune-transect-discrete-samples.csv'

files = {}

with open(CSV_FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cruise = row['cruise']
        if cruise not in files:
            files[cruise] = []
        files[cruise].append(row['syn_filename'])
        files[cruise].append(row['redeuk_filename'])
        files[cruise].append(row['hetprok_filename'])

PARENT_DIR = '/mnt/lab_data/Attune/cruise_data'
DEST_DIR = os.path.join(PARENT_DIR, 'zipped_FCS')


for cruise in files:
    # the cruise dir starts with a date that we do not know, followed by an underscore, followed by the cruise name
    for dirname in os.listdir(PARENT_DIR):
        # ensure dirname refers to a directory
        if not os.path.isdir(os.path.join(PARENT_DIR, dirname)):
            continue
        if dirname.endswith(f'_{cruise}'):
            cruise_dir = dirname
            break
    
    print(f'compressing specified files in {cruise_dir}...')

    fcs_dir = os.path.join(PARENT_DIR, cruise_dir, 'preserved', 'FCS')

    if cruise == 'EN655': # exceptional case
        fcs_dir = os.path.join(PARENT_DIR, cruise_dir, 'preserved2', 'FCS')

    chunk_size = 10000

    for i, chunk in enumerate(chunk_list(files[cruise], chunk_size)):
        # dest_zip_path = os.path.join(DEST_DIR, f'{cruise}_attune_fcs_{i+1:03d}.zip')
        dest_zip_path = os.path.join(DEST_DIR, f'{cruise}_attune_fcs.zip')
        if os.path.exists(dest_zip_path):
            continue
        with ZipFile(dest_zip_path, 'w') as zipObj:
            chunk_files = set(chunk)
            for f in chunk_files:
                if f == 'NaN':
                    continue
                f_path = os.path.join(fcs_dir, f)
                if not os.path.exists(f_path):
                    print(f'WARNING: {f} does not exist')
                    continue
                print(f'adding {f} to {os.path.basename(dest_zip_path)}...')
                zipObj.write(f_path, f)