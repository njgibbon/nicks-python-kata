# reverse
Various algorithms to reverse a string in python. 

Python doesn't come with any in-built method to reverse a string. So this might actually be handy to know. 

## Resources
### Code
### Tests
### Benchmarks

# Design & Analysis
First we just need to consider the steps to implement the algorithm efficiently in theory. 
A good place to start is to imagine how we could do this manually and methodically with some small input.  
 
A) Read the string backwards and write each character to a new string until we're done. 
O(n) where n is the length of the string because it takes n steps and scales linearly with the size of n. 

TODO: Add image

B) Swap the start (s) and end (e) characters around. Then s+1 and e-1 and so on until your counters meet in the middle and all characters have been swapped.
This is also O(n) because you need to make the same number of moves albeit in a different way. 
There is some additional overhead because *swapping* requires a a temporary variable and you need to check if the counters have met in the middle yet with each cycle. But it's of the same order. 
Also, as the swap is done inline the algorithm takes less space. 

TODO: Add image


1: traverse backwards and append
Move backwards through a sequence which corresponds with the length of the string and copy the element to the output string.
This means that the output string grows by 1 with each iteration.
Depending on the underlying implementation this could be O(1) making the whole operation t(n*1) or 
to resize the data and append an extra char OR it could take O()
Because strings are immutable in python 

2: traverse forwards and append to front

## Benchmarking
For each function I ran a few tests like so:
```
python3 -m timeit --number 100000 --unit usec 'import src.nicks_py_algs.reverse' 'src.nicks_py_algs.reverse.reverse_0("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")'
```
The test returns the average value of the best 5 runs. This gives the algorithm the best change to perform as well as it can on your machine. 
This type of testing is useful to point out significant performance differences.
The time tracked is in micro-seconds 1/1,000,000th of a second. 

<script src="https://gist.github.com/njgibbon/9a58049dac0c1b3ed3a0d96807d7a5cc.js"></script>


