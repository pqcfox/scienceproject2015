import os
import runtest
import shutil

tests_remaining = ['10_1', '10_2', '10_3', '10_4', '10_5', '10_6', '10_7', '10_8',
                   '100_1', '100_2', '100_3', '100_4', '100_5', '100_6', '100_7', '100_8',
                   '200_1', '200_2', '200_3', '200_4', '200_5', '200_6', '200_7', '200_8',
                   '500_1', '500_2', '500_3', '500_4', '500_5', '500_6', '500_7', '500_8',
                   '1000_1', '1000_2', '1000_3', '1000_4', '1000_5', '1000_6', '1000_7', '1000_8',
                   '2000_1', '2000_2', '2000_3', '2000_4', '2000_5', '2000_6', '2000_7', '2000_8',
                   '4075_1', '4075_2', '4075_3', '4075_4', '4075_5', '4075_6', '4075_7', '4075_8']

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
