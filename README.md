# Counting-Point-Mutations
Problem
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
# Download Code File
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
