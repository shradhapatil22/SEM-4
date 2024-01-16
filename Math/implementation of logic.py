import ttg
def main():
ch = 'y'
while(ch == 'y'):
 print("1)(p/\q)\t 2)(p\/q)\t3)~(p->q)\t4)p/\(q\/r)")
 opt = int(input("Enter your choice:"))
 if(opt == 1):
 p,q = map(int,input("Enter value for p and q:").split())
 print("~(p/\q:)",int(not(p and q)))
 elif(opt == 2):
 p,q = map(int,input("Enter value for p and q:").split())
 print("~(p\/q):",int(not(p or q)))
 elif(opt == 3):
 p,q = map(int,input("Enter value for p and q:").split())
 print("~(p->q):",int(p and (not q)))
 elif(opt == 4):
 p,q,r = map(int,input("Enter value for p ,q,r:").split())
 print("p/\(q\/r):",int(p and(q or r)))
 else:
 print("INVALID OPTION!!")
 ch = input("Continue(y/n)?")
 print("\nTruth-table for De-Morgans Law")
 print(ttg.Truths(['p','q'],['(p and q)','(p or q)' ,'~p','~q','~p or ~ q','~p and ~ q']))
 print("\nTruth-table for Negation of conditional law")
 print(ttg.Truths(['p','q'],['~(p=>q)','~q','p and ~q']))
 print('\nTruth-table for distributive law')
8
 print(ttg.Truths(['p','q','r'],['p and(q or r)','(p and q) or(p and r)']))
 if _name=="main_":
 main()