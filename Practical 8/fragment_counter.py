seq = "ATGCAATCGACTACGATCAATCGAGGGCC"
seq1 = "GAATTC"
import re
if len(re.findall(seq1, seq)) == 0:
    print("there will be one fragment")
else:
    print(f"there will be {len(re.findall(seq1, seq))} fragments")
