# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/sudoku)


### Overview

Text

### Details

We proceed in two parts. The first part lays out the basics of how to think about a Sudoku puzzle
in Python code. The second part gives some very specific hints that will enable you to build a 
Sudoku solver. We leave it to you to balance doing it on your own versus peeking at the hints!


#### Part 1: Setting up the Sudoku puzzle


One way to do this project is in terms of 'questions' that come up when we break down the problem.


The first question is how to represent the puzzle in Python code. Since a Sudoku puzzle is 9 x 9 
cells we can use a string of 81 characters. Each of these 81 characters corresponds to a different
cell in the puzzle. The characters 1, 2, 3, 4, 5, 6, 7, 8, 9 represent those 
numbers; and we are usually given some of them as the starting point of the puzzle. We can use a 
space character ' ' to represent an un-solved or empty cell. If we write a good solver we could test 
it by giving it a string of 81 spaces representing a completely empty Sudoko puzzle to solve and 
it will find a solution. 


The rules of Sudoku require us to precisely satisfy three conditions on the number in each cell..


- The number must not duplicate any other cell in its row
- The number must not duplicate any other cell in its column
- The number must not duplicate any other cell in its 3 x 3 cell block


This suggests that cell locations are important for the purpose of comparison with other cells. 
The next question is therefore how to convert a puzzle location or index in the string p into a 
cell address that can be used for comparisons. Here is an example Sudoku puzzle for reference 
where only the first six cells are filled, the rest are empty except the last cell:


```
p = '798512                                                                          3'
```

That is: p is a string of 81 characters corresponding to the 81 Sudoku cells; and values
are provided for only 7 of those cells. The rest are empty. 


We can index each cell location. For example p[0] = '7', p[1] = '9', p[2] = '8' and so 
on. Those indexes are 0, 1 and 2. Most of the cells are empty so for example p[43] = ' '. 
The very last cell (since we begin numbering at 0) has cell index 80, where p[80] = '3'. 


Here is the corresponding Sudoku puzzle in its proper format:


```
 7 | 9 | 8 | 5 | 1 | 2 |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   |   |
 -----------------------------------
   |   |   |   |   |   |   |   | 3 |
```


If we number the rows from the top down as 0, 1, 2, 3, 4, 5, 6, 7, 8 and the columns from 
left to right as 0, 1, 2, 3, 4, 5, 6, 7, 8 then each cell has an address given by two 
numbers. For example the upper left cell containing the '7' is at location (0, 0) and 
the 2 is at address (0,5). The '3' in the lower right corner is at address (8, 8).  Notice
that by starting the numbering at 0 instead of 1 we are being *Pythonic*: We are thinking
like Python programmers.


We now have two ways to refer to cell values: In string p using a single index from 0 to 81
and in our puzzle using a two number address like (7,3). How do we convert from one to the
other and back again?  We could imagine two functions that accomplish these two tasks:

```
def CellToAddress(c):
    row = 3
    col = 4
    return (row, col)

def AddressToCell(row, col)
    cell = row*9 + col
    return cell
```


One of those two functions is correct and the other one is incorrect. (Which is which?) Notice
that I am using the Python **tuple** in the first function to return an address (row, col). This 
part is correct... but sadly this function will always return row 3 column 4 regardless of what 
cell index it is given. So that needs some work. 


Once we can convert from cell number to address and back again we reach our third question:
How can we implement the rules of Sudoku? Here is where the fun (challenge!) begins so
rather than spoil that this introduction will stop here. Please contact the coaching
staff for the club if you decide to try this project so they can help you make progress.



#### Part 2: Solving the puzzle


Following the great Jake VanderPlas' solution we reason as follows: 


Because this problem seems fairly complicated I am going to assume that I can make two logical
guesses about how to solve it. Once I have those two guesses I am going to convert them into
Python code and see if they work. If I have only one logical guess I don't think it will be 
enough. If I give myself space for two then maybe that is enough. If it is not enough I will
keep adding more logic until I either solve the problem or determine that it is impossible. 


##### Logical Guess Number One


The Sudoku puzzle at the start is 81 cells, some of which are full and others are empty. 
If I go to an empty cell I can make a guess as to what number can go in that cell. In 
fact before doing anything else I know there are nine possible values that can go in the
cell: 1, 2, 3, 4, 5, 6, 7, 8 or 9. If there are already numbers in the row of this cell
then I cross those numbers off the list. If there are already numbers in the column of 
this cell then I cross *those* numbers off the list. My cell is also in one of the 
nine 3 x 3 blocks. If there are numbers in my cell's block I also cross *those* numbers
off the list. Now for example my list of possible guesses might be reduced to these
four: 1, 3, 4, and 8. So I am free to pick one of them, say the first one, and I can 
write a '1' in that cell. I know it is legal based on the information that I have so far. 
And once this cell has been filled with a '1' I can say I am one step closer to having
solved the puzzle; and if I go to another cell and ask the same question then I can 
follow the same procedure. Only now my new '1' is part of the existing data for what
values are possible in the next cell: If the next cell is in the same row then it can not
contain the value '1'; and so on. 


So here is my first logical guess: I am going to guess that I can just start jumping around
the puzzle to empty cells in no particularly clever way, simply filling in numbers from the
list of possible numbers, again in no particularly clever way. All I am doing is looking for
legal values for a cell, picking one of them, and moving on to another cell. The only thing
that can possibly go wrong is that I get to a cell and find out that there are no possible
choices available. In this case I have made some bad guesses that have made the puzzle 
unsolvable and I have to back up and try something else. 


Notice that in this way this problem is very similar to a maze where you can go down a blind
alley or a dead-end hallway and the only way to make progress is to back up. This is also 
the case with another one of our projects, the knight's tour. 


##### Logical Guess Number Two


Given the guessing approach described in part 1: I need a strategy for backing up and 
trying a different guess when I get stuck. In order to describe an approach to this
problem I am going to imagine a very long room with a very long table and a stack of
identical pieces of paper, each one with a copy of the original puzzle written on it. 
Let's say I have 100 copies of the puzzle although I will not need them all. And I 
also have a pencil with an eraser. Now we are going to solve the Sudoku problem using
Logical Guess Number One but we will do it by observing how the process works so that
we can produce Logical Guess Number Two. 


Left off here!



