from mcpi.minecraft import Minecraft
import numpy as np
from random import randint

# This is poor form: It treats a as a minecraft position and b as a tuple of 3 coordinates
def FracJump(a, b, frac): return (a.x + frac*(b[0]-a.x), a.y + frac*(b[1]-a.y), a.z + frac*(b[2]-a.z))

# Chaos game in 3D is len(v) vertices and frac jumps; we will do nSteps of these
#   mc is minecraft; notice the root position is determined by the player; it is not passed
#   v is a list of triples, vertex relative coordinates in (x, y, z)
#     notice there are n = len(v) such vertices, implicit
#     suppose we are at location p and select vertex q to move towards
#   frac is the distance we move along pq: And this might be more than 1 or negative
#   nSteps is the number of hops we will take
#   block and blockQ specify the artifact at p
def ChaosGame3D(mc, v, frac, nSteps, block, blockQ):   
    n = len(v)
    a = mc.player.getPos()                           # 
    a.x, a.y, a.z = a.x + 20, 0, a.z + 20            # an origin offset from player
    p = mc.player.getPos()                           # a working position
    print(a)

    verts = []    # vertex locations as triples
    for i in range(n):
        p.x, p.y, p.z = v[i][0] + a.x, v[i][1] + a.y, v[i][2] + a.z
        verts.append((p.x, p.y, p.z))
        print(verts)

    p.x, p.y, p.z = a.x + 40, a.y + 60, a.z + 80     # p is now the chaos point: arbitrary starting location
            
    for i in range(nSteps):
        p.x, p.y, p.z = FracJump(p, verts[randint(0, n-1)], frac)
        mc.setBlock(p.x, p.y, p.z, block, blockQ)
        if i < 10:
            print(p.x, p.y, p.z)

mc = Minecraft.create()
mc.player.setPos(2600, 50, 2200)      # Put the player at this location

n = 7
v = []
for i in range(n): v.append((randint(0,511),randint(0,255),randint(0,511)))
print(v)
ChaosGame3D(mc, v, frac = 0.5, nSteps = 20000, block = 41, blockQ = 0)
