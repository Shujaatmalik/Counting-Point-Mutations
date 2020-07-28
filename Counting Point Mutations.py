# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:25:53 2020

@author: Shujaat

"""
String1="CCCTCAGGTTAGCCATACGGAAGGGCATTCCCTAGGTAGAGTTGTTTGATAC"
String2="TCCTCCGTTTACAACTCTGGAAGTCCTTATCCTTGGTAGACGTGTTGGTTTT"
def Point_Mutations(String1,String2):
    
    counter=0
    for i in range(len(String1)):
        if(len(String1)!=len(String2)):
            print("Strings are not Equal")
            break
        elif(String1[i]!=String2[i]):
            counter=counter+1
    return counter        

c=Point_Mutations(String1,String2)
print("Counter is:",c)
        



