# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/adventure)


### Overview

Here is an adventure program, complete:


```
print('You are outside a castle full of monsters. The entrance is just wide enough for you to squeeze in.')
print('The wind whistles and cold rain is soaking you. Inside you see a fire... but you hear scary shrieks.')

action = input('What do you do? ')
if action == 'run away':
    print ('You win! Congratulations on your great fountain of wisdom!')
else:
    print ('The monsters get you... sorry but you lose.')
````

Now the trick is to come up with a more interesting version of this game...


### Details

One way to approach these games is to turn the players' action phrase (the response to 'What do you do?') into
a list of words. Then you can search for certain key words in that list to decide that the player probably had
the right idea. This makes use of two useful things in Python: The split method for strings and the **in** 
function for lists. In this example the player should light a fire in the fireplace because this will scare a 
cat who is sleeping in there; and the cat has a clue on her collar. 

```
while True: 
    print('you are in the library. There is a dark fireplace here and a desk with locked drawers.')
    action = input('What do you do?')
    action_list = action.split()
    if 'light' in action_list and 'fire' in action_list: 
        print('Finding some matches nearby you light a fire in the fireplace. A terrified cat leaps out and runs across the room.')
    else: 
        print('That doesn't seem to help much.')
```

Now let's see what happens when we run this code.
* The description of the library will print
* I am prompted for my action (input statement)
* I type in 'I break the desk apart and look for treasure'
  * The string action is now 'I break the desk apart and look for treasure'
  * action_list = action.split() creates a list action_list = ['I', 'break', 'the', 'desk', 'apart', 'and', 'look', 'for', 'treasure']
  * Since neither 'light' nor 'fire' is in that list I will get the message 'That doesn't seem to help much'
* The while loop repeats, giving me another chance
* This time I type in 'A fire will I now light with my trusty dragon breath'
 * Now the list is ['A', 'fire', 'will', 'I', 'now', 'light', 'with', 'my', 'trusty', 'dragon', 'breath']
 * if ('light' in action_list) returns True since 'light' is in that list
 * if ('fire' in action_list) returns True as well
 * Since both return True the **and** is also true...
 * So I see the success message and I move onwards
 
