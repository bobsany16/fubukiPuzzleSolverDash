# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:37:26 2019
This program implements the Fubuki Solver as a Dash App for better User Interface and Interaction
@author: Bobby Nguyen
"""

from flask import Flask
server = Flask('myapp')

# ***

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from itertools import permutations
from dash.dependencies import Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background' : '#81ecec',
    'text': 'black'
}

app.layout = html.Div(style={'backgroundColor': colors['background'], 
                             'display': 'flex', 
                             'height': '150%',
                             'columnCount': 2,
                             'padding': 0,
                             'margin': 0}, children=[
    html.Div(style={'color': colors['text'], 'width': '35%'}, children=[
        html.H2('FUBUKI SOLVER', style={'textDecoration': 'underline', 
                                        'letterSpacing': '5px',
                                        'textAlign': 'center',
                                        'fontWeight': 'bold'}),
        html.P(children='''
        Fubuki: a quick and easy solver for the Fubuki Puzzle
        Instructions: 
            Place the number 1 to 9 in the 3 by 3 grid 
            so that each horizontal and vertical 
            line adds up to the given sum. 
            You can only use each number once. 
            R and C values are already given. 
        ''', 
        style={
            'fontStyle' : 'italic',
            'color': colors['text'],
        }
        ),
        html.Div(style={ 'height': '75%', 'fontWeight': 'bold', 'display': 'grid'}, children = [
                html.P('Please select position:'),
                dcc.Dropdown(
                        id='selected_pos',
                        options=[
                                {'label' : 'a1', 'value' : 0},
                                {'label' : 'a2', 'value' : 1},
                                {'label' : 'a3', 'value' : 2},
                                {'label' : 'a4', 'value' : 3},
                                {'label' : 'a5', 'value' : 4},
                                {'label' : 'a6', 'value' : 5},
                                {'label' : 'a7', 'value' : 6},
                                {'label' : 'a8', 'value' : 7},
                                {'label' : 'a9', 'value' : 8},],
                        value = 4
                ),
                html.P('Please select value for position chosen:'),
                dcc.Slider(
                    id='val_slider', 
                    min=1,
                    max=9,
                    step = 1,
                    value = 2,
                    marks={
                        1: '1',
                        2: '2',
                        3: '3',
                        4: '4',
                        5: '5',
                        6: '6',
                        7: '7',
                        8: '8',
                        9: '9'}
                ),
                html.Div(style = {'margin-top': '25px', 'display': 'grid'} ,children = [
                    html.P('Please fill in prefilled R and C values:'),
                    html.P('R1 value:'),
                    dcc.Input(id='r1Val', type='number', value=17),
                    html.P('R2 value:'),
                    dcc.Input(id='r2Val', type='number', value=15),
                    html.P('R3 value:'),
                    dcc.Input(id='r3Val', type='number', value=13),
                    html.P('C1 value:'),
                    dcc.Input(id='c1Val', type='number', value=16),
                    html.P('C2 value:'),
                    dcc.Input(id='c2Val', type='number', value=11),
                    html.P('C3 value:'),
                    dcc.Input(id='c3Val', type='number', value=18)]),
                html.Button(id='submit-button', n_clicks=0, children='Submit', 
                            style={'margin-top': '15px', 'fontWeight': 'bold'}),
        ])
    ]),
    html.P(children=[
                html.H2('OUTPUT IS: ', style={'letterSpacing': '5px', 
                                              'fontWeight': 'bold', 
                                              'textDecoration': 'underline'}),
                html.P(id ='result-output', style={'text-align': 'center'})],
            style={'margin-left': '325px',
                   'width': '50%'})
])
@app.callback(
    Output('result-output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('selected_pos', 'value'),
     State('val_slider', 'value'),
     State('r1Val', 'value'),
     State('r2Val', 'value'),
     State('r3Val', 'value'),
     State('c1Val', 'value'),
     State('c2Val', 'value'),
     State('c3Val', 'value')]
)
def fubukiSolver (n_clicks,position, posValue, r1, r2, r3, c1, c2, c3):
    '''
    Function to solve fubuki puzzle by checking prefilled values with the 
    combined values of each permutations. Brute-force approach.
    
    @param n_clicks the click amount for Button that when user hits the button, @callback is fired. 
    @param position the position on the puzzle user want to set value
    @param posValu the value for the defined position
    @param r1-r3 R1 through R3 values defined by user
    @param c1-c3 C1 through C3 values defined by user
    '''
    resOut =[]
    n = 0 #to count number of solutions
    myList = np.arange(1,10, dtype=int) #Create a list from 1 - 9 of type int
    newList = np.delete(myList, np.where(myList==posValue)) #delete the prefilled value and its position given by user
    permList = permutations(newList)#to calculate all permutations for 9 numbers
    myPrefilledVals = np.array([r1, r2, r3, c1, c2, c3]) #put all the user-filled values into an array
    
    #iterate through all permutations to make comparisons
    for orderList in permList:
        orderList = np.insert(orderList, position, posValue)
        row1 = sum(orderList[0:3])
        row2 = sum(orderList[3:6])
        row3 = sum(orderList[6:9])
        col1 = orderList[0] + orderList[3] + orderList[6]
        col2 = orderList[1] + orderList[4] + orderList[7]
        col3 = orderList[2] + orderList[5] + orderList[8]
        #put all combinations into an array
        solution = np.array([row1,row2,row3,col1,col2,col3])
        '''Condition to check if solution matches the prefilledVals
            If it does, n increments and resOut append its solution'''
        if(solution==myPrefilledVals).all():
            n=n+1
            resOut.append(orderList[0:3])
            resOut.append(orderList[3:6])
            resOut.append(orderList[6:9])
    
    myResults = np.array(resOut)
    ##Create a pandas DataFrame to be input into html.Table() later on        
    dataframe = pd.DataFrame(myResults, 
                             columns=['C1', 'C2', 'C3'],
                             index= ['R{0}'.format(i) for i in range(1, len(resOut)+1)])
    '''To check: if there are solutions, then table will be generated, 
        Otherwise, return there is no result'''
    if n>0:
        
        for i in range(n):
            return html.Table(
        # Header
                [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
                [html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                        ]) for i in range(min(len(dataframe), len(dataframe)))]
                        )
    else:
        return 'There is no solution'   
   ###return '\n'.join(map(str,resOut))
   ###return pd.DataFrame(data)   
   ###return pd.Series(orderList[0:3])

if __name__== '__main__':
    #app.server.run()
   app.run_server(debug=True, port=3004)
   
   ''' Idea is to join the rows into a single string then output them in a formatted output''' 
   ''' Use join to do this but then how to return it from the function'''

