# ZnTrack: Plot Example

This repository demonstrates how to use ZnTrack and DVC to add plots to an experiment. The following files are relevant:

### run_experiment.py

This file contains the necessary node implementation and thus the plot capability. In the node an artifical ```DataFrame``` will be created to demonstrate how to visualize tabular data. ZnTrack offers interaction with a ```DataFrame``` object using the ```zn.plot```-method. This is shown in the given file, which will plot the ```experiment``` (x-axis) and ```error``` (y-axis) columns.

### workflow.ipynb

Used to write the graph and execute the workflow.
