# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/coils#pythonbytes-project-in-depth)


### Coils

Here we have all of the **Coils** from the PythonBytes worksheets. They are rephrased a little bit with the idea of 
suggesting projects.

### Starter Challenges

* Write a program that prints *Lonna’s dog said “whuff!!”*
* Write a program to print out the first 10 fibonacci numbers
* Determine what this program does by running it many times

```
from random import randint
print(randint(1,6)+randint(1,6))
```

* Write a program: Input a number n, then calculate and print n fibonacci numbers
* Write code to print ten rows of the Pascal triangle in a pretty and readable fashion
  * At the end of each row print a colon followed by the sum of all the numbers in that row
* If you roll 3 dice and add the results the lowest possible sum is 3 and the highest is 18. If you roll n dice the lowest is n and the highest is 6n. Write a program that rolls *n* dice 10,000 times and keeps track of the results in a list. Plot the results using a turtle. You can set the value of *n* at the top of the program or you can have this be an input. Compare your results for n = 1, 2, 3, 4, and 5. (Getting the turtle to draw your results is a very challenging and worthy project in itself!)
* You have a set of n objects, all different, placed in a row before you. You decide to count how many subsets of this set there are by placing either a black or a white pawn next to each object. A black pawn means the object is in the subset and a white pawn means that the object is not in the subset. Now two questions:
  * Does this suggest an easy way of calculating the total number of subsets?
  * What if anything does this have to do with previous challenges? 
* Write a computer program that guesses a number that you choose between 1 and 100
* Write a computer program that plays Nim. (You may have to look up Nim!)
* Add up all the integers from 1 to 9,472
* What is the difference between range(20), range(4,20), and range(4,20,7)? 
* Here is a more complex challenge in three parts...
  * **Chooser** picks a number from 1 to 100; and **Guesser** tries to guess it by saying a number. **Chooser** reponds by saying 'Higher!' or 'Lower!' or 'Got it!' and if you wish to keep score you count how many guesses were needed. The two players take turns being **Chooser** and **Guesser**. So the first challenge is to write a program that acts as **Chooser**.
  * You guessed it: Write a program that plays the game as **Guesser**. Try and make it as skillful as you are. 
  * Now take both programs and combine them into a larger program. The human player first decides whether they want to be **Chooser** or **Guesser** and the program continues from there. 


### Turtle Graphics


Know turtle graphics? These are for you!


* Write a program that draws your name in some impressive way.
* Can you create two turtles that each follow their own path?
* Draw a boat on the ocean. Draw some famous droodles; or invent your own.
* What will the following program do? Check your answer by copying this into CodePad at cswonders.


```
import turtle
from random import randint
t0 = turtle.Turtle(); t0.color('blue'); t0.speed(0); 
t1 = turtle.Turtle(); t1.color('red'); t1.speed(0)
for i in range(100): 
    t0.forward(randint(20, 40)); t0.left(randint(0,359))
    t1.forward(randint(20, 40)); t1.left(randint(0,359))
```

* Create two turtles--one blue, one red--and have them start out facing one another, some distance apart. Make them walk towards one another. What happens?
* Write a program showing a pencil drawing another pencil. Look up Escher's *Drawing Hands*...
* This one involves pursuit. Create two turtles named Alpha and Bravo. Place Alpha at (-150, -150). Place Bravo at (150, -150). Create a time for-loop that counts through 400 time ticks. Each tick: Alpha moves one pixel up and to the right. In the same tick: Bravo moves forward one pixel towards Alpha. Notice that as Alpha moves Bravo will have to keep adjusting the direction that she travels. To get an idea of how to do this I will give you two options. Either explore this web page: https://docs.python.org/2/library/turtle.html or visit the [project ideas page for bugs](https://github.com/robfatland/pythonbytes/tree/master/projects/bugs#pythonbytes-project-in-depth). 
* Enter two pairs of numbers (x, y) and (u, v) and draw three arrows: An arrow from (0, 0) to (x, y), an arrow from (0, 0) to (u, v), and an arrow from (0, 0) to (x + u, y + v). This is a basic building block for creating a spacecraft trajectory planning program. Once you are good at this try changing those coordinates x, y, u, and v inside of for-loops in some interesting way.


### Prime Race


These challenges have to do with prime numbers... *the building blocks of reality!*... so tread carefully.


Write a program that asks for an input number like 7 and then returns the 7th prime number (which is 17) as fast as it can. 
The program should take an input as big as 78,498. We will time all contestant programs to determine which is the fastest. 


Now that you are good at prime numbers: Generate the Ulam spiral! This can be done with turtle graphics as you can print in color; or use regular print statements but only print the primes. The Ulam spiral begins at some (input!) number and counts upwards, printing the numbers so at to emphasize those that are primes.  It is common to begin at 41. Here is an example that goes from 1 to 25; the numbers follow a spiral path. It is not very interesting until you figure out how to emphasize the prime numbers.

```
                        17 16 15 14 13
                        18  5  4  3 12
                        19  6  1  2 11
                        20  7  8  9 10
                        21 22 23 24 25 etcetera
```

Here is the same thing but only printing prime numbers...

```
                        17          13
                            5     3   
                        19        2 11
                            7         
                              23       etcetera
```

Does a pattern emerge if you make the spiral much bigger? How about if you begin at 41 rather than 1?

### Probability

* What does this program do?

```
from random import choice
for i in range(10): print choice(['heads', 'tails'])
```

* Suppose you only have a fair coin that has a 0.5 probability of coming up heads and a 0.5 probability of coming up tails. That is: It comes up heads 50% of the time. How would you use this coin to accurately create an unfair coin that came up heads 37.2% of the time? Check your conclusion by writing and using a Python program.


### Data Science

These are more involved challenges that start to investigate the idea of data. For our purposes *data* means some form of 
information that we can look at using Python. If you want to explore any of these further: Maybe check in with the coaches.

* You are given a variable n that contains a very very long string of letters. Only four letters were used: A, C, G and T. They are in any order; for example the string begins n = ‘ACGGTATACCATGCT…’ and it continues for 10,000 letters. You also have a variable s = ‘ACAGTATAGTTT’, a shorter string of 12 letters. The question is “Where can this little string s be found in the big string n? 

