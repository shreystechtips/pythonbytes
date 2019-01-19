# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/idunno#pythonbytes-project-in-depth)


### Overview


Here is a creature that lives in the ocean... and she has a problem... and she needs your help...


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/whales/humpback.png" alt="drawing" width="700"/>


### Details

A student -- when asked 'What can you do to help here?' -- replied 'ummmmm..... I dunno.......' This is exactly
right; and that's why we're here doing this project! As you develop tech skills you can help us change information
into a better world: For whales and humans as well. 


This project is a simple model of the ocean. First we want to create that watery world. Let's have it be small to
start with, 400 x 400 locations, in other words a grid of locations. One way to do this is with a list of rows. Each 
row is a list of 400 locations called columns. Let us call it ```ocean```. Run these two lines of code. You can
use any programming environment that supports turtle graphics; including [cswonders.com](http://cswonders.com). 


```
zero_row = [0]*400
ocean = [zero_row]*400
```

Now let's put the number `7` in one of those cells and make sure it appears when we print. 

```
ocean[53][291] = 7
print(ocean[52:55][290:293]
```

