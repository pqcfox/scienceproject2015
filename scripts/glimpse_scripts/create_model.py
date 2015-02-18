#!/bin/env/python

"""Creates a new Glimpse model containing imprinted prototypes from a corpus.  This script can be called at the command line to create and export a model via pickle, or its create_model function can be called directly to return the model object """

from glimpse import experiment
from glimpse.models import MakeParams, MakeModel
import numpy as np
import pickle

def create_model(training_corpus, num_protos, prototype_source = "uniform", params = None, suppress_gui = False):
    """ set up a blank experiment from a new corpus and return the model containing S2 Kernels.

    :param training_corpus: relative or absolute path to corpus directory
    :type training_corpus: str
    :param num_protos: number of prototypes generated
    :type num_protos: int
    :param prototype_source: algorithm to generate prototypes. Imprint by default.
    :type prototype_source: string or callable.  See glimpse.experiment for details.
    :param params: optionally provide a Params object specifying model params.  
    :type params: glimpse.models.ml.param.Params
    :param suppress_gui: prevent gui for update param values from appearing. False by default.
    :type suppress_gui: boolean
    :returns: Model object encoding imprint data
    :rtype: glimpse.models.ml.model.Model

    """
    exp = experiment.ExperimentData()
    """blank experiment object."""

    if params == None:
        params = MakeParams()
    if not suppress_gui: params.configure_traits()
    """set the parameters for the experiment and model.  The parameter fields are populated with default values, then a GUI appears to allow changes."""
    
    experiment.SetCorpus(exp, training_corpus) 

    exp.extractor.training_set = np.ones(len(exp.corpus.labels), dtype=bool)
    """Since we're just collecting imprints here, we mark the whole set as training."""

    #exp.extractor.model = MakeModel() 
    
    experiment.SetModel(exp, params=params)
    """creates a blank model object. """

    print params
    print experiment.GetParams(exp)

    experiment.MakePrototypes(exp, num_protos, "uniform")
    """creates prototypes (S2 Kernels) from imprints, and stores them in the model object attached to the experiment"""

    return exp.extractor.model

if __name__ == '__main__':
    """ask for a root directory & num protos for the corpus and save the exported model object in the current directory.  """

    print "This script creates a new Glimpse model with S2 kernels and saves the Model object in a pickle file."
    corpus_root = raw_input("corpus directory? (relative or absolute path) ")
    num_protos= int(raw_input("number of prototypes? "))
    target_filename= raw_input("filename for exported pickle file? (relative or absolute path) ")

    model = create_model(corpus_root, num_protos)
    target_file = file(target_filename, 'w')
    pickle.dump(model,target_file)

    print "wrote file '%s'" % target_filename
