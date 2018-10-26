# PythonBytes Project Ideas

[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects)


These are some project ideas for the 2018--2019 Tyee Middle School Python programming club.
Each idea given below is something you can do precisely; or you can make up your
own variations on these ideas. 

- **A farmer uses drones to locate beehives in her orchard so she can cultivate them and have a better harvest.**
- **You are observing some bugs placed on a table. They follow some rules for motion and your task is to simulate this.**
- **You have a chessboard and a knight placed upon it. Find a path of legal knight moves that visits every square once.**
- **Create a text adventure where a player must determine the right series of steps to escape from a locked room.**
- **Create a program that plays a simple game like tic-tac-toe or Nim against a human.**
- **Create an interactive program: Ask the player some questions; then tell them something interesting.**
- **Create a program that is able to find its way out of a maze.**
- **You study whales and their calls and you would like to try and talk to them.**

### this...


![humpback whale spectrogram](https://github.com/robfatland/pythonbytes/blob/master/projects/humpback_spectrogram1.png "whale call")



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


I ran this just now and it told me there are four bees at that location.


The challenge of this project is to think about the logic for locating the bee hives. If there was no danger of
losing drones you could just send the drone out four million times to every possible location in the orchard. 
However since the drones will eventually all wind up stuck in the baobab trees it behooves you to come up with 
a more efficient strategy.

### Converging Bugs


**You are observing some bugs placed on a table. They follow some rules for motion and your task is to simulate this.**


There is a famous math problem that can be solved using some logic. The idea here is to verify that the logical
solution is also what you would measure if you used a computer program to simulate how the bugs move. 


### Knight's Tour


**You have a chessboard and a knight placed upon it. Find a path of legal knight moves that visits every square once.**


### Room Escape 


**Create a text adventure where a player must determine the right series of steps to escape from a locked room.**


### Game Player


**Create a program that plays a simple game like tic-tac-toe or Nim against a human.**


### Fortune Teller


**Create an interactive program: Ask the player some questions; then tell them something interesting.**


### Maze Solver


**Create a program that is able to find its way out of a maze.**


### Project: Whale calls


**You study whales and their calls and you would like to try and talk to them.**


### More ideas to follow!
