from calendar import c
from cmath import pi
from contextlib import nullcontext
from django.shortcuts import render
from django.http import HttpResponse
from .models import Covid, Post
import pandas as pd
from .graph import get_bar_graph
from .graph import get_bar_graph_all
from .graph import get_level_bar_graph
from .graph import get_sentiment_bar_graph
from .graph import pie_chart

# Create your views here.

# def main(request):
#     title = 'Main Page'
#     covids_list = Covid.objects.all()
#     context = {'title': title,
#                'covids_list': covids_list}
#     return render(request, 'covids/new_main_page.html',
#                              context)
def Contract(request):
    return render(request, 'covids/Contract.html')


def main(request):

    # Read csv file
    x = 'all'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'title': 'Overall', 'csv': data, 'groupdata': groupdata, 'graph': graph}

    return render(request, 'covids/main.html',  context)

def compare_sentiment(request):

    # Set default if not request
    contextleft = {'csv': '', 'groupdata': '', 'graph': '', 'selectedmonth': '0'}
    contextright = {'csv': '', 'groupdata': '', 'graph': '', 'selectedmonth': '0'}

    # Get request parameter
    selectedmonthleft = request.GET.get('ddlleft')
    selectedmonthright = request.GET.get('ddlright')

    if selectedmonthleft is not None and selectedmonthright is not None :
        # Read csv file
        pd.set_option('display.max_rows', None)
        dataleft = pd.read_csv('data/' + str(selectedmonthleft) + '.csv')
        dataright = pd.read_csv('data/' + str(selectedmonthright) + '.csv')

        # Summary
        groupdataleft = dataleft.groupby(['Sentiment'])['Sentiment'].count()
        groupdataright = dataright.groupby(['Sentiment'])['Sentiment'].count()
        
        # groupdata = data.groupby(['Sentiment'])['Sentiment'].count()
        
        # Plot Graph left
        x = [x for x in groupdataleft.keys()]
        # print(x)
        y = [y for y in groupdataleft]
        # print(y)
        graphleft = get_sentiment_bar_graph(x, y)
        # print(graph)
        
        # Plot Graph right
        x = [x for x in groupdataright.keys()]
        # print(x)
        y = [y for y in groupdataright]
        # print(y)
        graphright = get_sentiment_bar_graph(x, y)

        # Return data left
        contextleft = {'csv': dataleft, 'groupdata': groupdataleft, 'graph': graphleft, 'selectedmonth': selectedmonthleft}

        # Return data right
        contextright = {'csv': dataright, 'groupdata': groupdataright, 'graph': graphright, 'selectedmonth': selectedmonthright}

    # Return data
    context = {'title': 'Compare Page', 'leftdata': contextleft, 'rightdata': contextright}

    return render(request, 'covids/compare.html',  context)

def compare_types(request):

    # Set default if not request
    contextleft = {'csv': '', 'groupdata': '', 'graph': '', 'selectedmonth': '0'}
    contextright = {'csv': '', 'groupdata': '', 'graph': '', 'selectedmonth': '0'}

    # Get request parameter
    selectedmonthleft = request.GET.get('ddlleft')
    selectedmonthright = request.GET.get('ddlright')

    if selectedmonthleft is not None and selectedmonthright is not None :
        # Read csv file
        pd.set_option('display.max_rows', None)
        dataleft = pd.read_csv('data/' + str(selectedmonthleft) + '.csv')
        dataright = pd.read_csv('data/' + str(selectedmonthright) + '.csv')

        # Summary
        groupdataleft = dataleft.groupby(['types'])['types'].count()
        groupdataright = dataright.groupby(['types'])['types'].count()
        
        # groupdata = data.groupby(['Sentiment'])['Sentiment'].count()
        
        # Plot Graph left
        x = [x for x in groupdataleft.keys()]
        # print(x)
        y = [y for y in groupdataleft]
        # print(y)
        graphleft = get_bar_graph(x, y)
        # print(graph)
        
        # Plot Graph right
        x = [x for x in groupdataright.keys()]
        # print(x)
        y = [y for y in groupdataright]
        # print(y)
        graphright = get_bar_graph(x, y)

        # Return data left
        contextleft = {'csv': dataleft, 'groupdata': groupdataleft, 'graph': graphleft, 'selectedmonth': selectedmonthleft}

        # Return data right
        contextright = {'csv': dataright, 'groupdata': groupdataright, 'graph': graphright, 'selectedmonth': selectedmonthright}

    # Return data
    context = {'title': 'Compare Page', 'leftdata': contextleft, 'rightdata': contextright}

    return render(request, 'covids/compare.html',  context)

def compare_levels(request):

    # Set default if not request
    contextleft = {'csv': '', 'groupdata': '', 'graph': '', 'selectedmonth': '0'}
    contextright = {'csv': '', 'groupdata': '', 'graph': '', 'selectedmonth': '0'}

    # Get request parameter
    selectedmonthleft = request.GET.get('ddlleft')
    selectedmonthright = request.GET.get('ddlright')

    if selectedmonthleft is not None and selectedmonthright is not None :
        # Read csv file
        pd.set_option('display.max_rows', None)
        dataleft = pd.read_csv('data/' + str(selectedmonthleft) + '.csv')
        dataright = pd.read_csv('data/' + str(selectedmonthright) + '.csv')

        # Summary
        groupdataleft = dataleft.groupby(['levels'])['levels'].count()
        groupdataright = dataright.groupby(['levels'])['levels'].count()
        
        # groupdata = data.groupby(['Sentiment'])['Sentiment'].count()
        
        # Plot Graph left
        x = [x for x in groupdataleft.keys()]
        # print(x)
        y = [y for y in groupdataleft]
        # print(y)
        graphleft = get_level_bar_graph(x, y)
        # print(graph)
        
        # Plot Graph right
        x = [x for x in groupdataright.keys()]
        # print(x)
        y = [y for y in groupdataright]
        # print(y)
        graphright = get_level_bar_graph(x, y)

        # Return data left
        contextleft = {'csv': dataleft, 'groupdata': groupdataleft, 'graph': graphleft, 'selectedmonth': selectedmonthleft}

        # Return data right
        contextright = {'csv': dataright, 'groupdata': groupdataright, 'graph': graphright, 'selectedmonth': selectedmonthright}

    # Return data
    context = {'title': 'Compare Page', 'leftdata': contextleft, 'rightdata': contextright}

    return render(request, 'covids/compare.html',  context)

def January(request):

    x = '1'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/January.html',  context)

def February(request):

    x = '2'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/February.html',  context)

def March(request):

    x = '3'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/March.html',  context)

def April(request):

    x = '4'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/April.html',  context)

def May(request):

    x = '5'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/May.html',  context)

def June(request):

    x = '6'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/June.html',  context)

def July(request):

    x = '7'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/July.html',  context)

def August(request):

    x = '8'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/August.html',  context)

def September(request):

    x = '9'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/September.html',  context)

def October(request):

    x = '10'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/October.html',  context)

def November(request):

    x = '11'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/November.html',  context)

def December(request):

    x = '12'
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('data/'+x+'.csv')

    # Summary
    groupdata = data.groupby(['types'])['types'].count()
    
    # Plot Graph
    x = [x for x in groupdata.keys()]
    # print(x)
    y = [y for y in groupdata]
    # print(y)
    graph = pie_chart(x, y)
    # print(graph)
    
    context = {'graph': graph}

    return render(request, 'covids/December.html',  context)