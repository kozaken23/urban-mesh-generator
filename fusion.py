#dorone-
from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np
import os

input_filename='jimen.dat'

with open(input_filename,'r') as dat_file:
    data = dat_file.readlines()

input_data = open('jimen.dat')

i=0
x=0
y=1
z=2
points1=[]
points=[]
n=0
# 一行ずつ読み込んでは表示する
for rows in input_data:
    result=rows.lstrip()
    row = result.split()
    ztmp=float(row[2])
    if ztmp<0:
        ztmp=0
    xp=(float(row[0]))
    yp=(float(row[1]))
    zp=ztmp
    pointxy=[xp,yp]
    point=[xp,yp,zp]
    points1.append(pointxy)
    points.append(point)
    #np.append(points,point,axis=0)
    #print(point)
    #print(points)
points1=np.array(points1)

#ドロネー
#print(pts)
# [[172  47]
#  [117 192]
#  [323 251]
#  [195 359]
#  [  9 211]
#  [277 242]]
print(type(points1))
# <class 'numpy.ndarray'>
print(points1.shape)
# (6, 2)
tri = Delaunay(points1)
print(type(tri))
# <class 'scipy.spatial.qhull.Delaunay'>
#fig = delaunay_plot_2d(tri)
#fig.savefig('samdorone.png')
size=len(points1)
sankaku=tri.simplices#三角形の点の番号

#zlist=[]
"""for rows in input_data:
    result=rows.lstrip()
    row = result.split()
    ztmp=float(row[2])
    if ztmp<0:
        ztmp=0
    zp=ztmp
    points1[i].append(zp)
    #print(points1[i])"""
#zlist=np.array(zlist)
#points=np.insert(points,0,zlist,axis=1)
#print(points1[1045577])
input_data.close()

with open('sample.wrl','w') as f:
    print('#VRML V2.0 utf8\nShape{\n    appearance Appearance{\n        material Material{\n            diffuseColor 0.5 0.5 0.5\n        }\n    }',file=f)
    print('    geometry IndexedFaceSet{\n        coord Coordinate{\n            point[',file=f)
    for i in range(size):
        print("                "+str(points[i][x])+" "+str(points[i][y])+" "+str(points[i][z])+",",file=f)
    print("            ]\n        }\n        coordIndex[",file=f)
    for i in range(len(sankaku)):
                print("            "+str(sankaku[i][0])+","+str(sankaku[i][1])+","+str(sankaku[i][2])+","+"-1",file=f)
    print('        ]\n    }\n}',file=f)
    
    
input_filename='tatemono.dat'

with open(input_filename,'r') as dat_file:
    data = dat_file.readlines()

input_data = open('tatemono.dat')

i=0
x=0
y=1
z=2
points1=[]
points=[]
n=0
# 一行ずつ読み込んでは表示する
for rows in input_data:
    result=rows.lstrip()
    row = result.split()
    ztmp=float(row[2])
    if ztmp<0:
        ztmp=0
    xp=(float(row[0]))
    yp=(float(row[1]))
    zp=ztmp
    pointxy=[xp,yp]
    point=[xp,yp,zp]
    points1.append(pointxy)
    points.append(point)
    #np.append(points,point,axis=0)
    #print(point)
    #print(points)
points1=np.array(points1)

#ドロネー
#print(pts)
# [[172  47]
#  [117 192]
#  [323 251]
#  [195 359]
#  [  9 211]
#  [277 242]]
print(type(points1))
# <class 'numpy.ndarray'>
print(points1.shape)
# (6, 2)
tri = Delaunay(points1)
print(type(tri))
# <class 'scipy.spatial.qhull.Delaunay'>
#fig = delaunay_plot_2d(tri)
#fig.savefig('samdorone.png')
size=len(points1)
sankaku=tri.simplices#三角形の点の番号

#zlist=[]
"""for rows in input_data:
    result=rows.lstrip()
    row = result.split()
    ztmp=float(row[2])
    if ztmp<0:
        ztmp=0
    zp=ztmp
    points1[i].append(zp)
    #print(points1[i])"""
#zlist=np.array(zlist)
#points=np.insert(points,0,zlist,axis=1)
#print(points1[1045577])
input_data.close()
    
with open('sample.wrl','a') as f:
    print('\nShape{\n    appearance Appearance{\n        material Material{\n            diffuseColor 1 1 1\n        }\n    }',file=f)
    print('    geometry IndexedFaceSet{\n        coord Coordinate{\n            point[',file=f)
    for i in range(size):
        print("                "+str(points[i][x])+" "+str(points[i][y])+" "+str(points[i][z])+",",file=f)
    print("            ]\n        }\n        coordIndex[",file=f)
    for i in range(len(sankaku)):
                print("            "+str(sankaku[i][0])+","+str(sankaku[i][1])+","+str(sankaku[i][2])+","+"-1",file=f)
    print('        ]\n    }\n}',file=f)