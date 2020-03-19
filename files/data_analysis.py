#!/usr/bin/env python
# coding: utf-8
# %%

# %%
import numpy
import glob
import matplotlib.pyplot
import sys

def visualize(filename): #Take a filename and make plots
    
    data = numpy.loadtxt(fname=filename,delimiter = ',')
    
    figure = matplotlib.pyplot.figure(figsize=(10.0,3.0))

    axes1 = figure.add_subplot(1,3,1)
    axes2 = figure.add_subplot(1,3,2)
    axes3 = figure.add_subplot(1,3,3)

    axes1.set_ylabel('average')
    axes2.set_ylabel('max')
    axes3.set_ylabel('min')

    axes1.plot(numpy.mean(data, axis=0))
    axes2.plot(numpy.max(data, axis=0))
    axes3.plot(numpy.min(data, axis=0))

    figure.tight_layout()
    matplotlib.pyplot.savefig(filename+'_fig.eps')
    
def detect_problems(filename): #Take a filename;  Conditional example
    data=numpy.loadtxt(fname=filename,delimiter=',')
    if numpy.max(data,axis=0)[0] == 0 and numpy.max(data,axis=0)[20] == 20:
        print('Suspicious looking maxima')
    elif numpy.sum(numpy.min(data,axis=0)) ==0:
        print('Minima add up to zero')
    else:
        print('Seems OK!')

if __name__ == "__main__":
        
    filename = sys.argv[1]

    visualize(filename)
    detect_problems(filename)


# %%




