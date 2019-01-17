# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/idunno#pythonbytes-project-in-depth)


### Overview


Here is a creature that lives in the ocean... and she has a problem... and she needs your help...


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/whales/humpback.png" alt="drawing" width="700"/>


### Details

A student -- when asked 'What can you do to help here?' -- replied 'ummmmm..... I dunno.......' This is exactly
right; and that's why we're here doing this project! 


First we want to create a world. Let's have it be 400 x 400 locations, a grid of locations. One way to do this 
is with a list of rows. Each row is a list of columns. Let us call it ```ocean```.

```
zero_row = [0]*400
ocean = [zero_row]*400
```


