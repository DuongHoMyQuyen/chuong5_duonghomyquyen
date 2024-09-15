# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:50:23 2024

@author: Student
"""

count= 0
n= int(input("Nhap so ln can lap:"))
while (count<n):
    print("Can lap thu:", count+1, "\tBiendem:", count)
    count= count+1
else:
    print("\nThuc hien lenh trong else, do:", "\ncount=", count, "\nn=", n, "\nbool(count<n)=", bool(count<n))