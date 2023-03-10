from Graph import Graph
from Euler import Euler
from Walk import Walk
import os

def main():
  """
  Main test program checks for a Euler circuit in a graph object.
  Hierholzer's algorithm is tested on graphs in test files
  """
  #dirPath = "/Users/leisingha/Github/Euler-graphs" #Using absolute path for my local repo 😝
  
  current_directory = os.getcwd()

  inputfile = str(input("Enter file name:\n "))

  inputfile = "/" + inputfile
  
  # Run test files to check for Euler Circuits
  print("\n=======================  RESULT  =======================\n")
  
  testInput(current_directory + inputfile)
  
  print("~ End of Program ~")

 

def testInput(filename):
  """
  Reads graphs from a file and tests the getEuler method on these graphs.
  
  Parameters:
    str filename: path of file
    int expected: number of graphs in file which have an Euler circult
  
  Returns the number of valid Euler circuits for the graphs in the file.
  """
  print("\n-------  Test " + filename +"  -------\n")
  found = 0
  graphList = Euler.fromFile(filename)
  for graph in graphList:
    found += testOnGraph(graph)
  print("Euler circuits " + "found: " + str(found))
  return found
  
def testOnGraph(graph):
  """
  Tests the getEuler method for a graph.  Prints the results.
  
  Parameters:
    Euler graph: Euler graph on which the getEulerH method will be tested
  
  Returns 1 if a valid Euler circuit has been found and 0 otherwise
  """
  print("Graph has " + str(graph.totalVertices())
			 + " vertices, and " + str(graph.totalEdges()) + " edges.") 
  circuit = graph.findEulerH()

  # Note that the first case should never happen because all Euler objects have Euler circuits
  if(circuit is None):
    print("Graph has no Euler Circuit")
    return 0
  elif (isValidEuler(graph,circuit)):
    print("Valid Euler Circuit")
    return 1
  else:
    print("Invalid Euler Circuit")
    return 0


def isValidEuler(graph, circuit):
  """
  Verifies whether a walk is a valid Euler circuit for a graph.
  
  Parameters:
    Graph graph: original graph
    Walk circuit: potential Euler circuit for graph
  
  Returns True iff circuit is a valid Euler circuit for graph.
  """

  # First check if the path is a circuit
  if not circuit.isCircuit():
    print("Error: Path returned is not a circuit")
    return False

  # Then check if the circuit has the correct number of edges
  circuitLength = circuit.length()
  totalEdges = graph.totalEdges()
  if circuitLength < totalEdges:
    print("Error: Some edges have not been visited")
    return False
  if circuitLength > totalEdges:
    print("Error: Too many edges in circuit")
    return False

  # Now traverse the circuit to verify that it is a correct Euler circuit for this graph
  edges = graph.getEdges()
  path = circuit.getVertices()
  v1 = path[0]
  for i in range(1,circuitLength):
    v2 = path[i]
    if edges[v1][v2] == 0:
      print("Error: The graph does not have enough edges between " + str(v1) + " and" + str(v2) + " to support the circuit found.")
      return False
    edges[v1][v2]-=1
    edges[v2][v1]-=1
    v1 = v2
  
  return True

# calls main program
if __name__ == '__main__':
  main()
