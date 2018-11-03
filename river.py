
import math
import numpy
day=numpy.matrix([[0,31],[31,60],[59,90],[90,120],[120,151],[151,181],[181,212],[212,243],[243,273],[273,304],[304,334],[334,365]])
print("Enter the month's number for which you want to calculate the Standard Deviation")
print("1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9.September\n10.October\n11.November\n12.December")
def variance(c, n):
	sum = 0
	for i in range(0, n):
		sum += c[i]
	mean = sum / n
	sqDiff = 0
	for i in range(0, n):
		sqDiff += ((c[i]) - mean)*(c[i]-mean)
		return sqDiff / n

def standardDeviation(arr, n):
	return math.sqrt(variance(arr, n))

data={}
for i in range(1901,2014):
	with open("kaveri/rfp_"+str(i)+".TXT") as f:
		a = [x.replace(" ", "").split("\t") for x in f.readlines()]
	b = []
	for line in a:
		line.remove("\n")
		array = [float(x) for x in line]
		b.append(array)
	data[i] = b

with open("Cauvery/date_matrix.txt") as f2:
    z = f2.readlines()


#date = []
#for line in z:
  #  array = [int(x) for x in line[:-1].split("	")]
 #   date.append(array)

#date = np.asarray(date)
#print(date[:][:])
#i1 = float(input())

m=eval(input(""))
if m<1 or m>12:
	print("Run the program again")
	exit()
m-=1;
f=open ('data.txt','w')
arr = []
sd = []
for j in range(day[m,0],day[m,1]):
	for k in range(0,116):
		for i in range(1901,2014):
			if i%4 == 0 and m>1:
				t=j+1
			elif i%4!=0 and m==1 and j==59:
				continue
			else:
				t=j 
			arr.append(data[i][t][k])		
		sd.append(standardDeviation(arr,len(arr)))	
		arr = []
# print(len(sd))
d=int(len(sd)/116)
for i in range(0,d):
	for j in range(0,116):
		f.write(str(sd[(i*116)+j])+" ")
	f.write("\n")


f.close()
# f=open ('data1.txt','w')
# arr = []
# sd = []
# for j in range(day[m,0],day[m,1]):
# 	for k in range(0,116):
# 		for i in range(1901,2014):
# 			if i%4 == 0 and m>1:
# 				t=j+1
# 			elif i%4!=0 and m==1 and j==59:
# 				continue
# 			else:
# 				t=j 
# 			arr.append(data[i][t][k])		
# 		sd.append(standardDeviation(arr,len(arr)))	
# 		arr = []
# # print(len(sd))
# d=int(len(sd)/116)
# # print(d)

# for i in range(0,d):
# 	for j in range(0,116):
# 		# f.write("abc")
# 		f.write(str(sd[(i*116)+j])+" ")
# 	f.write("\n")
# f.close()


