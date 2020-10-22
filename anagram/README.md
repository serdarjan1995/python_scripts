**Question**

An anagram is a word or phrase formed by rearranging the letters of
a different word or phrase. In other words, both strings must contain
the same exact letters in the same exact frequency.

Write a python script that reads 2 strings from command line and finds
out whether they are anagrams or not.
If they are not anagrams, then the script should find and print the
minimum number of character deletions required to make the two strings
anagrams. Otherwise, just print that they are anagrams.

**Input Format**

- The first line contains a single string, **a**.
- The second line contains a single string, **b**.

Expected input and output:
```
$ python3 solution.py
a: Tom Marvolo Riddle
b: I Am Lord Voldemort
remove 7 characters from 'Tom Marvolo Riddle' and 8 characters from 'I Am Lord Voldemort'

$ python3 solution.py
a: tom marvolo riddle
b: i am lord voldemort
remove 0 characters from 'tom marvolo riddle' and 1 characters from 'i am lord voldemort'

$ python3 solution.py
a: tom marvolo riddle
b: i am lordvoldemort
they are anagrams

$ python3 solution.py
a: tom riddle
b: voldemort
remove 3 characters from 'tom riddle' and 2 characters from 'voldemort'
```
