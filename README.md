# dollarpy

dollarpy is a python implementation of the $P Point-Cloud Recognizer.(link to the paper: http://depts.washington.edu/madlab/proj/dollar/pdollar.html)

The $P Point-Cloud Recognizer is a 2-D gesture recognizer designed for rapid prototyping of gesture-based user interfaces. In machine learning terms, $P is an instance-based nearest-neighbor classifier with a Euclidean scoring function, i.e., a geometric template matcher.

$P is the latest in the dollar family of recognizers that includes $1 for unistrokes and $N for multistrokes. Although about half of $P’s code is from $1, unlike both $1 and $N, $P does not represent gestures as ordered series of points (i.e., strokes), but as unordered point-clouds. By representing gestures as point-clouds, $P can handle both unistrokes and multistrokes equivalently and without the combinatoric overhead of $N. When comparing two point-clouds, $P solves the classic assignment problem between two bipartite graphs using an approximation of the Hungarian algorithm.

## Installation
*dollarpy* can be installed using pip:

```
pip install dollarpy
```

## Usage
pdollar - this prints the help menu
pdollar -r - this removes all the files from templates folder
pdollar -t <file-path> - this inserts the file in the template folder
pdollar -i <eventfile> - Prints the name of gesture file as they are recognized from the event stream from the template folder in the format (matched_filename, 1.0) (unmatched_filename, 0.0)

Since, I made the project in Python it doesn’t need any makefile to build the project

It works without .py as I have created a local alias, to make it run in the same format we have to make a alias using the given below code: 

Richas-MacBook-Pro:~ richasikri$ echo "alias pdollar='/Users/richasikri/Downloads/dollarpy/pdollar.py'" 
Richas-MacBook-Pro:~ richasikri$ source ~/.bash_profile

If not making a local alias we can run using the following commands:
./pdollar.py
./pdollar.py -r 
./pdollar.py -t <file-path> 
./pdollar.py -i <eventfile>

