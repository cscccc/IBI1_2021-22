import re
import pandas as pd
sequence = ''
def read_file(file):
    for lines in file:
        if not lines.startswith('>'):
            sequence = lines
    sequence = re.sub(' ','',sequence)
    sequence = re.sub(r'\n','',sequence)
    return sequence
# define a function to read the file, and only return amino acid sequence, excluding amino acid name.

f1 = read_file(open("DLX5_human.fa"))
print(f1)
f2 = read_file(open("DLX5_mouse.fa"))
print(f2)
f3 = read_file(open("RandomSeq.fa"))
print(f3)
# Read the 3 files and extract their DNA sequence


BLOSUM_62 = {'A':[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,0,-4],'R':[-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0,-1,-4],
           'N':[-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0,-1,-4],'D':[-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1,-1,-4],
           'C':[0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3,-2,-4],'Q':[-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3,-1,-4],
           'E':[-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],'G':[0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2,-1,-4],
           'H':[-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0,-1,-4],'I':[-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3,-1,-4],
           'L':[-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3,-1,-4],'K':[-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1,-1,-4],
           'M':[-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1,-1,-4],'F':[-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3,-1,-4],
           'P':[-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1,-2,-4],'S':[1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0,0,-4],
           'T':[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,0,-4],'W':[-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3,-2,-4],
           'Y':[-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2,-1,-4],'V':[0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2,-1,-4],
           'B':[-2,-1,3,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1,-1,-4],'Z':[-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
           'X':[0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1,-1,-4],'*':[-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]}
# Read BLOSUM_62. Obtained from the "https://github.com/Raha-Kheirinia/BLOSUM62/blob/master/BLOSUM62.txt" and write them in a dictionary
BLOSUM_62 = pd.DataFrame(BLOSUM_62, columns = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'],
                       index = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'])
# pd.DataFrame is a function that can turn the dictionary format into the dataframe format, so we can see it clearly
print(BLOSUM_62)
sum_score1 = 0
# Give it an initial value
for i in range(len(f1)):
    score1 = BLOSUM_62.loc[f1[i], f2[i]]
    sum_score1 = sum_score1 + score1
print("The score for alignment in human and mouse DLX5 sequence is:", sum_score1)
# sum_score1 is used to give the score for the alignment in human and mouse DLX5 sequence
sum_score2 = 0
# Give it an initial value
for i in range(len(f1)):
    score2 = BLOSUM_62.loc[f1[i], f3[i]]
    sum_score2 = sum_score2 + score2
print("The score for alignment in human DLX5 and random sequence is:", sum_score2)
# sum_score1 is used to give the score for the alignment in human  DLX5 and random sequence
sum_score3 = 0
# Give it an initial value
for i in range(len(f1)):
    score3 = BLOSUM_62.loc[f2[i], f3[i]]
    sum_score3 = sum_score3 + score3
print("The score for alignment in mouse DLX5 and random sequence is:", sum_score3)
# sum_score1 is used to give the score for the alignment in mouse  DLX5 and random sequence

similarity1 = 0
for i in range(len(f1)):
    if f1[i] == f3[i]:
        similarity1 = similarity1 + 1
identical_percentage1 = similarity1/len(f1)
print("The identical percentage of DLX5 in human and random sequence is:", identical_percentage1)
similarity2 = 0
for i in range(len(f2)):
    if f2[i] == f3[i]:
        similarity2 = similarity2 + 1
identical_percentage2 = similarity2/len(f2)
print("The identical percentage of DLX5 in mouse and random sequence is:", identical_percentage2)
similarity3 = 0
for i in range(len(f1)):
    if f1[i] == f2[i]:
        similarity3 = similarity3 + 1
identical_percentage3 = similarity3/len(f1)
print("The identical percentage of DLX5 in mouse and in human is:", identical_percentage3)
# Calculate the identical percentage of these amino acid sequence and print them

