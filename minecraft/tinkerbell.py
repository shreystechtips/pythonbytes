# geometry_helper contains simple or 'primitive' geometric builders
#
# pos = mc.player.getPos() # to set type (inelegant)

from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import numpy as np
import time
from random import randint
# import cgkit
pi = np.pi
def d2r(d): return pi*d/180.0
def r2d(r): return 180.0*r/pi
def swap(a, b): c = b; b = a; a = c; return (a, b)

# Try this out to get the highest non-air block y value
# y = mc.getHeight(0,0)


mc = Minecraft.create()
p = mc.player.getPos()
v = Vec3(p.x, p.y, p.z)

# print(mc.player.getRotation())
# print(mc.player.getPitch())
# print(mc.player.getDirection())

# Create a line of blocks between positions a and b
#   mc is a minecraft object
#   a and b are mc.player.getPos() positions
#   block is a tuple (blockType, blockQualifier)
def LineSegment(mc, a, b, block):
    if a == b: mc.setBlock(a.x, a.y, a.z, 38, block[1])
    else: 
        dx, dy, dz = np.abs(a.x-b.x), np.abs(a.y-b.y), np.abs(a.z-b.z)
        if dx >= dy and dx >= dz:
            if a.x > b.x: a, b = swap(a, b)
            my, ny = (b.y - a.y) / (b.x - a.x), a.y  # respective slope / intcpt
            mz, nz = (b.z - a.z) / (b.x - a.x), a.z  # respective slope / intcpt
            for xloc in range(int(a.x),int(b.x)+1):
                x = 1.0*xloc
                xrel = x - a.x
                y, z = my * xrel + ny, mz * xrel + nz
                mc.setBlock(x, y, z, 103, randint(0,8))
        elif dy >= dz:
            if a.y > b.y: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.y - a.y), a.x
            mz, nz = (b.z - a.z) / (b.y - a.y), a.z
            for yloc in range(int(a.y),int(b.y)+1):
                y = 1.0*yloc
                yrel = y - a.y
                x, z = mx * yrel + nx, mz * yrel + nz
                mc.setBlock(x, y, z, 38, randint(0,8))
        else:
            if a.z > b.z: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.z - a.z), a.x
            my, ny = (b.y - a.y) / (b.z - a.z), a.y
            for zloc in range(int(a.z),int(b.z)+1):
                z = 1.0*zloc
                zrel = z - a.z
                x, y = mx * zrel + nx, my * zrel + ny
                mc.setBlock(x, y, z, 38, randint(0,8))

polling_interval = 0.4
ahead_distance = 20.
ahead_radius = 10.0
nArcBlocks = int(ahead_radius * 2. * 3.14159 * 1.2)    # 1.2 is a factor to oversample a bit
        
while True:
    time.sleep(polling_interval)
    p2 = mc.player.getPos()
    if np.abs(p2.x - p.x) > 2. or np.abs(p2.y-p.y) > 2. or np.abs(p2.z-p.z) > 2.:

        # This draws a trailing line
        # LineSegment(mc, p, p2, (49, 0))
        # p = p2

        # v will be a unit vector in the direction of motion
        v = p2 - p
        mag_v = np.sqrt(v.x*v.x + v.y*v.y + v.z*v.z)
        v.x /= mag_v
        v.y /= mag_v
        v.z /= mag_v

        # cc is a location of the center of the drawing circle in mc space
        cc = p2 + Vec3(v.x*ahead_distance, v.y*ahead_distance, v.z*ahead_distance)    # location of center of circle

        # yz is unit perpendicular to v with a zero x-component
        yz = Vec3(1., 0., -v.x/v.z)
        mag_yz = np.sqrt(yz.x*yz.x + yz.y*yz.y + yz.z*yz.z)
        yz.x /= mag_yz
        yz.y /= mag_yz
        yz.z /= mag_yz

        # up is unit perpendicular to v and yz
        up = Vec3(yz.y*v.z-yz.z*v.y, yz.z*v.x-yz.x*v.z, yz.x*v.y-yz.y*v.x)
        mag_up = np.sqrt(up.x*up.x + up.y*up.y + up.z*up.z)
        up.x /= mag_up
        up.y /= mag_up
        up.z /= mag_up

        for i in range(nArcBlocks):
            theta = (float(i)/30.)*2.*np.pi
            ct = np.cos(theta)
            st = np.sin(theta)
            pp = cc + Vec3(yz.x*ct, yz.y*ct, yz.z*ct) + Vec3(up.x*st, up.y*st, up.z*st)
            mc.setBlock(pp.x, pp.y, pp.z, 46)
            
        

    
