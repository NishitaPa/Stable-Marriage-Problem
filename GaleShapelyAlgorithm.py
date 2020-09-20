#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:43:59 2020

"""
t = int(input('Enter number of males or females:'))
n = int(2*t)
preference_list = []
print('Enter preference list row wise:')
for i in range(0,n):
    a = []
    for j in range(0,t):
        a.append(int(input()))
    preference_list.append(a)
        
        
for i in range(0,n):
    for j in range(0,t):
        print(preference_list[i][j],' ', end = '')
    print()
  
def preferm1overm(w,m1,m):
    if (preference_list[w].index(m1) < preference_list[w].index(m)):
        preferm1overm = True
    else:
        preferm1overm = False
    return preferm1overm


men_list=[]
Engage_list = []
mFree=[]
for i in range(0,t):
    mFree.append(True)
    Engage_list.append(-1)
    men_list.append(i)
freecount = t
while freecount!=0:
    for i in men_list:
        if mFree[i]==True:
            print(freecount)
            for j in range(0,t):
                if mFree[i] == True:
                    w = preference_list[i][j]
                    if Engage_list[w-t] == -1:
                        Engage_list[w-t] = i
                        mFree[i] = False
                        freecount=freecount-1
                        print(freecount)
                    for k in (j+1,t):
                        continue
                    else:
                        m2 = Engage_list[w-t]
                    if (preferm1overm(w,i,m2) == True):
                            Engage_list[w-t]= i
                            mFree[i]= False
                            mFree[m2] = True
                            freecount = freecount
                            men_list.append(m2)
                            men_list.remove(i)
print('Women    Men')
for i in range(0,t):
    print(' ', (i+t), '     ',Engage_list[i])
