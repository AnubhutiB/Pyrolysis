#this code imports two csv files in two dataframes (df1 and df2) then you 
#make overlaid plots and subplots. T

import os
import pandas as pd
import matplotlib.pyplot as plt 

filelist = [y for y in os.listdir(os.getcwd()) if y.endswith(".csv")]

for file in filelist:
    #this data frame works for concatenated tga files which follow the same sequence
    
    data = pd.read_csv(file,skiprows=10)
    # load data set
    #temp= data.iloc [:,1].values.reshape(-1, 1) #make sure that all files follow the same temperature profile. To save a single column into a dataframe use values and reshape
    df1 = data.iloc [:,[1,2,6,10,14,18]] #If I import individual csv files and plot the first and third + first and fourth columns then my work might be less
    df2 = data.iloc [:,[1,3,7,11,15,19]]
 
    figure, axes = plt.subplots(2, 1, figsize=(10,10)) #generates subplots that are displayed as two rows and one column
    #only df1.plot will use x axis as number of items. I can use this to also mean that data is plotted vs time since time is increasing by unit value
    df1.plot(x= "Temp", ax=axes[0]) 
    #x = "Temp" plots the data vs the column called Temp. I had to rename it in the csv. the names can also be changed while importing the data. 
    #axes 0 and 1 indicate the location where the plot will go
    df2.plot(x= "Temp", ax=axes[1])
    axes[0].set_xlabel('Temperature' + u"\N{DEGREE SIGN}"+'C')
    axes[0].set_ylabel('Relative mass loss (%)')
    axes[0].set_title(file)    
    
    axes[1].set_xlabel('Temperature' + u"\N{DEGREE SIGN}"+'C')
    axes[1].set_ylabel('Rate of mass loss (wt%/min)')
    plt.rcParams.update({'font.size': 14})
    axes[0].legend(frameon=False)
    axes[1].legend(frameon=False)
    plt.savefig(file+'.png', dpi =300)
   

