def Nucleotide_content_calculator(self):
    gene = self.upper()
    import re
    A_num = re.findall('A',gene)
    C_num = re.findall('C',gene)
    G_num = re.findall('G',gene)
    T_num = re.findall('T',gene)
    con_A = len(A_num) / len(gene)
    con_C = len(C_num) / len(gene)
    con_G = len(G_num) / len(gene)
    con_T = len(T_num) / len(gene)
    print(f'the concentration of A is {con_A}')
    print(f'the concentration of C is {con_C}')
    print(f'the concentration of G is {con_G}')
    print(f'the concentration of T is {con_T}')
gene_seq = input('please input the gene seqences:')
Nucleotide_content_calculator(gene_seq)
