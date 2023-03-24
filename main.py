#!/home/htran197/anaconda3/envs/python3/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns
import time
from function import *
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#Global variables used for draw_graph function
count = {}
a = {}
b = {}
mSize = input('Enter the dimension of a square matrix: ')
mSize = int(mSize)
timeInt = input('Enter the time interval in ms: ')
timeInt = int(timeInt)
fig, axs = plt.subplots(mSize, sharex=True, sharey=True, figsize=(10, 5*mSize))
fig.suptitle('Matrix-Vector Multiplication of {} Variables'.format(mSize))
fig.supxlabel('Time(ms)')
fig.supylabel('Value')

#Initializing the global variables
for i in range(mSize):
    count[i] = 0
    a[i] = []
    b[i] = []


#Draw animated dynamic graph
def draw_graph(i):
    global count, graph, a, b
    for iter in range(mSize):
        count[iter] +=1
        a[iter].append(count[iter])
        b[iter].append(graph[str(iter)][count[iter]])
        axs[iter].cla()
        axs[iter].plot(a[iter],b[iter])
        axs[iter].set_title("Variable{}".format(str(iter)))
        
        
try:    
    #Give random values for matrix and vector
    matrix = np.random.randint(5, size=(mSize, mSize))
    vector = np.random.randint(5, size=(mSize))
    result = vector

    #Create column names for dataframe
    column = np.empty(mSize, dtype=str)
    for i in range(mSize):
        column[i] = str(i)

    #Initialized dataframe with column name
    graph = pd.DataFrame(columns=column)
    graph.columns = graph.columns.astype(str)

    #Keep track of number of iteration
    timeCount = 0
    print("Running matrix multiplication. Press CTRL+C to stop the application and produce the graphs.")
    
    #Continuously doing multiplication and ploting until user force stop application by CTRL+C
    while True:
        result = MatVecMul(matrix,result)     
        graph = graph.append(pd.DataFrame(result.reshape(1,-1), columns=list(graph)), ignore_index=True)
        timeCount += 1
        time.sleep(timeInt/1000)
        timeArr = range(0,timeCount+1)


finally:
    #Create dynamic plot of each variable when user interupt with CTRL+C  
    print()
    anim = animation.FuncAnimation(plt.gcf(),draw_graph,interval=timeInt)
    anim.save('Output.gif',writer='imagemagick')