# ForbiddenSubgraphs-GaTEx

[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Python program to find all forbidden subgraphs of graphs that can be explained by 0/1 labeled galled trees.

## Installation

The program requires Python 3.7 or higher.

#### Dependencies

* [NetworkX](https://networkx.github.io/)
* [tralda](https://github.com/david-schaller/tralda)

## Usage and description

This program takes as input an order list of all graphs of size 5, 6, 7, to K vertices and verifies if any of these graphs is a forbidden subgraph of a galled-tree explainable graph. 

Note that this program is part of a computer-assisted proof. In particular, the computed forbidden subgraphs form the base case of an induction proof to show that these forbidden subgraphs characterize graphs that can be explained by 0/1-labeled galled trees (gatex graphs) and thus, generalize the class of cographs. In order to make it as easy as possible for the reader to verify this implementation correcty computes these subgraphs we refer to Alg. 1 in [1] and argue that Alg. 1 is implemented to be readable as easy as possible and, thus, mainly brute-force routines are used, although such a simplified implementation goes hand in hand with a possibly lower runtime.


## Citation and references

If you use `ForbiddenSubgraphs-GaTEx` in your project or code from it, please consider citing:

*[1] **M. Hellmuth, G.E. Scholz (2022) Resolving Prime Modules: The Structure of Pseudo-cographs and Galled-Tree Explainable Graphs (arXiv)**

*[2] **M. Hellmuth, G.E. Scholz (2022) From Modular Decomposition Trees to Level-1 networks: Pseudo-Cographs, Polar-Cats and Prime Polar-Cats, 		Discr. Appl. Math, 321, 179-219**

Please report any bugs and questions in the [Issues](https://github.com/marc-hellmuth/ForbiddenSubgraphs-GaTEx/issues) section.


		

