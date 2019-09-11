# nicks_py_algs
Algorithms in python. 

• Implementing various algorithms in various sensible ways - including whatever is deemed to be the best.  
• Analysing the complexity and benchmarking to find the best implementation.  
• All whilst using (give or take) good engineering standards.  

## Docs
See the docs folder for analysis on notes per module and otherwise.

## Dev
### Venv & Dependencies
Set up and activate Env:
```
python3 -m venv venv
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Deactivate venv:
```
deactivate
```
### Testing
Run all:
```
python3 -m unittest discover -s tests
```
Run specifc:
```
#e.g
python3 -m unittest tests.test_reverse
```
### Benchmarking
Benchmark a function example:
```
#take a line from the /benchmarking folder
#e.g
python3 -m timeit --number 100000 --unit usec 'import src.nicks_py_algs.reverse' 'src.nicks_py_algs.reverse.reverse_0("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")'
```



