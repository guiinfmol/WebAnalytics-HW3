# Beam Search Algorithm
Project part of HW3 from the course 2IID0 - Web Analytics @ TU Eindhoven. Contains the Python code as well an R script to obtain the dataset from the original one provided by StudePortals. 

The structure is the following:
* **data**: Contains both the original dataset and the one extracted with the R script used by the Python script implementation. 
* **docs**: Contains the statement of the problems for a better understanding of the task.
* **src**: Here there are all the files needed to be coded to solve the problem. <br>
    * *Beam.py* includes de Beam Search Algorithm as well as some other auxiliary functions needed by the algorithm method. We took as an example both the theory slides and the pseudocode mentioned in the article written by W. Duivesteijn et al. with few modifications. One of them is that when the refinement functions faces a nominal attribute, it won't create both (feature = value), (feature != value) for descriprions, instead it creates only (feature = value). This decision has been made in order to boost the algorithm's performance.
    * *PriorityQ.py*  contains a class where we implemented the PriorityQueues needed in Beam. The core of this class is priority queues in the boltons package, with a slight modification in order to meet our requirements.
    * *Functions.py* is just a bunch of auxiliary functions. Here it is defined among others the Yule Q Quality Measure and the representation of the solution.
* **tests**: Include a simple script (no unit testing) testing that the PriorityQ works.
* *data_preprocessing.R* is a R file that preprocess the data from the original data so that it can be used later in Python.
* *main.py* execution of the algorithm, it expects *data/final_dataset.csv* to exist. To execute just install the ```requirements.txt``` and execute ```python main.py```.
* *stats.py* prints the stats of the dataset. Just run with ```python main.py```.

