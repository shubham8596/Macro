import sys
import os
fp=open(sys.argv[1],"r")
fp1=fp.readlines()
l=len(fp1)
fw=open("mntandmdt.txt","w")
fw.write("\t\t\t*** Macro Name Table ***\t\t\n\n")
fw.write("macro_name\tParameters\tStart\tEnd\n")
fw.write("------------------------------------------------\n")
macro_nm=[]
zz=[]
for i in range(0,l):
	if '%macro' in fp1[i]:
		f=fp1[i].split()
		ps=f[2].split(',')
		macro_nm.append(f[1])
		j=i
		
	if '%endmacro' in fp1[i]:
		fw.write(("%s\t%d\t\t%d\t%d"%(f[1],len(ps),j,i))+os.linesep)

fw.write(("\n\n\n\n")+os.linesep)
fw.write("\t\t\t*** Macro Defination Table ***\t\t\n\n")
fw.write("Macro defination\tStart\tEnd\n")
fw.write("------------------------------------------------\n")

for i in range(0,l):
	if '%macro' in fp1[i]:
		j=i		
	if '%endmacro' in fp1[i]:
		n=i
		az=fp1[1]
		aa=az.split()
		fw.write("\n\n%s\t%d\t%d\n"%(aa,j,n))
		for k in range(j+2,n):
			zz.append(fp1[k])
			fw.write("%s"%(fp1[k]))


