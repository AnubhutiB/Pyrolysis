import os
import pandas as pd 
#import numpy as np
import matplotlib.pyplot as plt
#from csaps import csaps
import scipy.signal

filelist = [y for y in os.listdir(os.getcwd()) if y.endswith(".csv")]

for file in filelist:
    
    print (file)
    data = pd.read_csv(file,skiprows=12, usecols=[0,3,4], names=['Time (min)', 'Relative mass loss (%)','Rate of mass loss (mg/s)'])
    x1 = data['Time (min)']
    x2 = data['Time (min)']
    y1 = data['Relative mass loss (%)']
    y2 = data['Rate of mass loss (mg/s)']
    ys = scipy.signal.savgol_filter(y2, 7, 3) # window size odd number, polynomial order 3
    
    fig=plt.figure()
    ax=fig.add_subplot(211) #111 is default; 211 for overlaying subplots horizontally
    ax2=fig.add_subplot(211, frame_on=False)
   
    ax.plot(x1,y1)
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Mass loss (%)")
    
    ax2.plot(x1,ys, color="C1")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel("Time (min)") 
    ax2.set_ylabel("Derivative (mg/s)")       
    ax2.xaxis.set_label_position('top') 
    ax2.yaxis.set_label_position('right') 
    
    # #Raw data plot
    ax3=fig.add_subplot(212)
    ax3.plot(x1,y1)
    #ax3.set_xlabel("Time (min)")
    ax3.set_ylabel("Mass loss (%)")
    
    ax4=fig.add_subplot(212, frame_on=False)
    ax4.plot(x2, y2, color="C2")
    ax4.xaxis.tick_top()
    ax4.yaxis.tick_right()
    #ax4.set_xlabel("Time (min)") 
    ax4.set_ylabel("Derivative (mg/s)")       
    #ax4.xaxis.set_label_position('top') 
    ax4.yaxis.set_label_position('right')
    
    fig.tight_layout(pad=0.1)
    plt.show()
    
