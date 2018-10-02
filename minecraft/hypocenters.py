# hypocenters.py loads data from a CSV file and prints hypocenter blocks

from mcpi.minecraft import Minecraft
import pandas as pd
import numpy as np

# minAir = 62 is the lowest above-ocean elevation in the y coordinate

x0 = 2200
z0 = 1700

mc = Minecraft.create()
mc.player.setPos(x0, 62, z0)      # Put the player at this location



# ls 'c:/Users/robfa/Documents/GitHub/PythonBytes/minecraft/'
df = pd.read_csv('C:/Users/robfa/Documents/GitHub/PythonBytes/minecraft/SomeHypocentersForMinecraft.csv')
nl = len(df)-1
print(df['xmc'][1])
for i in range(1, nl-1):
    x = int(df['xmc'][i])
    y = int(df['ymc'][i])
    z = int(df['zmc'][i])
    if y > 61 and y < 255:
        mc.setBlock(x, y, z, 41)


print('done')


