
"""Using an existing Glimpse model that contains prototype data, compute activations on a dataset to obtain the C2 features for each image.  Export the resulting data in a format usable by SVMLight.  SVM-readable files are placed in the current directory by default

"""

import numpy as np
from glimpse import experiment
from glimpse.models import MakeParams, MakeModel
from glimpse.pools import MakePool
import pickle

import os

def run_model(corpus_root, model, params = None, features_file_path=None):
    """
    :param corpus_root: path
    :type corpus_root: string
    :param params: optional params object to set non-default values.
    :type params: glimpse Params object

    """

    exp = experiment.ExperimentData()

    experiment.SetCorpus(exp, corpus_root)

    exp.extractor.model = model
    
    print "Computing activations..."
    experiment.ComputeActivation(exp, 'C2', MakePool())

    """The features are exported in SVMLight-friendly files.  If no target directory is specified, it saves them in the current directory."""
        
    if features_file_path == None:
        features_file_path = "%s/features" %os.getcwd()

    WriteSVMLightFile(exp,features_file_path)                                  
    WritePathsFile(exp,features_file_path)

    """function returns the complete data of the experiment for optional use elsewhere."""
    return exp

def WriteSVMLightFile(exp,file_path):
    layers = experiment.ResolveLayers(exp, 'C2')
    features = experiment.ExtractFeatures(layers, exp.extractor.activation)
    labels = exp.corpus.labels

    outfile = file(file_path, 'w')
    for i in range(len(features)):
        nextline = "%d " % labels[i]
        for j in range(len(features[i])):
            nextline += "%d:%f " % (j+1, features[i][j])
        nextline+="\n"
        outfile.write(nextline)
    outfile.close()

def WritePathsFile(exp, file_path):
    paths = exp.corpus.paths
    outfile = file(file_path+"-paths", 'w')
    for i in range(len(paths)):
        nextline = "%s" %paths[i]
        nextline += '\n'
        outfile.write(nextline)
    outfile.close()

if __name__ == "__main__":
    print "This script will compute activations at all layers and export C2 features of the given corpus using the given model. "

    saved_model_filename = raw_input("name of pickle file with saved model data? ")
    target_exp_filename = raw_input("name of pickle file to save new experiment data? ")

    corpus_root = raw_input("corpus directory? relative or absolute path) ")
    
    exp = run_model(corpus_root, pickle.load(file(saved_model_filename, 'r')))

    pickle.dump(exp, file(target_exp_filename, 'w'))
