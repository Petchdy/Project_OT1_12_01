from cProfile import label
from itertools import count
from operator import le
from turtle import color
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'tahoma'
from matplotlib import font_manager
import base64
from io import BytesIO
import numpy as np

def get_bar_graph(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))
    plt.title('Covid Report')
    # plt.plot(x,y)
    plt.bar(x,y,color=['#dcd3c2','#bf7a68','#89979a','#465658','#864f41','#c4a56b','#bc4747'])
    
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]//2, y[i], ha = 'center')

    addlabels(x,y)
    # plt.xticks(rotation=45)
    plt.xlabel('types')
    plt.ylabel('Number of Tweets')
    plt.ylim([0, max(y)+150])
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('tis-620')
    buffer.close()
    return graph

def pie_chart(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))
    plt.title('Covid Report')
    # plt.plot(x,y)

    if (len(x) == 7):
        plt.pie(y, labels = x, 
        # ไม่สบายใจ, ความเป็นอยู่,
        colors=['#326789', '#E65C4F', '#41436A', '#974063', '#FDD037', '#AECFA4'])
    else:
        plt.pie(y, labels = x, 
        # ไม่สบายใจ, ความเป็นอยู่,
        colors=['#326789', '#E65C4F', '#41436A', '#974063', '#AECFA4'])

    # plt.xticks(rotation=45)
    plt.xlabel('Affliction types')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('tis-620')
    buffer.close()
    return graph

def get_level_bar_graph(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))
    plt.title('Covid Report')
    # plt.plot(x,y)
    plt.bar(x,y,color=['#698f33','#d4a91e','#cf8525','#9c4848'])
    
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]//2, y[i], ha = 'center')

    addlabels(x,y)
    # plt.xticks(rotation=45)
    plt.xlabel('types')
    plt.ylabel('Number of Tweets')
    plt.ylim([0, max(y)+150])
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('tis-620')
    buffer.close()
    return graph

def get_sentiment_bar_graph(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))
    plt.title('Covid Report')
    # plt.plot(x,y)
    plt.bar(x,y,color=['#698f33','#b32b3b'])
    
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]//2, y[i], ha = 'center')

    addlabels(x,y)
    # plt.xticks(rotation=45)
    plt.xlabel('types')
    plt.ylabel('Number of Tweets')
    plt.ylim([0, max(y)+150])
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('tis-620')
    buffer.close()
    return graph

def get_bar_graph_all(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))
    plt.title('Covid Report')
    # plt.plot(x,y)
    plt.bar(x,y,color=['#dcd3c2','#bf7a68','#89979a','#465658','#864f41','#c4a56b','#bc4747'])
    
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]//2, y[i], ha = 'center')

    addlabels(x,y)
    # plt.xticks(rotation=45)
    plt.xlabel('types')
    plt.ylabel('Number of Tweets')
    plt.ylim([0, 5500])
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('tis-620')
    buffer.close()
    return graph