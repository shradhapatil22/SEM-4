import numpy as np
import csv
data = np.loadtxt ( "in.txt" , usecols =range ( 1,4 ) , delimiter = ',' )
print ( " marks data \ n " , data )
avg = np.array ( [ ] )
for mks in data :
    avg = np.append ( avg , round ( np.mean ( mks ) , 2 ) )
for i in avg :
    print ( i )
with open ( "in.txt" ) as inF :
   with open ( " out.txt " , "w" ) as outf:
        reader =csv.reader ( inF )
        i=0
        for line in reader :
            outf.write ( line [ 4 ] +' ' + str ( avg [ i ] ) + ' \ n ' )
print ( " class Topper has scored average mks : " , np.max ( avg ) )