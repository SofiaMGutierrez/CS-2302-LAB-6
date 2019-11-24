#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:22:56 2019

@author: sofiagutierrez
"""

# Adjacency matrix representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as g_AL
import graph_EL as g_EL

class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        if self.directed:
            self.am[source][dest] = weight
        else:
            self.am[source][dest] = weight
            self.am[dest][source] = weight
        
    def delete_edge(self,source,dest):
        if not self.directed:
            self.am[source][dest] = -1
            self.am[dest][source] = -1
        else:
            self.am[source][dest] = -1
                
    def display(self):
        print(self.am)

    def draw(self):
        g = self.as_AL()
        g.draw()

    def as_EL(self):
        g = g_EL.Graph(self.am.shape[0], weighted = self.weighted, directed = self.directed)
        if self.directed: 
            for i in range(self.am.shape[0]):
                for j in range(self.am.shape[1]):
                    if self.am[i][j] != -1:
                        g.insert_edge(i, j, self.am[i][j])
                        g.el.sort(key = lambda edge: edge.source)
        else:
            for i in range(self.am.shape[0]):
                for j in range(i, self.am.shape[1]):
                    if self.am[i][j] != -1:
                        g.insert_edge(i, j, self.am[i][j])
        return g

    def as_AM(self):
        return self
    
    def as_AL(self):
        g = g_AL.Graph(self.am.shape[0], weighted = self.weighted, directed = self.directed)
        if self.directed:
            for i in range(self.am.shape[0]):
                for j in range(self.am.shape[1]):
                    if self.am[i][j] != -1:
                        g.insert_edge(i, j, self.am[i][j])
        else:
            for i in range(self.am.shape[0]):
                for j in range(i, self.am.shape[1]):
                    if self.am[i][j] != -1:
                        g.insert_edge(i, j, self.am[i][j])
                        g.insert_edge(j, i, self.am[i][j])
        return g
    
        def breadthFirstSearch(self, start, end):
        frontierQ = [start]
        discoveredSet = [start]
        path = [-1]*16
        while frontierQ:
            vertex = frontierQ.pop(0)
            for i in range(len(self.am[vertex])):
                if self.am[vertex][i] != -1 and i not in discoveredSet:
                    frontierQ.append(i)
                    discoveredSet.append(i)
                    path[i] = vertex
        return path
    
        def depthFirstSearch(self,start,end):
        fronteirStack = [start]
        discoveredSet = [start]
        path = [-1]*16
        while fronteirStack:
            vertex = fronteirStack.pop()
            for i in range(len(self.am[vertex])):
                if self.am[vertex][i] != -1 and i not in discoveredSet:
                    fronteirStack.append(i)
                    discoveredSet.append(i)
                    path[i] = vertex
        return path
'''
if __name__ == "__main__":   
    plt.close("all")   
    g = Graph(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(6,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(6,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g1=g.as_AL()
    g1.draw()
'''