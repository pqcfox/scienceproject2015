import os
import runtest
import shutil

tests_remaining = ['2000_2', '2000_3', '2000_4']

files_to_save = ['data/matrix.p', 'data/classes.p', 'data/results.txt', 'logfile']
dest_folder = 'past_runs'
root_folder = '/stash/mm-group/ct101hmax'

for test in tests_remaining:
    dest = os.path.join(dest_folder, test) 
    os.mkdir(dest)
    num_protos = int(test.split('_')[0]) 
    runtest.runtest(num_protos)
    os.chdir(root_folder)
    for f in files_to_save:
        shutil.copy(f, dest) 
