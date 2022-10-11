# ZnTrack: Plot Example

This repository demonstrates how to use ZnTrack and DVC to add plots to an experiment. The following files are relevant:

### run_experiment.py

This file contains the necessary node implementation and thus the plot capability. In the node an artifical ```DataFrame``` will be created to demonstrate how to visualize tabular data. ZnTrack offers interaction with a ```DataFrame``` object using the ```zn.plot```-method. This is shown in the given file, which will plot the ```experiment``` (x-axis) and ```error``` (y-axis) columns.

### workflow.ipynb

Used to write the graph and execute the workflow.

### Inspect on Iterative Studio 

Click -> [![DVC](https://img.shields.io/badge/-tracked-white.svg?logo=data-version-control&link=https://dvc.org/?utm_campaign=badge)](https://studio.iterative.ai/user/JR-1991/projects/dvc-plot-example-ixq7swn31y?commits=4618729%2Cprimary%3B4618728%2Cpurple)

Here you can inspect the resulting plots of two runs by selecting the commits and clicking on the ```plots``` tab.
