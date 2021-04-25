# Session 8
# Problem 2: Circular Sector Class

""" STATEMENT:
In this exercise, we will work with circular sectors of circles centred at (0,0).
Such sectors will be specified by three numbers:
the angle (in degrees between 0 and 359) that the segment starts from (fr)
the angle (in degrees between 0 and 359) that the segment ends (to)
the radius (rad)

All of the above are integer numbers and the angles are counted from the direction of the positive x axis.

Moreover, you may assume that the from angle is always smaller or equal to the to angle (fr <= to).
(If you'd like, after you have a working solution, you can solve a more challenging version of this problem when this simplification is removed.)

To implement, follow the pattern on the left. The examples of how the class is used and tested are below:

TEMPLATE:

TESTS:

See #Test1, #Test2, … in Statement """

class Sector:

def __init__(self):

self.fr = 0
self.to = 0
self.rad = 0

def rotate(self, angle):

#implement this

#rotates sector by angle
#you man assume the rotation never results in a sector with fr > to
#(it is optional to solve this problem without this assumption; see above)

def intersect(self, other):

#implement this

#returns sector (i.e., object of class Sector) that is intersection
#of this and other sector
#you may assume that the two sectors have nonempty intersection

def is_empty(self):

#implement this

#returns True if the sector has empty area, otherwise False

def __eq__(self, other):

#implement this

#returns True this sector is the same as the other, otherwise False

def __str__(self):

#implement this

#returns string "F T R" where F is from angle, T is to, and R is radius

s1 = Sector()
s1.fr = 0
s1.to = 20
s1.rad = 40
assert str(s1)=="0 20 40"
s1.rotate(50)
assert str(s1)=="50 70 40"
s2 = Sector()
s2.fr = 50
s2.to = 70
s2.rad = 40
assert s1==s2
s2.fr = 60
s2.to = 100
s2.rad = 30
s3 = s1.intersect(s2)
assert str(s3)=="60 70 30"