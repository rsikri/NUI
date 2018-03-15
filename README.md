# dollarpy



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

