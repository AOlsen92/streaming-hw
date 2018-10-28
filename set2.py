from nltk.tokenize import word_tokenize
import numpy as np
import numpy.random

def data_stream():
    """Stream the data in 'leipzig100k.txt' """
    with open('leipzig100k.txt', 'r') as f:
        for line in f:
            for w in word_tokenize(line):
                if w.isalnum():
                    yield w
   
def bloom_filter_set():
    """Stream the data in 'Proper.txt' """
    with open('Proper.txt', 'r') as f:
        for line in f:
            yield line.strip()

############### DO NOT MODIFY ABOVE THIS LINE #################



# Implement a universal hash family of functions below: each function from the
# family should be able to hash a word from the data stream to a number in the
# appropriate range needed.
yes = []
padding = '!'
for x in data_stream():
    if len(x) == 0:
        yes.append(x)
    else:
        yes.append(x.ljust(len(x) + (8-(len(x) % 8)),'!'))
    
    
    #listx.append(x.ljust(8,'!'))
ascii1 = [[ord(ch) for ch in word] for word in yes]

m2 = []

for i in range(len(ascii1)):
    m2.append(256**7*ascii1[i][0]+ 256**6 * ascii1[i][1] + 256**5 * ascii1[i][2] + 256**4 *ascii1[i][3] + 256**3 * ascii1[i][4] + 256**2 * ascii1[i][5] + 256 **1 * ascii1[i][6] + 2256**0 * ascii1[i][7])



    

# hab(x)=((ax+b)modp)modm
# ((a*x+b)%p)%m

def uhf(p,m):
    
    
    #p: a very large prime
    #m: size of the table
    
    a = np.random.randint(1,p-1)
    b = np.random.randint(0,p-1)
    return lambda x: ((a * x + b)% p)% m
    
# Returns a hash function that can map a word to a number in the range 0 - rng    
    pass

size = 2**18
p = 2059861
hashes = [np.vectorize(uhf(p,len(m2)))(range(len(m2))) for
                                            _ in range(5)]
############### 

################### Part 1 ######################

from bitarray import bitarray
size = 2**18   # size of the filter

hash_fns = [hashes[0], hashes[1], hashes[2], hashes[3], hashes[4]]  # place holder for hash functions
bloom_filter = []
#num_words =         # number in data stream
#num_words_in_set =   # number in Bloom filter's set

#for word in bloom_filter_set(): # add the word to the filter by hashing etc.
for word in bloom_filter_set():
    bloom_filter.append(word)



#    pass 



#for word in data_stream():  # check for membership in the Bloom filter
#    pass 

print('Total number of words in stream = %s'%(len(ascii1),))
print('Total number of words in stream = %s'%(len(bloom_filter),))
      
################### Part 2 ######################

hash_range = 24 # number of bits in the range of the hash functions
fm_hash_functions = [None]*35  # Create the appropriate hashes here

def num_trailing_bits(n):
    
    s = str(n)
    rev = s[::-1]	
    count = 0
    for i in rev:
        if i is '0':
            count = count + 1
        else:
            break		
        return count
    """Returns the number of trailing zeros in bin(n)

    n: integer
    """

    pass

num_distinct = 0

#for word in data_stream(): # Implement the Flajolet-Martin algorithm
#    pass

print("Estimate of number of distinct elements = %s"%(num_distinct,))

################### Part 3 ######################

var_reservoir = [0]*512
second_moment = 0
third_moment = 0

# You can use numpy.random's API for maintaining the reservoir of variables

#for word in data_stream(): # Imoplement the AMS algorithm here
#    pass 
      
print("Estimate of second moment = %s"%(second_moment,))
print("Estimate of third moment = %s"%(third_moment,))
