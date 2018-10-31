# PythonBytes Project Ideas


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects)


### On selecting a project
Below is a list of project ideas. Choose one to try out; modify it if you like; or make up one of your own.
The most important thing to remember as you read and think is: Check in with us so we can help make sure 
you are successful with your project.  To keep your project work from being confusing, impossible and/or 
discouraging you might look for something 'very easy' first. Often a simple-sounding project can be 
surprisingly fun and interesting. 


- **Many interesting project ideas can be found at [Project Euler](https://projecteuler.net/)**
- **You are an artist who uses computer graphics to produce graphical themes and patterns: Existing and new**
- **A farmer uses drones to locate beehives in her orchard so she can cultivate them and have a better harvest**
- **You are observing some bugs placed on a table. They follow some rules for motion and your task is to simulate this**
- **There are many ways to calculate pi using a computer; so learn to build and compare them**
- **You have a chessboard and a knight placed upon it. Find a path of legal knight moves that visits every square once**
- **Create a text adventure where a player must determine the right series of steps to escape from a locked room**
- **Create a program that plays a simple game like tic-tac-toe or Nim against a human**
- **Create a program that solves a Sudoku puzzle**
- **Create an interactive video game using a Python package like [pygame](http://pygame.org)**
- **Use a simple procedure called the *Chaos Game* to create a fractal structure with infinite permiter and zero area**
- **Create an interactive program: Ask the player some questions; then tell them something interesting**
- **Create a program that is able to find its way out of a maze**
- **Use the rules of complex arithmetic to create one of an infinite number of Julia Set fractals**
- **You study whales and their calls and you would like to try and talk to them**
- **Minecraft landscapes: You use four simple functions to build anything you can imagine in Minecraft** 
- **Ditch Day Stack: An advanced project for those who complete some other project and wish to do more**




### Project: Project Euler! 


**Many interesting project ideas can be found at [Project Euler](https://projecteuler.net/)**


This is a website containing dozens and dozens of interesting programming challenges with mathematical themes. 
Here is an extended quote from their main page: 


> Project Euler is a series of challenging mathematical/computer programming problems that will require more 
> than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient 
> methods, the use of a computer and programming skills will be required to solve most problems.
>
> The motivation for starting Project Euler, and its continuation, is to provide a platform for the inquiring 
> mind to delve into unfamiliar areas and learn new concepts in a fun and recreational context.


Here is a good example of a Project Euler problem (number 63): 

> The 5-digit number 16807 is also a fifth power: Seven raised to the fifth power. 
> Similarly, the 9-digit number 134217728 is also eight raised to the ninth power.
>
> How many n-digit positive integers exist which are also an n-th power?


### Project: Art Concepts


**You are an artist who uses computer graphics to produce graphical themes and patterns: Existing and new**


Here is an image of a painting by Dutch painter Piet Mondrian. 


![image of a painting by Piet Mondrian](https://github.com/robfatland/pythonbytes/blob/master/projects/mondrian.png "Tableau I, 1921")


It is abstract and very minimal in its construction elements. The idea of this project is to research different themes and 
artists with the idea of creating similar graphical elements using Python. You might begin with Turtle graphics but there 
are many other ways you can proceed.  There is even an [entire book](https://www.makeartwithpython.com/book/) devoted to
making art using Python that we can explore. 


### Project: Bees and Drones


**A farmer wishes to use drones to locate some beehives on her orchard so she can cultivate them and have a better harvest.**

You are a farmer. You have an orchard 2000 meters x 2000 meters. Notice that locations in your orchard can be
represented using (x, y) coordinates. Your trees (they are baobab trees) go up quite high, as high as 30 meters; 
so we can think of the height above the ground as a third (z) coordinate. Hence a location in your orchard can
be written as (x, y, z). For example (16, 12, 5) would be a point 20 meters from the corner of the orchard and 
5 meters above the ground.  


Seeing a few bees buzzing about -- honey bees I should say -- you have determined that there are some bee hives 
in your orchard. However the tall trees make them hard to locate... but you have a small supply of drones that 
can travel to any location (x, y, z) in your orchard and count the number of bees there. The drone turns off its
propellers for a moment and uses a microphone to count the number of bees nearby. Then it flies back to your 
house and reports how many bees it found.


Unfortunately there is a small chance that your drone will get caught in a tree and be lost to you each time 
you send it out to count bees. (Perhaps the bees recover the lost drones and use them for their own purposes.
If you understand this joke please explain it to your parents.) 


You want to locate the bee hives so that you can transfer the summer swarms to Dadant box hives. Then those 
bees will have a nice home and they can help you by pollinating your trees. This will result in more fruit to
sell at the market. So the project is to write a program that locates the hives before you run out of drones.  


To do this project you will take advantage of a service that Rob put on the internet. It is like a website 
that you go to; and when you go there (using Python) you tell it the (x, y, z) coordinates you send your 
drone to and the website responds back with how many bees were found. This requires about four lines of 
code that we will interpret: Should you decide to take on this project. The lines of code are given below.


```
import requests
def bees(x, y, z): return int(requests.get('https://52t7suregg.' + \
        'execute-api.us-east-1.amazonaws.com/default/dronebees?' + \
        'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text)
    
print(bees(10, 17, 4))
```

You can try this without using Python by clicking on 
[this link](https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?x=10&y=17&z=4).


I ran this just now and it told me there are four bees at that location. If the bees() function gives 
'drone lost' then you the farmer have one less drone to work with. You start with ten drones and you can't buy more
so you want to be careful about how many times you send your drones out for data. 


The challenge of this project is to think about the logic for locating the bee hives. If there was no danger of
losing drones you could just send the drone out four million times to every possible location in the orchard. 
However since the drones will eventually all wind up stuck in the baobab trees it behooves you to come up with 
a more efficient strategy.


Notice that you can augment your Python program with an incredibly powerful computer: You can use your own brain
to make suggestions by means of an input statement. 



### Project: Converging Bugs


**You are observing some bugs placed on a table. They follow some rules for motion and your task is to simulate this.**


There is a famous math problem that can be solved using some logic. The idea here is to verify that the logical
solution is also what you would measure if you used a computer program to simulate how the bugs move. 


Pursuit is really easy to do using turtle graphics. There are a number of methods built into turtles that 
enable you to send one turtle towards another. (If you are looking for 'pursuit' notes this is the place. 
(There is a club coil about this.))  The first method of interest is called **towards** and it gives you
a heading as an angle: From one location to another. In our case you can get a heading from one turtle to
another. The second idea is then simply to set the heading of a turtle. You do this using the setheading
method. Here are three lines of code that orient a turtle named bravo towards another turtle named alpha
and then move it in that direction 1 pixel:


```
    heading_from_bravo_towards_alpha = bravo.towards(alpha)
    bravo.setheading(heading_from_bravo_towards_alpha)
    bravo.forward(1)
```


### Project: Pi from Py


**There are many ways to calculate pi using a computer; so learn to build and compare them**


One of the most fundamental ideas in computer programming is the loop: Doing a task over and over again (each
time in a different way) until a much larger task is completed. Humans rapidly tire of such tasks since we are
busy with other tasks at the same time... like eating lunch and singing songs. So imagine if you will that some
mathematician has invented a sequence of fractions which is infinitely long. When added together these fractions
are equal to pi... which consists of an infinite number of digits. Using a computer you can calculate pi 
*approximately* by adding up tens of thousands of these fractions. How accurate is the result? 


The interesting thing is that there are dozens and even hundreds of ways to calculate pi in this way; suggesting
a comparison of a few of them using your Python programming skills. This is an excellent starter project if you 
are concerned about doing something fairly simple to build up your confidence. 

### Project: Knight's Tour


**You have a chessboard and a knight placed upon it. Find a path of legal knight moves that visits every square once.**


This is another famous problem that can be solved with a good choice of algorithm. It also usually takes the 
form of a recursion problem; so here is a note on recursion. Suppose you want to add 2 + 2 + 2 + 2 + 2 + 2 + 2.
One way to do this is to write a Python function that can call itself. This is an advanced topic so you will 
want to talk to the Python Bytes coaches if you are not already familiar with it. 


Now to consider whether you want to try this project: First make sure you know how knights move across the board 
in the game of chess. Then think about how you would keep track of where the knight has visited (which squares) 
on its tour. For each move you must determine where the knight *could* possibly go next and which of those *possible*
squares have already been visisted. If the knight has no possible moves from a given square then your program must 
back up the knight up to where it can choose a different path. It is very much like walking through a maze that you
build as you go through it. When the knight backs up it should not try the same path as you already know that won't
work; so you must keep track of what you have already tried in some way. So there is quite a lot of logic involved 
in this problem and it is definitely a difficult programming challenge. But it is also very fun. 


### Project: Room Escape 


**Create a text adventure where a player must determine the right series of steps to escape from a locked room.**


### Project: Game Player


**Create a program that plays a simple game like tic-tac-toe or Nim against a human.**


Creating simple computer games where the computer takes one side is a time-tested way of improving your programming 
skills. First you must create code that properly conducts the game; and then you must add some form of intelligence
so it plays well enough for the game to be interesting to the human player. Tic-tac-toe and Nim are two examples
of games but there are dozens more.


### Project: Solve a Sudoku puzzle


**Create a program that solves a Sudoku puzzle**


This project develops arithmetic and logic (Python) skills. If you are unfamiliar with Sudoku you
should learn about it and try some easy example puzzles first. Let's assume you have done so; now
how would you go about building a program that solves a Sudoku (instantly!). We describe one approach
here following the ideas of the great Jake VanderPlas. You can dive into the sudoku folder and read
the guidelines there... or you can begin right away without any hints and see how far you get. 




### Project: Video game


**Create an interactive video game using a Python package like [pygame](http://pygame.org)**


### Project: Fractals I


**Use a simple procedure called the *Chaos Game* to create a fractal structure with infinite permiter and zero area**


The Chaos Game uses a geometric plane with three (or *n*) points and a random number generator. You begin anywhere
and follow a simple rule to determine which of the points is your target. You move half-way to that target and draw
a small dot. Then you repeat the procedure a large number of times until a pattern emerges. Advanced programmers 
may choose to play the Chaos Game in three dimensions, for example in the world of Minecraft. 


### Project: Fortune Teller


**Create an interactive program: Ask the player some questions; then tell them something interesting.**


### Project: Maze Solver


**Create a program that is able to find its way out of a maze.**



### Project: Fractals II


**Use the rules of complex arithmetic to create one of an infinite number of Julia Set fractals.**


### Project: Whale calls


**You study whales and their calls and you would like to try and talk to them.**


![humpback whale spectrogram](https://github.com/robfatland/pythonbytes/blob/master/projects/humpback_spectrogram.png "whale call")


### Project: Minecraft landscapes


**Minecraft landscapes: You use four simple functions to build anything you can imagine in Minecraft** 


### Project: Ditch Day Stack


**Ditch Day Stack: An advanced project for those who complete some other project and have time to do more.**


This is an advanced project for students who complete a project and have time to do more. The key idea to this project
is you have no idea what it is about to start with except for the three words 'ditch day stack'. 
