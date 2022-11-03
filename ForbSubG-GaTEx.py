import networkx as nx
import itertools

from tralda.cograph import (to_cotree)

import tralda.tools.GraphTools as gt

__author__ = 'Marc Hellmuth'


P4=nx.Graph()
P4.add_edge('a', 'b')
P4.add_edge('b', 'c')
P4.add_edge('c', 'd')


def findKsubsets(SET,K):
	"""Finds all subsets of SET of size K
    
    Parameters
    ----------
    SET : set
          The set of which size k subsets should be generated
    K 	: int
       	  The size of the subsets to be considered
    
    Returns
    -------
	List of all size K subsets of SET
    """
	return list(itertools.combinations(SET, K))



def findP4(G,CC): 
	"""Checks (brute-force) if there is an induced P4 and, in the affirmative case, 
	   the vertex set U of such a P4 is returned
    
    Parameters
    ----------
    G  : nexworkx.Graph
         A graph.
    CC : nx.connected_components(G)
         A connected component of G
         
    Returns
    -------
	Vertex-set U of an induced P4 in CC if such a P4 exist
    """

	for i in range(len(CC)): 
		SetsOf4 = findKsubsets(CC[i],4)
		for U in SetsOf4:
			testP4 = G.subgraph(U)
			if(nx.is_isomorphic(P4, testP4)): 
				return(U)



def IsPrimitive(G):
	"""Checks (brute-force) if G is primitive or not
    
    Parameters
    ----------
    G  : nexworkx.Graph
         A graph.
         
    Returns
    -------
	True if G is primitive and, otherwise, False
    """

	V_set = set(G.nodes)

	if(bool(to_cotree(G))):
		return False

	N=G.number_of_nodes()
	for k in range(N): 
		if(k>1 and k<N):
			All_k_Subsets = findKsubsets(V_set,k)	
			for M in All_k_Subsets:
				M_outside = V_set - set(M)
				count_valid_z = 0
				for z in M_outside: #for all z outside M check if z is adjacent to all or none 
					count = 0
					for v in M:
						if(G.has_edge(v, z)):
							count += 1
					if(count==0 or count==len(M)):
						count_valid_z += 1
						
				if(count_valid_z == len(M_outside)):
					return False
	return True





def PseudoCographTest(G):
	"""Checks if G Pseudo-cograph or not
	   This is a direct implementation of Alg. 2 in 
	   	From Modular Decomposition Trees to Level-1 networks: 
	   	Pseudo-Cographs, Polar-Cats and Prime Polar-Cats
		M. Hellmuth, G.E. Scholz
		Discr. Appl. Math, 321, 179-219, 2022
    
    Parameters
    ----------
    G  : nexworkx.Graph
         A graph.
         
    Returns
    -------
	True if G is is a pseudo-cograph and, otherwise, False
    """

	V_set = set(G.nodes)
	v_set = {}

	CC = [c for c in sorted(nx.connected_components(G), key=len, reverse=True)]	
	U = findP4(G,CC) 

	for v in U:
		singleton = {v}
		disconnected = False 				
		G1 = G.copy()
		G1.remove_node(v) #G1=G-v
		G2  = nx.complement(G1) #G2=complemtn(G-v)
	
		if(not(nx.is_connected(G1))): 
			H=G1.copy()	
			disconnected = True 				
			CC_H = [c for c in sorted(nx.connected_components(H), key=len, reverse=True)]	 				
		elif(not(nx.is_connected(G2))): 	
			H=G2.copy()	
			disconnected = True 				
			CC_H = [c for c in sorted(nx.connected_components(H), key=len, reverse=True)]	

		
		if(disconnected):
			for j in range(len(CC_H)):
				Isec = CC_H[j].intersection(U) 
				if(len(Isec)>1): #take component that has at least two vertices of a P4
					G1 = G.copy()
					G2 = G.copy()
					C2 = V_set.difference(CC_H[j]) 
					C1 = CC_H[j].union(singleton) 


					H1 = G1.subgraph(C1)
					H2 = G2.subgraph(C2)
					
					if (bool(to_cotree(H1)) and bool(to_cotree(H2))):
						return True
	return False



def FindForbidden(H, G):
	"""Checks (brute-force) if G contains H as an induced subgraph
    
    Parameters
    ----------
    H, G  : nexworkx.Graph
         	Two graph.
         
    Returns
    -------
	True if H is an induced subgraph of H and, otherwise, False
    """

	N=H.number_of_nodes()
	V_set = set(G.nodes)
	for l in range(5,N+1):
		AllSubsets=list(itertools.combinations(V_set, l))
		for W in AllSubsets:
			subG =  G.subgraph(W)
			if(nx.is_isomorphic(H, subG)): 
				return True
	return False			
		




ForbiddenGraphs = []
ForbiddenGraphs_G6 = []


with open("All_Graphs_on_5-8vertices.txt", 'rt') as graph_file:
	"""Checks for every graph in file "All_Graphs_on_5-8vertices.txt"
	   (in G6-format) if this graph is a forbidden subgraph or not 
    
    Parameters
    ----------
    All_Graphs_on_5-8vertices.txt  : graph_file
         							 all graphs of size 5-8
         
    Returns
    -------
	A list of forbidden subgraphs of size 5-8
    """
	for G6 in graph_file:


		G6 = G6.strip()
		graph = nx.from_graph6_bytes(bytes(G6, 'utf8'))
		if(IsPrimitive(graph)):
			if(not(PseudoCographTest(graph))):
				ContainsForbSubgraph = False
	
				for l in range(len(ForbiddenGraphs)):
					if(ForbiddenGraphs[l].number_of_nodes()<graph.number_of_nodes()):
						if(FindForbidden(ForbiddenGraphs[l], graph)):
							ContainsForbSubgraph = True
							l=len(ForbiddenGraphs)+1

				if(not(ContainsForbSubgraph)):
					ForbiddenGraphs.append(graph) 
					ForbiddenGraphs_G6.append(G6) 
	
		
	print(len(ForbiddenGraphs))
	for r in range(len(ForbiddenGraphs)):
		print(ForbiddenGraphs_G6[r])

			

