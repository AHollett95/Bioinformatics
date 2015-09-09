__author__ = 'Austin Hollett'
#%matplotlib inline
import numpy
import matplotlib.pyplot as plt

sample = open('C:\\Users\\Austin\\smel-aug2015\\sample.gff3', 'r')
for line in sample:
    if "\tgene\t" in line:
          values = line.split('/t')
          #start = int(values[3])
          #end = int(values[4])
          #length = end - start + 1

with open('C:\Users\Austin\smel-aug2015\s_meliloti.gff3', 'r') as f:
    GFF = [line.rstrip() for line in f]
with open('C:\Users\Austin\smel-aug2015\s_meliloti.fa', 'r') as g:
    fasta = str(map(lambda x: ''.join(g), g))

def countC(string):
    c = string.count('C')
    return int(c)
def countG(string):
    g = string.count('G')
    return int(g)

xaxis = []
yaxis = []
for line in GFF:
    if "\tgene\t" in line:
        values = line.split('\t')               #splits strings from the tabs
        start = int(values[3])                  #start value is taken here
        end = int(values[4])                    #end value of gene is taken here
        length = end - start + 1                #computed length from end - start + 1 because of 0 default
        xaxis.append(length)                    #adds length to x-axis list
        temp = fasta[start:end]                 #gets string of gene from start value to end value
        Ccount = countC(temp)                   #returns how many C's there are
        Gcount = countG(temp)                   #returns how many G's there are
        GC = (Gcount + Ccount) / float(length)  #calculates the GC
        yaxis.append(GC)                        #adds GC to y-axis list

print xaxis
print yaxis

plt.scatter(xaxis,yaxis)
plt.ylabel("GC Content")
plt.xlabel("Length of Gene")

plt.show()