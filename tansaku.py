import os
import math
import sys
import statistics
gap=0.5
sys.setrecursionlimit(10000000)
def search1(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p1[x,y]-z)<=gap:
			global c1
			c1+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=y1_2:
				search1(x,y+1,p1[x,y]) #上
			if x+1<=x1_2 and y+1<=y1_2:
				search1(x+1,y+1,p1[x,y]) #右上
			if x+1<=x1_2:
				search1(x+1,y,p1[x,y]) #右
			if x<=x1_2 and ymin<=y-1:
				search1(x+1,y-1,p1[x,y]) #右下
			if ymin<=y-1:
				search1(x,y-1,p1[x,y]) #下
			if xmin<=x-1 and ymin<=y-1:
				search1(x-1,y-1,p1[x,y]) #左下
			if xmin<=x-1:
				search1(x-1,y,p1[x,y]) #左
			if xmin<=x-1 and y+1<=y1_2:
				search1(x-1,y+1,p1[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search2(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p2[x,y]-z)<=gap:
			global c2
			c2+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=y2_3:
				search2(x,y+1,p2[x,y]) #上
			if x+1<=x1_2 and y+1<=y2_3:
				search2(x+1,y+1,p2[x,y]) #右上
			if x+1<=x1_2:
				search2(x+1,y,p2[x,y]) #右
			if x<=x1_2 and y1_2<=y-1:
				search2(x+1,y-1,p2[x,y]) #右下
			if y1_2<=y-1:
				search2(x,y-1,p2[x,y]) #下
			if xmin<=x-1 and y1_2<=y-1:
				search2(x-1,y-1,p2[x,y]) #左下
			if xmin<=x-1:
				search2(x-1,y,p2[x,y]) #左
			if xmin<=x-1 and y+1<=y2_3:
				search2(x-1,y+1,p2[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search3(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p3[x,y]-z)<=gap:
			global c3
			c3+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=ymax:
				search3(x,y+1,p3[x,y]) #上
			if x+1<=x1_2 and y+1<=ymax:
				search3(x+1,y+1,p3[x,y]) #右上
			if x+1<=x1_2:
				search3(x+1,y,p3[x,y]) #右
			if x<=x1_2 and y2_3<=y-1:
				search3(x+1,y-1,p3[x,y]) #右下
			if y2_3<=y-1:
				search3(x,y-1,p3[x,y]) #下
			if xmin<=x-1 and y2_3<=y-1:
				search3(x-1,y-1,p3[x,y]) #左下
			if xmin<=x-1:
				search3(x-1,y,p3[x,y]) #左
			if xmin<=x-1 and y+1<=ymax:
				search3(x-1,y+1,p3[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search4(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p4[x,y]-z)<=gap:
			global c4
			c4+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=y1_2:
				search4(x,y+1,p4[x,y]) #上
			if x+1<=x2_3 and y+1<=y1_2:
				search4(x+1,y+1,p4[x,y]) #右上
			if x+1<=x2_3:
				search4(x+1,y,p4[x,y]) #右
			if x<=x2_3 and ymin<=y-1:
				search4(x+1,y-1,p4[x,y]) #右下
			if ymin<=y-1:
				search4(x,y-1,p4[x,y]) #下
			if x1_2<=x-1 and ymin<=y-1:
				search4(x-1,y-1,p4[x,y]) #左下
			if x1_2<=x-1:
				search4(x-1,y,p4[x,y]) #左
			if x1_2<=x-1 and y+1<=y1_2:
				search4(x-1,y+1,p4[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search5(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p5[x,y]-z)<=gap:
			global c5
			c5+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=y2_3:
				search5(x,y+1,p5[x,y]) #上
			if x+1<=x2_3 and y+1<=y2_3:
				search5(x+1,y+1,p5[x,y]) #右上
			if x+1<=x2_3:
				search5(x+1,y,p5[x,y]) #右
			if x<=x2_3 and y1_2<=y-1:
				search5(x+1,y-1,p5[x,y]) #右下
			if y1_2<=y-1:
				search5(x,y-1,p5[x,y]) #下
			if x1_2<=x-1 and y1_2<=y-1:
				search5(x-1,y-1,p5[x,y]) #左下
			if x1_2<=x-1:
				search5(x-1,y,p5[x,y]) #左
			if x1_2<=x-1 and y+1<=y2_3:
				search5(x-1,y+1,p5[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search6(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p6[x,y]-z)<=gap:
			global c6
			c6+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=ymax:
				search6(x,y+1,p6[x,y]) #上
			if x+1<=x2_3 and y+1<=ymax:
				search6(x+1,y+1,p6[x,y]) #右上
			if x+1<=x2_3:
				search6(x+1,y,p6[x,y]) #右
			if x<=x2_3 and y2_3<=y-1:
				search6(x+1,y-1,p6[x,y]) #右下
			if y2_3<=y-1:
				search6(x,y-1,p6[x,y]) #下
			if x1_2<=x-1 and y2_3<=y-1:
				search6(x-1,y-1,p6[x,y]) #左下
			if x1_2<=x-1:
				search6(x-1,y,p6[x,y]) #左
			if x1_2<=x-1 and y+1<=ymax:
				search6(x-1,y+1,p6[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search7(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p7[x,y]-z)<=gap:
			global c7
			c7+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=y1_2:
				search7(x,y+1,p7[x,y]) #上
			if x+1<=xmax and y+1<=y1_2:
				search7(x+1,y+1,p7[x,y]) #右上
			if x+1<=xmax:
				search7(x+1,y,p7[x,y]) #右
			if x<=xmax and ymin<=y-1:
				search7(x+1,y-1,p7[x,y]) #右下
			if ymin<=y-1:
				search7(x,y-1,p7[x,y]) #下
			if x2_3<=x-1 and ymin<=y-1:
				search7(x-1,y-1,p7[x,y]) #左下
			if x2_3<=x-1:
				search7(x-1,y,p7[x,y]) #左
			if x2_3<=x-1 and y+1<=y1_2:
				search7(x-1,y+1,p7[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search8(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p8[x,y]-z)<=gap:
			global c8
			c8+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=y2_3:
				search8(x,y+1,p8[x,y]) #上
			if x+1<=xmax and y+1<=y2_3:
				search8(x+1,y+1,p8[x,y]) #右上
			if x+1<=xmax:
				search8(x+1,y,p8[x,y]) #右
			if x<=xmax and y1_2<=y-1:
				search8(x+1,y-1,p8[x,y]) #右下
			if y1_2<=y-1:
				search8(x,y-1,p8[x,y]) #下
			if x2_3<=x-1 and y1_2<=y-1:
				search8(x-1,y-1,p8[x,y]) #左下
			if x2_3<=x-1:
				search8(x-1,y,p8[x,y]) #左
			if x2_3<=x-1 and y+1<=y2_3:
				search8(x-1,y+1,p8[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
def search9(x,y,z):
	#探索済みかどうか
	try:
		if reached[x,y]:
			return
			#隣接点との差の判定
	except KeyError:
		pass
	try:
		if math.fabs(p9[x,y]-z)<=gap:
			global c9
			c9+=1
			#もうこないからねー
			reached[x,y]=True
			#8近傍を試す
			if y+1<=ymax:
				search9(x,y+1,p9[x,y]) #上
			if x+1<=xmax and y+1<=ymax:
				search9(x+1,y+1,p9[x,y]) #右上
			if x+1<=xmax:
				search9(x+1,y,p9[x,y]) #右
			if x<=xmax and y2_3<=y-1:
				search9(x+1,y-1,p9[x,y]) #右下
			if y2_3<=y-1:
				search9(x,y-1,p9[x,y]) #下
			if x2_3<=x-1 and y2_3<=y-1:
				search9(x-1,y-1,p9[x,y]) #左下
			if x2_3<=x-1:
				search9(x-1,y,p9[x,y]) #左
			if x2_3<=x-1 and y+1<=ymax:
				search9(x-1,y+1,p9[x,y]) #左上
		else:
			edge[x,y]=True
			return
	except KeyError:
		return
	

input_filename='kesssson41.dat'

with open(input_filename,'r') as dat_file:
	data = dat_file.readlines()


input_data = open(input_filename)

i=0
x=[]
y=[]
z=[]

# 一行ずつ読み込んでは表示する
for rows in input_data:
	result=rows.lstrip()
	row = result.split()
	ztmp=float(row[2])
	x.append(float(row[0]))
	y.append(float(row[1]))
	z.append(ztmp)
input_data.close()
point=[x,y,z]

xsize=len(x)
ysize=len(y)
xmin=min(x)
xmax=max(x)
ymin=min(y)
ymax=max(y)
x1_2=xmin+(xmax-xmin)//3
x2_3=x1_2+(xmax-xmin)//3
y1_2=ymin+(ymax-ymin)//3
y2_3=y1_2+(ymax-ymin)//3



p={0:-9999}
p1={0:-9999}
p2={0:-9999}
p3={0:-9999}
p4={0:-9999}
p5={0:-9999}
p6={0:-9999}
p7={0:-9999}
p8={0:-9999}
p9={0:-9999}
reached={0:-9999}
edge={0:-9999}
z1=[]
z2=[]
z3=[]
z4=[]
z5=[]
z6=[]
z7=[]
z8=[]
z9=[]


for i in range(xsize):
	p[int(point[0][i]),int(point[1][i])]=point[2][i]
	if point[0][i]<x1_2 and point[1][i]<y1_2:
		p1[int(point[0][i]),int(point[1][i])]=point[2][i]
		z1.append(point[2][i])
	elif point[0][i]<x1_2 and point[1][i]<y2_3:
		p2[int(point[0][i]),int(point[1][i])]=point[2][i]
		z2.append(point[2][i])
	elif point[0][i]<x1_2:
		p3[int(point[0][i]),int(point[1][i])]=point[2][i]
		z3.append(point[2][i])
	elif point[0][i]<x2_3 and point[1][i]<y1_2:
		p4[int(point[0][i]),int(point[1][i])]=point[2][i]
		z4.append(point[2][i])
	elif point[0][i]<x2_3 and point[1][i]<y2_3:
		p5[int(point[0][i]),int(point[1][i])]=point[2][i]
		z5.append(point[2][i])
	elif point[0][i]<x2_3:
		p6[int(point[0][i]),int(point[1][i])]=point[2][i]
		z6.append(point[2][i])
	elif point[1][i]<y1_2:
		p7[int(point[0][i]),int(point[1][i])]=point[2][i]
		z7.append(point[2][i])
	elif point[1][i]<y2_3:
		p8[int(point[0][i]),int(point[1][i])]=point[2][i]
		z8.append(point[2][i])
	else:
		p9[int(point[0][i]),int(point[1][i])]=point[2][i]
		z9.append(point[2][i])
			
	reached[int(point[0][i]),int(point[1][i])]=False
	edge[int(point[0][i]),int(point[1][i])]=False
	
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
	
for k in range(1000):
	startz1=min(z1)
	startz2=min(z2)
	startz3=min(z3)
	startz4=min(z4)
	startz5=min(z5)
	startz6=min(z6)
	startz7=min(z7)
	startz8=min(z8)
	startz9=min(z9)

	for i in range(xsize):
		if point[0][i]<x1_2 and point[1][i]<y1_2:
			if point[2][i]==startz1:
				startx1=point[0][i]
				starty1=point[1][i]
		elif point[0][i]<x1_2 and point[1][i]<y2_3:
			if point[2][i]==startz2:
				startx2=point[0][i]
				starty2=point[1][i]
		elif point[0][i]<x1_2:
			if point[2][i]==startz3:
				startx3=point[0][i]
				starty3=point[1][i]
		elif point[0][i]<x2_3 and point[1][i]<y1_2:
			if point[2][i]==startz4:
				startx4=point[0][i]
				starty4=point[1][i]
		elif point[0][i]<x2_3 and point[1][i]<y2_3:
			if point[2][i]==startz5:
				startx5=point[0][i]
				starty5=point[1][i]
		elif point[0][i]<x2_3:
			if point[2][i]==startz6:
				startx6=point[0][i]
				starty6=point[1][i]
		elif point[1][i]<y1_2:
			if point[2][i]==startz7:
				startx7=point[0][i]
				starty7=point[1][i]
		elif point[1][i]<y2_3:
			if point[2][i]==startz8:
				startx8=point[0][i]
				starty8=point[1][i]
		else:
			if point[2][i]==startz9:
				startx9=point[0][i]
				starty9=point[1][i]
				
	

	

	
	search1(startx1,starty1,startz1)
	search2(startx2,starty2,startz2)
	search3(startx3,starty3,startz3)
	search4(startx4,starty4,startz4)
	search5(startx5,starty5,startz5)
	search6(startx6,starty6,startz6)
	search7(startx7,starty7,startz7)
	search8(startx8,starty8,startz8)
	search9(startx9,starty9,startz9)
	
	r=(c1+c2+c3+c4+c5+c6+c7+c8+c9)*100/xsize
	
	
	
	
	z1=[i for i in z1 if i!=startz1]
	z2=[i for i in z2 if i!=startz2]
	z3=[i for i in z3 if i!=startz3]
	z4=[i for i in z4 if i!=startz4]
	z5=[i for i in z5 if i!=startz5]
	z6=[i for i in z6 if i!=startz6]
	z7=[i for i in z7 if i!=startz7]
	z8=[i for i in z8 if i!=startz8]
	z9=[i for i in z9 if i!=startz9]
	
	if k%100==0:
		print("Stage:",k)
	
print("Area1:")
print(c1,"\nArea2:")
print(c2,"\nArea3:")
print(c3,"\nArea4:")
print(c4,"\nArea5:")
print(c5,"\nArea6:")
print(c6,"\nArea7:")
print(c7,"\nArea8:")
print(c8,"\nArea9:")
print(c3)
print("Ground:",r,"%")
print("Billding:",100-r,"%")



jimen=open('jimen41.dat','w')
tatemono=open('tatemono41.dat','w')
for i in range(xsize):
	if reached[int(point[0][i]),int(point[1][i])]:
		jimen.write(str(point[0][i]))
		jimen.write(" ")
		jimen.write(str(point[1][i]))
		jimen.write(" ")
		jimen.write(str(p[int(point[0][i]),int(point[1][i])]))
		jimen.write("\n")
		tatemono.write(str(point[0][i]))
		tatemono.write(" ")
		tatemono.write(str(point[1][i]))
		tatemono.write(" ")
		tatemono.write("-0.1")
		tatemono.write("\n")
	elif edge[int(point[0][i]),int(point[1][i])]:
		for dx in range(-1,2):
			for dy in range(-1,2):
				try:
					if reached[int(point[0][i]+dx),int(point[1][i]+dy)]:
						tatemono.write(str(point[0][i]+dx*0.00001))
						tatemono.write(" ")
						tatemono.write(str(point[1][i]+dy*0.00001))
						tatemono.write(" ")
						tatemono.write(str(p[int(point[0][i]+dx),int(point[1][i]+dy)]))
						tatemono.write("\n")
				except KeyError:
					pass
	else:
		tatemono.write(str(point[0][i]))
		tatemono.write(" ")
		tatemono.write(str(point[1][i]))
		tatemono.write(" ")
		tatemono.write(str(p[int(point[0][i]),int(point[1][i])]))
		tatemono.write("\n")
		jimen.write(str(point[0][i]))
		jimen.write(" ")
		jimen.write(str(point[1][i]))
		jimen.write(" ")
		jimen.write("0")
		jimen.write("\n")
jimen.close()
tatemono.close()
