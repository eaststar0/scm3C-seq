#description: Joins 2 files into one with matching 1st column. If one misses data, mark "NA"
#Usage: python Join_two_files.py file1 file2 output

import sys                                                             
import os

fn1=sys.argv[1].split('/')[-1]
fn2=sys.argv[2].split('/')[-1]
dfh1=open(fn1,'r')
dfh2=open(fn2,'r')
line1=dfh1.readline().split()
line2=dfh2.readline().split()
o1=[]
o2=[]
count=0
for i in line1[1:]:
        o1.append(str(count+2))
        count+=1
count=0
for i in line2[1:]:
        o2.append(str(count+2))
        count+=1
command="join -a1 -a2 -e '0' -o 0"
for i in o1:
        command+=',1.'+i
for i in o2:
        command+=',2.'+i
dfh1.close()
dfh2.close()
os.system(command+' '+fn1+' '+fn2+' > '+sys.argv[3])
