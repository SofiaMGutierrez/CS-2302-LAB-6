#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:33:13 2019

@author: sofiagutierrez
"""

# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as g_AL
import graph_AM as g_AM

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        temp_edge = Edge(source, dest, weight)
        match = False
        if self.directed:
            for edge in self.el:
                if (edge.source == temp_edge.source and edge.dest == temp_edge.dest):
                    match = True
                    break
            if not match:
                self.el.append(temp_edge)
                self.el.sort(key = lambda edge: edge.source)
            
        else:
            for edge in self.el:
                if (edge.source == temp_edge.source and edge.dest == temp_edge.dest) or (edge.source == temp_edge.dest and edge.dest == temp_edge.source):
                    match = True
                    break
            if not match:
                self.el.append(temp_edge)
                self.el.sort(key = lambda edge: edge.source)
    
    def delete_edge(self,source,dest):
        counter = 0
        if self.directed:
            for edge in self.el:
                if edge.source == source and edge.dest == dest:
                    break
                counter += 1
        else:
            for edge in self.el:
                if (edge.source == source and edge.dest == dest) or (edge.source == dest and edge.dest == source):
                    break
                counter += 1
        del self.el[counter]
                
    def display(self):
        print('[', end = '')
        for e in self.el:
            print('(',e.source, ',', e.dest, ',', e.weight, ')', end = '')
        print(']')
     
    def draw(self):
        adjlist = self.as_AL()
        
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(adjlist.al)):
            for edge in adjlist.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
            
    def as_EL(self):
        return self
    
    def as_AM(self):
        g = g_AM.Graph(self.vertices, self.weighted, self.directed)
        for edge in self.el:
            g.insert_edge(edge.source, edge.dest, edge.weight)
        return g
    
    def as_AL(self):
        g = g_AL.Graph(self.vertices, self.weighted, self.directed)
        for edge in self.el:
            g.insert_edge(edge.source, edge.dest, edge.weight)
        return g
    
        def breadthFirstSearch(self, start, end):
        frontierQ = [start]
        discoveredSet = [start]
        path = [-1]*16
        while frontierQ:
            vertex = frontierQ.pop(0)
            for edge in self.el:
                if edge.source == vertex and edge.dest not in discoveredSet:
                    frontierQ.append(edge.dest)
                    discoveredSet.append(edge.dest)
                    path[edge.dest] = edge.source 
        return path
    
        def depthFirstSearch(self,start,end):
        fronteirStack = [start]
        discoveredSet = [start]
        path = [-1]*16
        while fronteirStack:
            vertex = fronteirStack.pop()
            for edge in self.el:
                if edge.source == vertex and edge.dest not in discoveredSet:
                    fronteirStack.append(edge.dest)
                    discoveredSet.append(edge.dest)
                    path[edge.dest] = edge.source 
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