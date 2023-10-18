t=int (input('svp done le nober des etudient:'))
l=[]
for i in range(1,t+1) :
    v = float(input('svp done les valeur des note:'))
    l.append(v)

m = sum(l) /t
print("Les notes supérieures à la moyenne sont :")
for v in l:
    if v>m :
      print(v)







