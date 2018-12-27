# PythonBytes Project In-Depth

## Four Bugs


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/bugs#pythonbytes-project-in-depth)


### Overview

Four bugs -- call them A, B, C, and D -- are at the corners of a square table of side *s*. Each bug
faces the bug at the next corner to their left: A faces B, B faces C, C faces D and D faces A. At a 
signal all the bugs begin walking: Each towards the bug it is facing. They take identical-length tiny bug steps
and as you might imagine they constantly adjust the direction of their walk. For example A starts walking towards
B but as B is walking towards C: A will have to adjust her path to the right to keep sighted on B. 


Eventually all of the bugs meet at the center of the table. When they do: How far has each walked? 


Now you are probably wondering what their real names are. I was too until I looked it up. They are named Alpher, 
Bethe, Gamow and Dyson. You would think that bug C would be called Camow but there is not a letter 'C' in Greek
so we make due with 'G' and that is why it is Gamow. You can look up Alpher Bethe and Gamow on Wikipedia but it 
will not mention Dyson. He came along later to explain everything. So technically the bugs should be abbreviated
A, B, G and D but that would confuse everyone. Come to think of it this paragraph probably didn't help.


### Now what?

Now if you wish to try the project out: You can work on it at cswonders, for example on the Code Pad. Be sure
to save your work somewhere in case something unfortunate happens. You might copy-paste it to OneNote. If you
try this project out you may wish to skip down on this page to the section called **Details**. There are some
very useful tips on how turtle graphics can help you solve this problem. 


As always you will want to tell a coach or parent that you are working on this project. Put it on the sign-up 
sheet and make sure that you ask for help if you happen to get stuck. There are also example programs in this
folder that you can look at if you like. But spoiler alert: They work!




### Details


The technical word for one thing chasing after another is 'pursuit'. It is a good word to know because
often the paths of pursuit are pretty and/or interesting curves. Pursuit problems in Python can make good 
use of turtle graphics. Why? Because turtle graphics has built in 
tools or *methods* that help keep the bugs moving in the right direction. 
This section explains the key ones. 


Suppose we have a turtle called **a** and another called **b**:


```
from turtle import Turtle

a = Turtle()
b = Turtle()
```

Now you can set their pen colors and their positions:

```
a.pencolor(255, 0, 0)
b.pencolor(0, 255, 0)
a.setpos(150, 150)
b.setpos(150, -150)
```

On cswonders our drawing canvas is 400 x 400 pixels with coordinates going from -200 to 200. Notice that
the turtles -- where we placed them -- are pretty far out there but they are still visible on the canvas. 


Now on the canvas or table-top there is an angle from turtle a to turtle b. We can determine this angle
using the towards method:


```
angle_a_to_b = a.towards(b)
```

Notice that angle_a_to_b is a variable and its value will be -90.0 because the angles are measured in degrees. 
What would be the angle if we did ```b.towards(a)```? I'll give you a moment to consider and give the answer below.
The key is that the positive x axis is at angle 0. relative to the origin.


Now how do we point turtle a towards turtle b (or bug a towards bug b if you like)? We use another method called
```setheading()```. By the way the answer to the above question is -90.0. 


```
a.setheading(angle_a_to_b)
```

Now bug **a** is facing towards bug **b**. We can tell bug **a** to take a step forward by one pixel using
the ```forward()``` method. In so doing the **a** bug will be a little bit closer to the **b** bug.


```
a.forward(1)
```

Notice since bug **a** is already pointed in the proper direction the 'forward' command does what we want: Pursuit.


The trick of the program of course is to have all four bugs executing this code at the same time.


How do we know that all of the bugs have come together? Here we can use the turtle graphics method ```distance```.


distance_a_to_b = a.distance(b)


Now you could put an if-statement testing whether this distance is less than say 2 pixels. If it is then we 
presume that the bugs are very close together and have reached the end of their journey. Then it remains to 
report how far each one walked. 


### Making the problem more complicated

This problem can be extended, for example...

- Suppose two diagonals are drawn on the square table. It is possible that in its path 
each bug may cross over this diagonal. Perhaps even more than once. We ask: 
What is the number of times if any that a bug will cross a diagonal?
- Suppose that there is only one bug with no bugs to pursue. This bug has nothing to do and so walks
a distance of zero. If there are two bugs separated by a distance *s* and they walk towards one 
another then each walks a distance *s/2*. What if the table is an equilateral triangle of side *s* 
and there are three bugs, one at each vertex? How far do they walk?
- What if the table is a pentagon with five sides of length *s* and there are five bugs? 
- What if the table is a hexagon? 
- What if the table is a regular n-gon with *n* sides of length *s*? Then how far do the bugs walk
before they meet at the center of the table? 
- What happens if the bugs start out in random locations on some table? Is this interesting or not?
- Same as the previous but each bug's speed is proportional to its distance from the next bug.
Now what happens? In this scenario bugs that are very close to their target bug move slowly and bugs 
that are far from their target bug move faster. 



