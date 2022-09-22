import numpy as np
import pandas as pd

from zntrack import Node, zn

class RunExperiment(Node):
    
    # Parameters
    num_exps: int = zn.params()
    seed: float = zn.params()
    
    # Plots
    
    # ZnTrack offers a convinient way to plot data by simply
    # passing zn.plots as the default for an attribute.
    #
    # This will store the data as a dataframe in-memory and 
    # write metadata to a CSV file found in the "nodes" directory
    # Once commited to the repository, Iterative Studio will 
    # recognize the plot and display it in the "compare" section
     
    plot: pd.DataFrame= zn.plots(x="experiment", y="error")
    
    def run(self):
        """Generates random number plots in the unit interval"""
        
        np.random.seed(self.seed)
        
        self.plot = pd.DataFrame({
            "experiment": list(range(self.num_exps)),
            "error": [np.random.uniform(0,1) for _ in range(self.num_exps)]
        })
        
        self.plot.index.name = "index"