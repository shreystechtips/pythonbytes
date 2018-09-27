from mcpi.minecraft import Minecraft
import numpy as np
from random import randint
import kilroy
from kilroy import msg

def FracJump(a, b, frac): return (a.x + frac*(b.x-a.x), a.y + frac*(b.y-a.y), a.z + frac*(b.z-a.z))

def MonteCarlo(mc, p0, v, frac, nSteps):   
    a = mc.player.getPos()                           # establish a as a position; will be used to set vertex locations
    p = mc.player.getPos()                           # establish p (our point dot) as a position
    p.x, p.y, p.z = p0.x + 17, p0.y + 24, p0.z + 7   #   and move it a bit away from the passed origin

    vertices = []    # build out the four vertex locations
    for i in range(nVerts):
        a.x, a.y, a.z = v[i][0] + p0.x, v[i][1] + p0.y, v[i][2] + p0.z
        vertices.append(a)        # vertices is a list of minecraft positions where we are concerned with .x, .y, .z coordinates
            
    for i in range(nSteps):
        p.x, p.y, p.z = FracJump(p, vertices[randint(0, len(v)-1)], frac)
        mc.setBlock(p.x, p.y, p.z, kilroy.gold)

mc = Minecraft.create()
xPos, yPos, zPos = 2500, 50, 2500       
mc.player.setPos(xPos, yPos, zPos)    # Put the player at this location
p0=mc.player.getPos()                 # ...and establish a minecraft position called 'originPos'
p0.y -= 2                             # ...and move this to 2 blocks away from the player

msg(mc, "start tetrahedron")
MonteCarlo(mc, p0, v = [(0,0,0), (200,0,150)), (200,0,-150)), (120,205,0)], frac = 0.5, nSteps = 10000)
msg(mc, "tetrahedron maker returned")
