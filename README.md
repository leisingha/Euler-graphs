# Euler-graphs 📈
Checks for valid Euler circuits in graphs

The program instantitates graph objects from simple text files that contain directed or undirected adjacency matrix.It then implements Heirholzer's Algorithm to find Euler circuits in each Graph objects using a findEulerH() method.

## Input File Format

The program prompts the user for a commandline input for a filename which includes the adjacency matrix representation of the graph.(*make sure the input files are in the same folder as Test.py*)

* Each graph starts on a new line which contains two elements: 
    - "D" or "U" to specify whether the graph is directed or undirected
    - The number of vertices in that graph
* Followed by one line for each row of the adjacency matrix of the graph: 
    - in each row the elements are separated by blanks.

**Example:**
D 3  
0 1 0   
1 0 0    
0 0 0    

## Test.py

* Does the actual Testing 🧪 using the main function which uses additional helper functions defined locally and imported from other modules.

## Graph.py

* Instantiates list of Graph objects read from a file. (*Superclass for Euler*)

## Euler.py

* Euler objects are Graph objects that contain Euler Circuits
    - They are guaranteed to be connected and all their vertices have even degree

## Walk.py

* Walk objects can be used to build walks from Graphs.
    - A Walk is simply a list of vertices in the order in which they occur in the walk.
    - The edges are not listed.
