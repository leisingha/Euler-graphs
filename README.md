# Euler-graphs 📈
Checks for valid Euler circuits in graphs

The program instantitates graph objects from simple text files that contain directed or undirected adjacency matrix.It then implements Heirholzer's Algorithm to find Euler circuits in each Graph objects using a findEulerH() method.

## Input File Format

* Each graph starts on a new line which contains two elements: 
    - "D" or "U" to specify whether the graph is directed or undirected
    - The number of vertices in that graph
* Followed by one line for each row of the adjacency matrix of the graph: 
    -in each row the elements are separated by blanks.

