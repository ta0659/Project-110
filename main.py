import pandas as  pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import random

dataset = []
df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

def randomsetofdata(counter):
    for i in range(0,counter):
        random_index = random.randint(0,(len(data) - 1))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df], ['Temp'], show_hist = False)
    fig.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randomsetofdata(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    print('Sampling Mean' ,mean)
    std_dv = statistics.stdev(data)
    print('Population Mean',std_dv)

setup()

