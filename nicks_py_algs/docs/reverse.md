# reverse
Various algorithms to reverse a string in python. 

Python doesn't come with any in-built method to reverse a string. So this might actually be handy to know. 

## Resources
### Code
https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/src/nicks_py_algs/reverse.py
### Tests
https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/tests/test_reverse.py
### Benchmarks
https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/benchmarking/timeit_reverse.sh

# Design
First we just need to consider the steps to implement the algorithm efficiently in theory. A good place to start is to imagine how we could do this manually and methodically with some small input.  

**A)** Read the string backwards and write each character to a new string until we're done. This runs in O(n) where n is the length of the string because it takes n steps and scales linearly with the size of n. 

![reverse traverse](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/hello-traverse-reverse.png)

**B)** Swap the start (s) and end (e) characters around. Then s+1 and e-1 and so on until your counters meet in the middle and all characters have been swapped.
This is also O(n) because you need to make the same number of moves albeit in a different way. There is some additional overhead because *swapping* requires a temporary variable and you need to check if the counters have met in the middle yet with each cycle. But it's of the same order. Also, as the swap is done inline the algorithm takes less space. 

![reverse swap](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/hello-inline-reverse.png)

## Implementation

**Traverse backwards**

Calculate the length of the input string. Use this to loop backwards and append each char to a new string. The complexity of the appending operation depends on the underlying implementation in the interpreter. Because Python strings are immutable it is likely that each `reversed_output = reversed_output + s[i]` takes the current state of the output string and the new character and copies them to a new variable. This is not linear as it follows the pattern 1 + 2 + 3 ... + n.
t(n(n+1)/2) and so it is of the order n^2. For this reason it is expected this algorithm will run slower than the rest.   

**Traverse forwards and append to front**

With this function we traverse the string normally as it is iterable. And with each iteration we append the new character to the front of the output string. This is expected to have a similar running time of the first algorithm for the same reason.   

**Swap in 'list' and 'join'**

This is an implementation of the inline swapping algorithm. We need to create a list object with the string so that we can swap inline as lists are mutable. The 'join' operation solves the appending problem efficiently unlike the first two algorithms.  

**'List' 'reverse' and 'join'**

This is a built in inline list reverse function so it is expected to be similar and likely a bit better in running time than our new swap function.  

**'Reversed' and 'join'**

By passing a string to 'reversed' an iterator is returned which is set to go through the list in reverse. Where 'next' counts down instead of up. And this can be passed straight to the 'join' operation. This is expected to have good performance. 

**Slice**

To my knowledge slice will take a sub-list of a list and copy it to a new space. Expected to have similar good performance.  

## Benchmarking
For each function I ran a few tests like so:
```
python3 -m timeit --number 1000 --unit usec 'import src.nicks_py_algs.reverse' 'src.nicks_py_algs.reverse.reverse_0("abcdefghijklmnopqrstuvwxyz")'
```
But I set the input string to a length of 10,000.  
The test returns the average value of the best 5 runs. This gives the algorithm the best chance to perform as well as it can on your machine. This type of testing is useful to point out significant performance differences. The time tracked is in microseconds (1/1,000,000th of a second).  

![reverse benchmark table](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/reverse_benchmark_table.png)

![reverse_0](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/reverse_0_bench.png)
![reverse_1](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/reverse_1_bench.png)
![reverse_2](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/reverse_2_bench.png)
![reverse_3](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/reverse_3_bench.png)
![reverse_4](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/reverse_4_bench.png)
![reverse_5](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/reverse_5_bench.png)

### Thoughts
As expected the first functions performed worst. It is interesting how much worse the 'forward traverse' did because they are so similar. Perhaps `reversed_output = reversed_output + s[i]` ends up being quicker than `reversed_output = c + reversed_output` for some reason.  

It is interesting that my inline swap function was 6x~ slower than the built-in 'reversed' function because they are expected to be doing the same thing. Both should deal the same additional overhead described in the design section. When checking the underlying implementation the function is very similar (just in 'while' form). I guess 2 key differences is that this loop seems to be passing pointers around and not doing actual copies which my implementation is probably doing. And secondly, the whole operation is in C which means it will be inherently faster. 

![cpython_reverse](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/cpython_reverse.png)

https://github.com/python/cpython/blob/master/Objects/listobject.c  

Finally, it is clear that slicing is by far the fastest, but why exactly? It could be, again, that the whole operation is in C and there is no additional 'join' step. The underlying implementation doesn't seem to be doing anything special - just looping to copy into another list. 

![cpython_slice](https://github.com/njgibbon/nicks-python-kata/blob/master/nicks_py_algs/images/cpython_slice.png)  

It could be interesting to manufacture more tests to isolate the reasons. Checking with different python compilers / interpreters would be useful. 


## Key takeaways
• Slicing is the most efficient way to reverse a string in python.   
• 'Reverse' to swap inline and 'reversed' for a copy perform well and are clearer. 
• String concatenation as implemented in the slower algorithms should be avoided.    
• Benchmarking is useful to see things we can't concretely detect otherwise. 
• Code runs fast - the slowest implementation was still only around 1 1,000th of a second. 

## Resources

https://www.python.org/dev/peps/pep-0322/  

https://waymoot.org/home/python_string/  

https://www.journaldev.com/23647/python-reverse-string  

https://www.quora.com/How-is-slicing-implemented-in-python  
