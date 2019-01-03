# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/sudoku#pythonbytes-project-in-depth)


This page tells you how to do this project. You do not have to read it! You can simply start working on the
project according to your thoughts. 


## Overview


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/sudoku/sudoku2.png" alt="drawing" width="300"/>


These project notes are currently in development. You are welcome to read through here but 
not everything is complete and tested! My sudoku program does not work yet, for example.


To get started on this we use a strategy called *recursion*. You may want to say to yourself
'I need to understand recursion' before going further. That way when you run into recursion 
you will be prepared for the awesomeness. Also you can look up recursion in the dictionary:


> recursion (noun): See *recursion*


Incidentally there are a number of styles of puzzle similar to Sudoku; such as Shikaku and Nurikabe. 
If you create a Sudoku solver you have the opportunity to go further into these other games. 


## Details

We proceed in three parts here. First read the notes on *recursion* at the 
[knight's tour project page](https://github.com/robfatland/pythonbytes/tree/master/projects/knight#recursion).
This gives some simple exercises for you to try that use recursion.


Second we describe Sudoku here on this page from a Python programmer's perspective. 
This sets us up with a computer programmer's frame of mind. We break the Sudoku solver into 
small steps on the path to success.


Third we will go from our thinking framework to code that solves a Sudoku puzzle. 


## Part 1: Understanding recursion


Go to [this link](https://github.com/robfatland/pythonbytes/tree/master/projects/knight#recursion)
and learn about recursion. Don't forget to do the exercises!


## Part 2: A programmer's approach to a Sudoku puzzle


Attribution: This description follows closely the ideas of Jake VanderPlas' 
[article on Sudoku solvers](http://jakevdp.github.io/blog/2013/04/15/code-golf-in-python-sudoku/).
Jake uses Python **sets** but we will stick to using **lists**. 


All Sudoku puzzles have a starting point. The most basic would be an empty puzzle: Simple 9 x 9 
empty **cells**. This has many solutions! But all the Sudoku puzzles you will find (say in the newspaper)
have some numbers filled in. With 81 cells in the puzzle we can
write it out as 81 **characters** where we use a zero **0** for the empty cells.
For example this puzzle: 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/sudoku/sudoku2.png" alt="drawing" width="300"/>


Translates to these characters ```060000008201800500905002000000704602300090005504608000000900301007005906100000050```.
I made this by reading from top to bottom, left to right for each row, writing a zero for empty cells. However as you
will read below we will not use a *string* type for this in our Python program. Strings are too static, too difficult
to modify; so we will use something more flexible.


Guessing answers to the entire puzzle would prove... time consuming. Instead we describe here an approach
of just guessing one cell at a time to sneak up on the solution. This will be much like solving a maze where
you take only one step at a time... and if you discover you have gone down a blind alley you back up and choose
a  new path.


An open cell can have any of nine values in the solution; but in fact some of these are eliminated by the rules. 
That is: The rules of Sudoku permit us to make these guesses for each cell for only *allowed* choices. 


The nice thing about using Python is that the program keeps track of everything.
Therefore for a celebratory moment: Not only are we capable of imagining 
such a difficult puzzle to solve; we can also come up with an efficient way 
to solve it and use the structure of the computer to do the tedious work...
very quickly.


##### **Representing the Sudoku puzzle**


A Sudoku puzzle is 9 x 9 cells or 81 cells. Therefore we could represent a puzzle using
a string of 81 characters. In Python strings are a **type** of variable; but they are difficult 
to change... 
We can only change strings by building new strings from them which is slow and klunky. 
The thing in Python that is easy to change is called a **list**.  Therefore let's 
use a string to describe the Sudoku puzzle at the start; and then let's convert this string into lists that we 
can work with. 

Our first puzzle we have as a string already:


```
p1 = '060000008201800500905002000000704602300090005504608000000900301007005906100000050'
```


Here just to check our skill a little further is another puzzle.


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/sudoku/sudoku.png" alt="drawing" width="300"/>



Here is the same thing in written characters with periods ```.``` for empty cells; and these become zero characters ```0```.


```
..86324..                                       008632400
.4.....1.                                       040000010
5..9.4..6   --------------------------------->  500904006
8.......5                                       800000005
6.......4            zeros for blanks           600000004
1.7...9.2                                       107000902
4..751..3   --------------------------------->  400751003
.6.....2.                                       060000020
..58267..                                       005826700
```


And we connect them all together in a single string to represent the Sudoku puzzle:

```
p2 = '008632400040000010500904006800000005600000004107000902400751003060000020005826700'
```

To start with we just refer to the first puzzle, written above as string ```p1```.


#### Sudoku rules


Each zero in the puzzle string must be converted to a number from 1 to 9 according to
the three rules of Sudoku


* No number may repeat on any row
* No number may repeat on any column
* No number may repeat in any block


There are nine **3 x 3** blocks as you can see in both of the above puzzle images. Each block is **3 x 3** cells.


#### First key idea of writing a Sudoku solver


The cells can be numbered in Python fashion from 0 to 80 (as there are 81 of them). 
However each cell has a unique (row, column) address. 
The upper left cell is (0, 0) and has index 0.
The lower right cell is (8, 8) and has index 80. 
The center cell is (4, 4) and has index 40.
The lower left cell is (0, 8) and has index 72.


#### Second key idea of writing a Sudoku solver


An empty cell in the puzzle string is a '0' zero character. This is fine but
it does not give us information about what *could* be written in that cell. 
So when we get to the business of solving the puzzle let us instead represent an empty 
cell of the puzzle as a **list** of possible numbers that could
be written in that cell according to the three Sudoku rules. 


For example cell (0, 0) of the first puzzle **p1** could have any of the nine digits so we make this list:


```['1', '2', '3', '4', '5', '6', '7', '8', '9']```


However the rules of Sudoku tell us some of these are forbidden: 
* 1, 2, 5, 6, 9 from the cell block numbers in the puzzle
* 1, 2, 3, 5, 9 from the column
* 6, 8 from the row


The correct list of possible values is therefore: 


```['4', '7', '8']```


#### Third key idea of writing a Sudoku solver


This is the last bit of bookkeeping: Every cell has its own set of *related* cells per
the rules. These are the cells in the same *row* as that cell, in the same *column* as 
that cell, and in the same *block* as that cell. 


## Part 3: Converting ideas to Python code


* add guess g to cell index n in puzzle p by creating a new string pn = p[:n] + g + p[n+1:]
  * check this with code!













