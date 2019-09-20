# Web Analytics
This repository contains the project for HW3 of Web Analytics and has the following structure:

    - folder /src:
        Here there are all the files needed to be coded to solve the problem:
            * Beam.py includes de Beam Search Algorithm as well as some other auxiliary functions needed by the algorithm
            method. We took as an example both the theory slides and the pseudocode mentioned in the article written
            by W. Duivesteijn et al. with few modifications. One of them is that when the refinement functions faces a
            nominal attribute, it won't create both (feature = value), (feature != value) for descriprions, instead it
            creates only (feature = value). This decision has been made in order to boost the algorithm's performance.
            * PriorityQ is a class where we implemented the PriorityQueues needed in Beam.py. The core of this class is
            priority queues in the boltons package, with a slight modification in order to meet our requirements.
            * Functions.py is just a bunch of auxiliary functions. Here it is defined among others the Yule Q Quality
            Measure and the representation of the solution.
    - folder /data:
        It includes a bunch of files that are samples (modified or not) extracted from the dataset that we were given.
    - root_folder /:
        Some simple tests to test our algorithm and parts of our code along with a functional demo

