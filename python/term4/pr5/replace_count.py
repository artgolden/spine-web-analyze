f = open("dros_seq.gvf", 'r')

AT = 0
GC = 0
TA = 0
CG = 0

for i in f:
    if i[0] == '2':
        ar = i.split('\t')
        # print ar
        for j in range(8):
            ar.pop(0)
        ln = ar[0]
        # print ln
        # Get positions of all '=' in the line
        p = [pos for pos, char in enumerate(ln) if char == '='] 
        # print p
        if ln[p[1] + 1] =='A' and ln[p[-1] + 1] == 'T':
            AT += 1
        elif  ln[p[1] + 1] =='G' and ln[p[-1] + 1] == 'C':
            GC += 1
        elif  ln[p[1] + 1] =='T' and ln[p[-1] + 1] == 'A':
            TA += 1
        elif  ln[p[1] + 1] =='C' and ln[p[-1] + 1] == 'G':
            CG += 1
print " A -> T: {}\n G -> C: {}\n T -> A: {}\n C -> G: {}".format(
    AT, GC, TA, CG)
