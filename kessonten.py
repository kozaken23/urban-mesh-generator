from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np
import os

input_filename='53394610_dsm_1m.dat'


with open(input_filename,'r') as dat_file:
    data = dat_file.readlines()

input_data = open(input_filename)

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
cnt=0
#欠損点補完
for i in range(len(points)):
    cnt+=1
    if points[i][z]<=-9999:
        kx=points[i][x]
        ky=points[i][y]
        z1=-1
        z2=-1
        z3=-1
        z4=-1
        z5=-1
        z6=-1
        z7=-1
        z8=-1
        zz=0

        for j in range(len(points)):
            if points[j][x]==kx-1 and points[j][y]==ky-1:
                if points[j][z]!=-9999.99:
                    z1=points[j][z]
                    zz+=1
                else:
                    z1=0
            elif points[j][x]==kx and points[j][y]==ky-1:
                if points[j][z]!=-9999.99:
                    z2=points[j][z]
                    zz+=1
                else:
                    z2=0
            elif points[j][x]==kx+1 and points[j][y]==ky-1:
                if points[j][z]!=-9999.99:
                    z3=points[j][z]
                    zz+=1
                else:
                    z3=0
            elif points[j][x]==kx-1 and points[j][y]==ky:
                if points[j][z]!=-9999.99:
                    z4=points[j][z]
                    zz+=1
                else:
                    z4=0
            elif points[j][x]==kx+1 and points[j][y]==ky:
                if points[j][z]!=-9999.99:
                    z5=points[j][z]
                    zz+=1
                else:
                    z5=0
            elif points[j][x]==kx-1 and points[j][y]==ky+1:
                if points[j][z]!=-9999.99:
                    z6=points[j][z]
                    zz+=1
                else:
                    z6=0
            elif points[j][x]==kx and points[j][y]==ky+1:
                if points[j][z]!=-9999.99:
                    z7=points[j][z]
                    zz+=1
                else:
                    z7=0
            elif points[j][x]==kx+1 and points[j][y]==ky+1:
                if points[j][z]!=-9999.99:
                    z8=points[j][z]
                    zz+=1
                else:
                    z8=0
            if z1!=-1 and z2!=-1 and z3!=-1 and z4!=-1 and z5!=-1 and z6!=-1 and z7!=-1 and z8!=-1:
                break
        points[i][z]=(z1+z2+z3+z4+z5+z6+z7+z8)/zz

kesson=open('kesssson10.dat','w')
for i in range(len(points)):
	kesson.write(str(points[i][x]))
	kesson.write(" ")
	kesson.write(str(points[i][y]))
	kesson.write(" ")
	kesson.write(str(points[i][z]))
	kesson.write("\n")
kesson.close()
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



"""with open('sample.wrl','w') as f:
    print('#VRML V2.0 utf8\nShape{\n    appearance Appearance{\n        material Material{\n            diffuseColor 0 0 1\n        }\n    }',file=f)
    print('    geometry IndexedFaceSet{\n        coord Coordinate{\n            point[',file=f)
    for i in range(size):
        print("                "+str(points[i][x])+" "+str(points[i][y])+" "+str(points[i][z])+",",file=f)
    print("            ]\n        }\n        coordIndex[",file=f)
    for i in range(len(sankaku)):
                print("            "+str(sankaku[i][0])+","+str(sankaku[i][1])+","+str(sankaku[i][2])+","+"-1",file=f)
    print('        ]\n    }\n}',file=f)"""
    
