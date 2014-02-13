# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
import random
def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output

#dna= 'ATGATGTGAATGATTGCTTGA'
def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    amino_acid=""
    for i in range(0, len(dna), 3):
        mycodon=dna[i:i+3]
       # print'this is my codon'
        #print mycodon
        for j in range(len(codons)):
            for k in range(len(codons[j])):
                #print codons[j][k]
                if codons[j][k] == mycodon:
                    #print aa[j]
                    amino_acid += aa[j]
    return amino_acid
                    
    #step uno break apart string into groups of three
    #find sequence +find index
    #then connect to amino acids 
    
        
#print coding_strand_to_AA(dna)
#    

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    input_a='ATTATTATT'
    expected_output='III'
    actual_output=coding_strand_to_AA(input_a)
    print 'Expected Output is ' + expected_output
    print 'Actual Output is ' +actual_output
    
    input_a='ATGATGATT'
    expected_output='MMI'
    actual_output=coding_strand_to_AA(input_a)
    print 'Expected Output is ' + expected_output
    print 'Actual Output is ' +actual_output
    
    # YOUR IMPLEMENTATION HERE

print coding_strand_to_AA_unit_tests()

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
            sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    L=dna
    rdna=L[::-1]
    print rdna
    newrdna=""
    for i in range(0,len(rdna)):
            if rdna[i]=='A':
                newrdna='T'+newrdna
            elif rdna[i]=='G':
                newrdna='C'+newrdna
            elif rdna[i]=='T':
                newrdna='A'+newrdna
            elif rdna[i]=='C':
                newrdna='G'+newrdna
    S=newrdna
    P=S[::-1]
    return P
    
#print get_reverse_complement(dna)

def get_reverse_complement_unit_tests():

    """ Unit tests for the get_complement function """
    input_a='ATTATTATT'
    expected_output='AATAATAAT'
    actual_output=get_reverse_complement(input_a)
    print 'Expected Output is ' + expected_output
    print 'Actual Output is ' +actual_output
    
    input_a='ATTCATATT'
    expected_output='AATATGAAT'
    actual_output=get_reverse_complement(input_a)
    print 'Expected Output is ' + expected_output
    print 'Actual Output is ' +actual_output
            

print get_reverse_complement_unit_tests()
        
    
    # YOUR IMPLEMENTATION HERE    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence   input_a='ATTCATCATCATCATTAG'
    expected_output='ATTCATCATCATCAT'
    actual_output=rest_of_ORF(input_a)
    print 'Expected Output is ' + expected_output
    print 'Actual Output is ' +actual_output
        returns: the open reading frame represented as a string
    """
    STOP_CODONS=['TAG','TGA','TAA' ]#constants are uppercase
    for i in range(0,len(dna),3):
        codon=dna[i:i+3]
        if codon in STOP_CODONS:
            return dna[0:i]
    return dna
    
#print rest_of_ORF(dna)


def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    input_a='ATTCATTAG'
    expected_output='ATTCAT'
    actual_output=rest_of_ORF(input_a)
    print 'Expected Output is ' + expected_output
    print 'Actual Output is ' +actual_output
    
    input_a='ATTCATCATCATCATTAG'
    expected_output='ATTCATCATCATCAT'
    actual_output=rest_of_ORF(input_a)
    print 'Expected Output is ' + expected_output
    print 'Actual Output is ' +actual_output

    
print rest_of_ORF_unit_tests()
        
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and 
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """ 
    i=0
    multiple_list=[]
    while i < len(dna):
        part = dna[i:i+3]
        if part == 'ATG':    #if the first indecied are ATG then it runs the code that creates the string of DNA
            ORF=rest_of_ORF(dna[i:]) 
            multiple_list.append(ORF)
            i+=len(ORF)
        else:
            i+=3
    # print multiple_list
    return multiple_list
   
            #runs fuinction to mmake list of function
            #need to save to list
            #need to continue to next ATG start 
            #need to add that to list
            #need to output new list as commas between lists
            
#print find_all_ORFs_oneframe(dna)            
    
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    input_a='ATGATTATTTGATGAATGGATTGA'
    expected_output='[ATGATTATT,ATGGAT]'
    actual_output=find_all_ORFs_oneframe(input_a)
    print 'Expected Output is ' + expected_output
    print  actual_output
    
    input_a='ATGGGATTGTTT'
    expected_output='[ATGGATTGTTT]'
    actual_output=find_all_ORFs_oneframe(input_a)
    print 'Expected Output is ' + expected_output
    print  actual_output
    
print find_all_ORFs_oneframe_unit_tests()

    # YOUR IMPLEMENTATION HERE

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    #these functions offset to analyze each each open frame reference
    zero_offset=find_all_ORFs_oneframe(dna[0:])
    
    one_offset=find_all_ORFs_oneframe(dna[1:])
   
    two_offset=find_all_ORFs_oneframe(dna[2:])
    
    return zero_offset+one_offset+two_offset
   
    # YOUR IMPLEMENTATION HERE
#print find_all_ORFs(dna)

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    print 'Begin Unit test Find_all_ORFs'
    input_a='ATGCATGAATGTAGATGTAG'
    expected_output='[ATGCATGAATGTAGATGTAG, ATGAATGTAGATGTAG, ATG, ATG]'
    actual_output=find_all_ORFs(input_a)
    print 'Expected Output is ' + expected_output
    print  actual_output
    
    input_a='ATGCATGAATGTAGATGCATCATTAG'
    expected_output='[ATGCATGAATGTAGATGCATCATTAG, ATGAATGTAGATGCATCATTAG, ATG, ATGCATCAT]'
    actual_output=find_all_ORFs(input_a)
    print 'Expected Output is ' + expected_output
    print  "actucal OUtput is", actual_output
    print 'ENd Unit test Find_all_ORFs'
print find_all_ORFs_unit_tests()
        
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs(dna)+find_all_ORFs(get_reverse_complement(dna))
    
     
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    print ''
    print 'Begin Unit test Find_all_ORFs both tests'
    input_a='ATGCGAGGGTAGATGGATTAG'
    expected_output='[ATGCGAGGG, ATGGAT]'
    actual_output=find_all_ORFs_both_strands(input_a)
    print 'Expected Output is ' + expected_output
    print  actual_output
    
    
    input_a='ATGCGAATGTAGCATCAAATAGATGTAG'
    expected_output='[ATGCGAATG, ATG, ATGCTACATTCGCAT]'
    actual_output=find_all_ORFs_both_strands(input_a)
    print 'Expected Output is ' + expected_output
    print  actual_output    
    print 'end'
    print ''
print find_all_ORFs_both_strands_unit_tests()

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    both_strings=find_all_ORFs_both_strands(dna)
    L=max(both_strings,key=len)
    Q=len(L)
    return Q

        #save out put of find all orfboth string to some variable
        

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    input_a="ATGCGAATGTAGCATCAAA"
    expected_output=''
    actual_output=longest_ORF(input_a)
    print 'Expected Output is ' + expected_output
    print "actual output: ", actual_output

print longest_ORF_unit_tests()

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    list_dna=list(dna)
    random.shuffle(list_dna)#just shuffles original list, doesn't return, not fruitful
    random_string_dna=collapse(list_dna)
    longest_dna=longest_ORF(random_string_dna)
    return longest_dna
    dna= 'ATGATGTGAATGATTGCTTGA'
#print longest_ORF_noncoding(dna, 10)


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    
    List_of_dna=find_all_ORFs_both_strands(dna)
    aa_list=[]
    for string in List_of_dna:
        if len(string)< threshold:
            continue
        else:
            aa_list.append(coding_strand_to_AA(string))
    return aa_list
#print gene_finder(dna,10)
#    return [coding_strand_to_AA(string) for string in List_of_dna]
if __name__=="__main__":
    from load import load_seq
    dna = load_seq("./data/X73525.fa")
#    
    # YOUR IMPLEMENTATION HERE
    
    #Ryan  Louie, Doyoung Li, James Jang, Casey Alvarado, the list kinda goes on. and the ninjas