# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-II#pythonbytes-project-in-depth)


### Overview


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/fractals-II/juliaset.png" alt="drawing" width="300"/>

Here is the 
[link to the simpler fractal project](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-I#pythonbytes-project-in-depth). 


This project begins with defining a new kind of number and some associated arithmetic rules. In particular we need both 
addition and multiplication. You are accustomed to real numbers like 4.3 and -19.83838383831111. So let's create a new
number that is simply two real numbers in a row like this: (4.3, -19.8383838383838381111). This -- you might say -- is not 
a number! It is two numbers in parentheses separated by a comma! This is true. But if we can come up with some good rules
for arithmetic then we can also say it is a new kind of number, a complicated number, even sometimes called a **complex** 
number. 

A complex number we write abstractly as **(a, b)**. Another one might be **(c, d)**. Let's define adding them in the 
most obvious possible way: 


(**a**, **b**) + (**c**, **d**) = (**a** + **c**, **b** + **d**)


Now we need a rule for multiplication. This will be a bit more *complex*:


(**a**, **b**) * (**c**, **d**) = (**a** * **c** - **b** * **d**, **a** * **d** + **b** * **c**)


With this we are ready to build some fractals2... almost. We also need the idea of the absolute value of a complex
number. The absolute value of 7 is 7. The absolute value of -4  is 4. The absolute value of a complex number is the
length of the hypotenuse of a right triangle whose legs are **a** and **b**. Let's call that **S** for *Size*:


**S** = square root (**a** * **a** + **b** * **b**)


Now we have everything we need. Notice that a complex number (**a**, **b**) can be drawn on a graph using the x-axis for 
the first number **a** and the y-axis for **b**. 



### Details




