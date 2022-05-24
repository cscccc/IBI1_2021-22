file_name = input("please type the file name:")
f1 = open('/Users/yumenghan/Downloads/IBI/Week 8. Python III Working with Strings/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r').readlines()#需要整理的文件
f2 = open('gene.fasta','w')
f3 = open(f'{file_name}.fa','w')
for i in f1:
    if i.startswith('>'):
        f2.write('\n'+i)
    else:
        f2.write(i.strip("\n"))
Gene = open('/Users/yumenghan/Downloads/IBI/Week 8. Python III Working with Strings/gene.fasta')
Gene_list = []
for line in Gene:
    Gene_list.append(line)
Gene.close()
seq = ''.join(Gene_list)
print(seq)
import re
regular_expression =  '(?<=gene:)[A-Z0-9]*(?<!_mRNA)'
#print(re.findall(regular_expression,seq))
name = re.findall(regular_expression,seq)
regular_expression2 = '[A-Z]{10,}'
print(re.findall(regular_expression2,seq))
only_seq = re.findall(regular_expression2,seq)
seq_num = []
for i in only_seq :
    counter = re.findall("GAATTC",i)
    seq_num.append(f"{len(counter) + 1 }  {i}")
print(seq_num)
result = []
for i in range(0,len(seq_num)):
    result.append(f'{name[i]}     {seq_num[i]}     ')
print(result)
for i in result:
    f3.write(i)
