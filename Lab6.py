#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:21:05 2019
Course: CS 2302
Author: Sofia Gutierrez
Lab #6: The purpose of this lab is to build,
modify, and display graphs using adjacency list,
adjacency matrix, and edge list. These functions
were then used to solve a riddle with the help of
Breadth-first-search and Depth-first-search
Instructor: Olac Fuentes
T.A.: Anindita Nath
"""
import graph_AL as AL_graph
import graph_AM as AM_graph
import graph_EL as EL_graph

def build_graph():
    weighted = False
    directed = False
    
    AL = AL_graph.Graph(16, weighted, directed)
    AL.insert_edge(0, 5)
    AL.insert_edge(2, 11)
    AL.insert_edge(2, 7)
    AL.insert_edge(4, 5)
    AL.insert_edge(4, 7)
    AL.insert_edge(4, 13)
    AL.insert_edge(8, 11)
    AL.insert_edge(8, 13)
    AL.insert_edge(10, 11)
    AL.insert_edge(10, 15)
    
    # build adjacency matrix and edge list
    AM = AL.as_AM()
    EL = AL.as_EL()
    
    return AL, AM, EL

def graphs(AL, AM, EL):
    AL.draw()
    AM.draw()
    EL.draw()
    
if __name__ == "__main__":
    
    AL, AM, EL = build_graph()
    
    ########## Adjacency list ##########
    #Depth-first-search
    print("Adjancency List Depth First:")
    print(AL.DFS(0, 15))
    AL.printDFS(0, 15)
    #Breadth-first-search
    print("Adjacency List Breadth First:")
    print(AL.BFS(0, 15))
    AL.printBFS(0, 15)
    
    print()

    ########## Adjacency Matrix ##########
    #Depth-first-search
    print("Adjancency Matrix Depth First:")
    print(AM.DFS(0, 15))
    AM.printDFS(0, 15)
    #Breadth-first-search
    print("Adjacency Matrix Breadth First:")
    print(AM.BFS(0, 15))
    AM.printBFS(0, 15)
    
    print()
    
    ########## Edge List ##########
    #Depth-first-search
    print("Edge List Depth First:")
    print(EL.DFS(0, 15))
    EL.printDFS(0, 15)
    #Breadth-first-search
    print("Edge List Breadth First:")
    print(EL.BFS(0, 15))
    EL.printBFS(0, 15)