#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:21:05 2019

@author: sofiagutierrez
"""

import matplotlib.pyplot as plt
import numpy as np
import graph_AL as g_AL
import graph_AM as g_AM 
import graph_EL as g_EL
import time


def build_graph():
    
    AL_graph = g_AL.Graph(16)
    
    AL_graph.insert_edge(0,5)
    AL_graph.insert_edge(2,7)
    AL_graph.insert_edge(2,11)
    AL_graph.insert_edge(4,5)
    AL_graph.insert_edge(4,7)
    AL_graph.insert_edge(4,13)
    AL_graph.insert_edge(8,11)
    AL_graph.insert_edge(8,13)
    AL_graph.insert_edge(10,11)
    AL_graph.insert_edge(10,15)
    
    AL.as_AM()
    
    return AL, AM, EL

def drawGraphs():
	AL, AM, EL = buildGraphs()
	AL.draw()
	AM.draw()
	EL.draw()

if __name__ == '__main__':
    AL, AM, EL = build_graph()
    AL.draw()
    AM.draw()
    EL.draw()
    
    AL, AM, EL = buildGraphs()
	
	print("AL: breadth First Search")
	print(AL.breadthFirstSearch(0,15))
	AL.printBreadthPath(0,15)
	print("AL: Depth First Search")
	print(AL.depthFirstSearch(0,15))
	AL.printDepthPath(0,15)
	print()
	

	print("AM: breadth First Search")
	print(AM.breadthFirstSearch(0,15))
	AM.printBreadthPath(0,15)
	print("AM: Depth First Search")
	print(AM.depthFirstSearch(0,15))	
	AM.printDepthPath(0,15)
	print()


	print("EL: breadth First Search")
	print(EL.breadthFirstSearch(0,15))
	EL.printBreadthPath(0,15)
	print("EL: Depth First Search")
	print(EL.depthFirstSearch(0,15))	
	EL.printDepthPath(0,15)	
	print()