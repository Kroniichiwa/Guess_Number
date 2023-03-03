# Binary search 



 ## How to run

 - Open your terminal where the files are located and type
 ```bash
  Python3 main.py
```
 - Put the number that you're confident in and the program will tell you that it lower or higher!


## How Binary search work?
- First let’s be clear that binary search is only efficient when we have random access. If we have to walk step by step (like a linked list) then a linear search would make more sense. So we know we can make jumps to random points in our search array efficiently. The stride version uses this in it’s idea – let’s make large jumps and only slow the speed as we get closer to our target.
- The search goes through the array from left to right, and the initial jump length is n/2. At each step, the jump length will be halved: first n/4, then n/8, n/16, etc., until finally the length is 1. After the jumps, either the target element has been found or we know that it does not appear in the array
 ## This is what it look like in the easier way
 ![binary search](https://www.topcoder.com/wp-content/uploads/2017/07/binary-search.png)




 

 


## reference 

[Topcoder](https://www.topcoder.com/blog/binary-stride-a-variant-on-binary-search/

