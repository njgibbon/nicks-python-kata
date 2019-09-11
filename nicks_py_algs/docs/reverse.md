# reverse
Various algorithms to reverse a string in python. 

## resource
### code
### timeit
### tests

Analysis
How would you do it on paper with a small value?
copy out. Bit more memory. 
Or swap around. 

1: traverse backwards and append
Move backwards through a sequence which corresponds with the length of the string and copy the element to the output string.
This means that the output string grows by 1 with each iteration.
Depending on the underlying implementation this could be O(1) making the whole operation t(n*1) or 
to resize the data and append an extra char OR it could take O()
Because strings are immutable in python 

2: traverse forwards and append to front

