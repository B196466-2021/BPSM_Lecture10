#!/usr/local/bin/python3
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
at_content = (my_dna.count('A') + my_dna.count('T')) / len(my_dna)
print("A+T content is",str(int(100*at_content)),"percent")
