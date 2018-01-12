
import sys, json, numpy as np
test = ["a", "t", "c", "g"]
from seqMatchers import matchers as Matchers

def writeDna(dna = str):
 
   seq =[]
   aminoAcid = []  
   for i in range(1, len(dna)-1):
        
        if dna[i] == test[0] or dna[i]==test[1] or dna[i]==test[2] or dna[i]==test[3]:
         x = ""
         codingLine = dna[i]              
         template = Matchers.dnaMatch(codingLine) 
         rna = Matchers.rnaMatch(template)
         seq.append({ "location": i, "coding" : codingLine, "template": template, "rna": rna })
                 
          
        else:
         print "error"  
  
   print seq      
   return seq 


#Read data from stdin
def read_in():
    
    lines = sys.stdin.readlines()
         
    dna = writeDna(lines[0])
    
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(dna)

def main():
    #get our data as an array from read_in()
    lines = read_in()
    print lines 
    #create a numpy array
    np_lines = np.array(lines)
    
    #use numpys sum method to find sum of all elements in the array
    lines_sum = np.sum(np_lines)

    #return the sum to the output stream
    print lines_sum
    
#start process
if __name__ == '__main__':
    main()