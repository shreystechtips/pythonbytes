# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/sudoku#pythonbytes-project-in-depth)


### Overview


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/sudoku/sudoku.png" alt="drawing" width="300"/>


These project notes are currently in development. You are welcome to read through here but 
not everything is complete and tested! My sudoku program does not work yet, for example.


To get started on this we use a strategy called *recursion*. You may want to say to yourself
'I need to understand recursion' before going further. That way when you run into recursion 
you will be prepared for the awesomeness. 


Incidentally there are a number of styles of puzzle similar to Sudoku; such as Shikaku. 
If you create a Sudoku solver you have the opportunity to go further.



### Details

We proceed in two parts. First we describe how to think about a Sudoku puzzle
with a computer programmer's frame of mind. Second we break the program down by hints that 
show you the path very directly. 


#### Part 1: A programmer's approach to a Sudoku puzzle


All Sudoku puzzles have a starting point. The most basic would be an empty puzzle: Simple 9 x 9 
empty cells. Obviously this has many solutions!


Suppose you come upon a Sudoku puzzle with 21 cells filled in, leaving 60 empty. Each of those
60 empty cells will have a number from { 1, 2, 3, 4, 5, 6, 7, 8, 9 } in it. The number of 
possibilities is 9 raised to the 60 power. This is too many possibilities for a
computer to simply try them all: 
1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000. 
If you could try one billion possibilities per second it would require...


...wait for it...


2.3 quadrillion quadrillion ages of the universe to try every possibility.


Fortunately we have a time-saving trick that will allow us to solve any Sudoku problem in a couple 
of seconds. Therefore let us celebrate for a moment: Not only are we capable of imagining such a
difficult puzzle to solve; we are also able to come up with an efficient way to solve it. 


Ok, so how to begin? Let us begin by breaking the challenge (of solving a Sudoku) down into
smaller challenges. 
A good programmer learns to recognize useful *questions* that come from this process of 
breaking down a problem.


**How shall we represent a Sudoku puzzle?**


Since a Sudoku puzzle is 9 x 9 or 81 cells we can use a string of 81 characters. 
However strings are difficult to change... in fact we can only change them by using
them to build new strings. What is *easy* to change in Python is a list. So let us 
plan to use a string to describe a puzzle; but then we will convert this string 
into a list with 81 elements. This list will (we hope) help us solve the Sudoku puzzle. 


Here is a string that represents the Sudoku puzzle shown above. I read across from
left to right, starting at the top and going down (just like reading a page of English
text like this one). 

```
**86324** 
*4*****1*
5**9*4**6
8*******5
6*******4
1*7***9*2
4**751**3
*6*****2*
**58267**
```

or -- after connecting everything into one line -- this line of Python code assigns a string to a
variable called ```puzzle```:


```
puzzle = '**86324***4*****1*5**9*4**68*******56*******41*7***9*24**751**3*6*****2***58267**'
```

I use the asterisk character **\*** to indicate an empty cell.


Suppose we convert at string like the one shown above to a list (since we can modify Python 
lists). How do we do that? It is not too hard. Python has a very simple way:


```
p = list(puzzle)
```

Now if we print the variable ```p``` we will find that it is a list:


```
print(p)

['*', '*', '8', '6', '3', '2', '4', '*', '*', '*', '4', '*', '*', '*', '*', '*', '1', '*', '5', '*', '*', '9', '*', '4', '*', '*', '6', '8', '*', '*', '*', '*', '*', '*', '*', '5', '6', '*', '*', '*', '*', '*', '*', '*', '4', '1', '*', '7', '*', '*', '*', '9', '*', '2', '4', '*', '*', '7', '5', '1', '*', '*', '3', '*', '6', '*', '*', '*', '*', '*', '2', '*', '*', '*', '5', '8', '2', '6', '7', '*', '*']
```

This is fine; and a little later we will convert this very nice listing of single characters into a list 
of lists. For now though let's consider this a good start and move on to the actual rules of Sudoku.


The rules of Sudoku answer the question 'What numbermust be in each empty cell?':

- The number in a cell must not duplicate any other cell in its row
- The number in a cell must not duplicate any other cell in its column
- The number in a cell must not duplicate any other cell in its 3 x 3 cell block


Therefore cell locations are important for the purpose of comparison with other cells. 


REWRITE ENDS HERE



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


Given the guessing approach described in part 1: I need a strategy for what happens
when I have no legal guesses. That is I need a way of backing up and trying a different 
path when I get stuck. 


I imagine a very long room with a very long table. I have a stack of paper where on 
each sheet is printed (very large) the Sudoku puzzle I am trying to solve. And I have 
a pencil with an eraser.  I am going to solve the Sudoku puzzle by starting out at one end
of the long table and taking the top sheet of paper, my first copy of the puzzle. 
By observing how my solution process works I will arrive at my second logical guess. 


I look at my first copy of the Sudoku puzzle and say 'Here is a new Sudoku puzzle for me 
to solve.' 


On this piece of paper I write (fairly small) up at the top of each empty cell every possible 
guess for that cell. For example (using the puzzle we have above) in cell 8 at the upper 
right corner I write '4, 6' since those are the only two possibilities. In cell 7, just to 
the left of cell 8, I write '3, 4, 6'. In cell 6 I also write '3, 4, 6'. Notice that these
are possible guesses. The possible guesses in once cell do not affect the possible guesses
in another cell.  I do not do possible guesses for cells that have big numbers written in
them: Those are assumed to be 'done'. I only do possible guesses for empty cells. 


Now that I have filled out possible guesses for all of the cells I will pick an empty
cell, let's say cell 12 which has coordinates (1, 3) and has possible guesses 3, 4,
6, 7, 8, 9. I choose the first of these, '3' and I write that as a full-sized number
in the center of the cell. This is a guess; but I am pretending it is correct as we 
described doing above. 


I now get a new copy of the puzzle from my stack of copies. I carefully copy the '3'
in cell 12 onto this new copy so it is slightly more solved than the previous copy.
And now I say to myself 'Here is a new Sudoku puzzle for me to solve.'  


This phrase should look familiar.


On this (new) copy I write (small) at the top of each empty cell every possible guess for
that cell. Just as I did before; but now taking into account my additional '3' in cell 12. 


Now that I have filled out possible guesses for all of the cells I pick an empty 
cell, let's say cell 43. I pick the first number in the list of possible guesses 
for cell 43 and I write it very large in the center of cell 43. This is a guess that I
am pretending is correct. 


I now get a new copy of the puzzle from my stack of copies. I carefully copy my
two guesses onto this new copy so it is slightly more solved than the previous copy.
And now I say to myself 'Here is a new Sudoku puzzle for me to solve.' 


This phrase should look familiar.


On this (new) copy I write small at the top of each empty cell every possible guess 
for that cell.  Now I pick an empty cell and I pick the first number in the list of 
possible guesses for that cell.  I write this guess as a large number in the center of that 
cell: A guess that I am pretending is correct.  Now I get a new copy of the puzzle from 
my stack of copies.  I carefully copy my guesses onto this new copy so it is slightly 
more solved than the previous copy.  


And now I say to myself 'Here is a new Sudoku puzzle for me to solve.' 


This phrase should look familiar.


On this new copy I write small at the top of each empty cell every possible guess 
for that cell.  Now I pick an empty cell and I pick the first number in the list of 
possible guesses for that cell.  I write this guess as a large number in the center of that 
cell: A guess that I am pretending is correct.  Now I get a new copy of the puzzle from 
my stack of copies.  I carefully copy my guesses onto this new copy so it is slightly 
more solved than the previous copy.  


And now I say to myself 'Here is a new Sudoku puzzle for me to solve.' 


This phrase should look familiar.


On this new copy I write small at the top of each empty cell every possible guess 
for that cell.  Now I pick an empty cell and I pick the first number in the list of 
possible guesses for that cell.  I write this guess as a large number in the center of that 
cell: A guess that I am pretending is correct.  Now I get a new copy of the puzzle from 
my stack of copies.  I carefully copy my guesses onto this new copy so it is slightly 
more solved than the previous copy.  


And now I say to myself 'Here is a new Sudoku puzzle for me to solve.' 


This phrase should look familiar.


You might be tired of reading all of this over and over again... but I am trying to 
make the point that this is why we invented computers: They never get bored of doing
repetitive jobs. Anyway now let's suppose we have done this procedure 65 times 
so that there are 65 pieces of paper laid out on the long table. Each piece of paper
is a record of the next guess. Since we began with 7 cells filled and we made 65
guesses we now have 72 cells filled and there remain 9 empty cells. We are pretty 
happy because we are almost done with the Sudoku puzzle. 


This time as we work from our latest copy of the puzzle with all the guesses filled
in we find that one of the cells has zero possible guesses. There is simply no number
that can be placed in that cell that does not violate the three rules of Sudoku. 
What does this mean? 


What it means is that our previous guess, sheet number 65, was a bad guess. It has
produced an unsolvable Sudoku puzzle. So we can not go any further; we must back up. 
We take our current piece of paper and we ball it up and throw it in the recycling. 
We go back to the previous piece of paper where we wrote down our latest guess and
we erase that guess. At the top of that cell is the list of possible guesses. Since
we chose the first one of those -- and it proved to be a bad guess -- we erase it
from our list of possible guesses. Now we choose the next guess in that list and 
we carry on as before. 


So here you can imagine: What if there was only one possible guess? Then the list 
of possible guesses is down to zero. What do we do? We ball up that piece of paper 
and move backwards to piece of paper number 64. There we erase that last guess 
and choose instead the next possible guess. If there is no next possible guess we 
ball up that piece of paper and move backwards once more. In fact we keep going 
backwards until we reach a point where we can go forwards again. 


It may take some thought to see how this procedure works to solve the Sudoku
puzzle; but see if the Second Logical Guess now makes sense to you: 


Here is the second logical guess: Because I am doing the same procedure over
and over again I will create one and only one function that *calls itself*. 
Every time the function calls itself it is working with a new slightly 
improved copy of the puzzle. If the function gets stuck (there are no possible
choices for one of the cells) the function will simply *not* call itself:
Because we can't go any further. Rather that function will **return** 
back to the previous version of that function. This is *balling up the piece of
paper and backing up to the previous guess*. 


So to summarize our two logical guesses: 


- Once we know all possible guesses for the empty cells we can choose any cell and
choose any guess and pretend it is correct, creating a slightly more solved version 
of the puzzle. 
- By making this solver function call itself it will move closer and closer to a
complete solution but it must also be able to quit (return) when it gets stuck
in such a way that it can try a new guess.





