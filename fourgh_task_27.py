import os
name_of_file = 'data.txt'
total_number = 0

def Sequence(filename):
    file = open(filename, 'r')
    m = 0
    f = 0
    cur = 0
    try:
        f=open(filename, "r")
        for s in [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']: 
            if(s==0):
                try:
                    cur=int(s)
                except:
                    print('word ',s,' ignored',sep='')
            else:
                try:
                    integer=int(s)
                except:
                    print('word ',s,' ignored',sep='')
                if (integer == cur):
                    if(f==0):
                        m = m+2
                        f=1
                        cur = integer
                    elif  (f == 1):
                        m += 1
                        cur = integer
                if (int(s) != cur):
                    f=0
                    cur = int(s)
        file.close()
        return m
    except FileNotError:
        return None

total_number = Sequence(name_of_file)

if (total_number == 0):
    print("answer 0")
elif (total_number > 0):
    print("answer is", total_number)
elif (total_number == None):
    print("Can't open file")
