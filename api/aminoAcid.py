
import sys, json, numpy as np
test = ["a", "t", "c", "g"]
from seqMatchers import matchers as Matchers

def aminoAcidPrecentage(mrna = str):  
    
    aminoAcid = []  
    aminoAcidPrecent = []   
    seq = list(mrna[1:])
    ## every 3 mrna creates the amino acid we need##
    for i in range(0,len(seq)-4,3):
       
       ###mrna = str(seq[i])+ str(seq[i+1]["rna"])+ str(seq[i+2]["rna"])   
       rna = str(seq[i+1]) + str(seq[i+2]) + str(seq[i+3])
       # mrna return the right amino acid
       amino = Matchers.aminoMatch(rna)
       
       aminoAcid.append(amino)
    np_amino = np.array(aminoAcid) 
    
    unique_elements, counts_elements = np.unique(np_amino, return_counts=True)
    
    index = 0
    ## calculate precentage of the each amino in the dna##
    for i in counts_elements:
       
       precentage = float(i)/(len(np_amino))*100
       aminoAcidPrecent.append({ "amino_name" : str(unique_elements[index]), "precentage" : precentage })       
       index = index + 1
        
    print aminoAcidPrecent
    return aminoAcidPrecent   
    
#Read data from stdin
def read_in():
    
    lines = sys.stdin.readlines()     
    aa = aminoAcidPrecentage(lines[0])
    
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(aa)

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