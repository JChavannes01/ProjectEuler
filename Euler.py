import time
import sys
""" Project euler exercises solved with python scripts.
	Exercise source: http://projecteuler.net"""


## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1:.1f}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

    
def problem1():
	"""	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
		The sum of these multiples is 23.
		Find the sum of all the multiples of 3 or 5 below 1000."""
	print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))


def problem2():
	"""	Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
			1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
		By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""
	x1, x2, sum, limit = 1, 2, 0, 4_000_000
		
	while x2 <= limit:
		if x2 % 2 == 0:
			sum += x2
			
		x1, x2 = x2, x1+x2
		
	print(sum)
			
		
def problem3():
	"""	The prime factors of 13195 are 5, 7, 13 and 29.
		What is the largest prime factor of the number 600851475143 ?"""
	largestPrime, factor, number = 2, 2, 600_851_475_143
	
	while factor <= number:
		if number % factor == 0:
			#number can be divided by this prime, new largestPrime
			largestPrime, number = factor, number // factor
		else:
			factor += 1
			
	print(largestPrime)


def problem4():
	"""	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
		Find the largest palindrome made from the product of two 3-digit numbers."""
	limit, maxPalindrome, = 999, 0
	
	for factor1 in range(limit, 0, -1):
		if factor1**2 <= maxPalindrome:
			break # we can stop early since we can't get a higher number
		
		for factor2 in range(factor1, 0, -1):
			product = factor1*factor2
			if str(product) == str(product)[::-1]:
				maxPalindrome = max(maxPalindrome, product)
				break #found a palindrome, since factors descend this must be the largest
				
	print(maxPalindrome)	
	
			
def problem5():
    """ 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
    
    # Get the prime factorisation of all the numbers,
    # take the LCM combination of all numbers. 
    # LCM = product of all prime factorisations with the max exponent.
    
    limit = 20
    totalPrimeFactorisationDict = dict()
    
    for i in range(1, limit+1):
        prime, exponent = 2, 0
        
        while True:
            if i % prime == 0:
                i = i // prime
                exponent += 1
            else:
                if exponent > totalPrimeFactorisationDict.get(prime, 0):
                    totalPrimeFactorisationDict[prime] = exponent
                exponent = 0
                prime += 1
                if prime > i:
                    break
            
    product = 1
    
    for (prime, exp) in totalPrimeFactorisationDict.items():
        print("prime: {}, exp: {}".format(prime, exp))
        product *= prime**exp
        
        
    print("problem5:", product)
    
    
def problem6():
    """ The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385
        The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)^2 = 55^2 = 3025
        Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

        Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
    print( sum(range(1,101))**2 - sum([x**2 for x in range(1,101)]) )

    
def problem7():
    """ By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
        What is the 10 001st prime number?"""
    # find nth prime:
    primes = [2]
    i = 3

    while len(primes) < 10001:
        i += 2
        is_prime = True        
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    
    print( primes[-1] )
    
    
def problem8():
    """ The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

            73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450

        Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?"""
    sequence =  '73167176531330624919225119674426574742355349194934'
    sequence += '96983520312774506326239578318016984801869478851843'
    sequence += '85861560789112949495459501737958331952853208805511'
    sequence += '12540698747158523863050715693290963295227443043557'
    sequence += '66896648950445244523161731856403098711121722383113'
    sequence += '62229893423380308135336276614282806444486645238749'
    sequence += '30358907296290491560440772390713810515859307960866'
    sequence += '70172427121883998797908792274921901699720888093776'
    sequence += '65727333001053367881220235421809751254540594752243'
    sequence += '52584907711670556013604839586446706324415722155397'
    sequence += '53697817977846174064955149290862569321978468622482'
    sequence += '83972241375657056057490261407972968652414535100474'
    sequence += '82166370484403199890008895243450658541227588666881'
    sequence += '16427171479924442928230863465674813919123162824586'
    sequence += '17866458359124566529476545682848912883142607690042'
    sequence += '24219022671055626321111109370544217506941658960408'
    sequence += '07198403850962455444362981230987879927244284909188'
    sequence += '84580156166097919133875499200524063689912560717606'
    sequence += '05886116467109405077541002256983155200055935729725'
    sequence += '71636269561882670428252483600823257530420752963450'

    largestProduct = 0
    for index in range(1, len(sequence)-12):
        product = 1
        for offset in range(13):
            product *= int(sequence[index+offset])
        largestProduct = max(product, largestProduct)
    print(largestProduct)
    
    
def problem9():
    """ A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
            a^2 + b^2 = c^2
        For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc."""
    for c in range(400, 1000):
        for b in range((500-c//2), min(c, 1000-c)):
            a = 1000 - b - c
            if a**2 + b**2 == c**2:
                print("found the triplet: ({},{},{}), product: {}".format(a,b,c, a*b*c))
                break
                
    
def problem10():
    """ The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
        Find the sum of all the primes below two million."""
    primes = [2]
    
    for i in range(3, 200000, 2):
        is_prime = True        
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    
    print("done finding primes.")
    print( "problem 10: sum = {}".format(sum(primes)) )
    
        
        
def problem11():
    """ In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

            08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

        The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
        What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?"""
    grid = list()
    grid.append([ 8,  2, 22, 97, 38, 15, 00, 40, 00, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8]) 
    grid.append([49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62, 00]) 
    grid.append([81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65]) 
    grid.append([52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91])
    grid.append([22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
    grid.append([24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
    grid.append([32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
    grid.append([67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21])
    grid.append([24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
    grid.append([21, 36, 23,  9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95])
    grid.append([78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92])
    grid.append([16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57])
    grid.append([86, 56, 00, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
    grid.append([19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40])
    grid.append([ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
    grid.append([88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
    grid.append([ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36])
    grid.append([20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16])
    grid.append([20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54])
    grid.append([ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48])        
    # grid[row][col]
    
    largestProduct = 0
    originRow, originCol, position = 0, 0, ""
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # check vertical
            if row+3 < len(grid):
                if product([ grid[row+offset][col] for offset in range(4)]) > largestProduct:
                    originRow, originCol, position = row, col, "Vertical"
                largestProduct = max(largestProduct, product([ grid[row+offset][col] for offset in range(4)])) 
                
            # check horizontal
            if col+3 < len(grid[row]):
#                if product([ grid[row][col+offset] for offset in range(4)]) > largestProduct:
#                        originRow, originCol, position = row, col, "Horizontal"
                largestProduct = max(largestProduct, product([ grid[row][col+offset] for offset in range(4)]))            
            
            # check diagonal bottom right
            if row+3 < len(grid) and col+3 < len(grid[row]):
#                if product([ grid[row+offset][col+offset] for offset in range(4)]) > largestProduct:
#                        originRow, originCol, position = row, col, "Diagonal \\"
                largestProduct = max(largestProduct, product([ grid[row+offset][col+offset] for offset in range(4)]))
            
            # check diagonal bottom left
            if row+3 < len(grid) and col > 3:
#                if product([ grid[row+offset][col-offset] for offset in range(4)]) > largestProduct:
#                        originRow, originCol, position = row, col, "Diagonal /"
                largestProduct = max(largestProduct, product([ grid[row+offset][col-offset] for offset in range(4)]))
                
    print("problem11: largestProduct = {}, at {},{} {}".format(largestProduct, originRow, originCol, position))
    
    
def product(list):
    """Helper for problem 11, returns the product of a list of numbers"""
    product = 1 if len(list) > 0 else 0
    for x in list:
        product *= x
    return product
    
    
def problem12():
    """ The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
       Let us list the factors of the first seven triangle numbers:
             1: 1
             3: 1,3
             6: 1,2,3,6
            10: 1,2,5,10
            15: 1,3,5,15
            21: 1,3,7,21
            28: 1,2,4,7,14,28
        We can see that 28 is the first triangle number to have over five divisors.
        What is the value of the first triangle number to have over five hundred divisors?"""
    triN, i = 0, 1
    while True:
        numOfDivs = 1
        triN += i
        i += 1
        for exp in factorise(triN).values():
            numOfDivs *= exp+1
        if numOfDivs > 500:
            print(triN, numOfDivs)
            break
        

def factorise(n):
    p, factorisation = 2, dict()
    while p <= n:
        if n % p == 0:
            n = n // p
            factorisation[p] = factorisation.get(p,0) + 1
        else:
            p += 1
    return factorisation
        
        
def problem13():
    """Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""
    lines = open('problem13.txt').readlines()
    print('sum:', str(sum([int(line.strip()) for line in lines]))[:10] )
    
        
def problem14():
    """ The following iterative sequence is defined for the set of positive integers:
            n → n/2 (n is even)
            n → 3n + 1 (n is odd)
       Using the rule above and starting with 13, we generate the following sequence:
            13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?
        NOTE: Once the chain starts the terms are allowed to go above one million. A: longest chain length: 525, for start: 837799 """
    n, chain = 13, [13]
    longestChainLength, longestChainStart = 1, 1
    for n in range(1_000_000):
        chain = [n]
        start = n
        while True:
            n = collatzFunc(n)
            chain.append(n)
            if n <= 1:
                break
        if len(chain) > longestChainLength:
            longestChainLength = len(chain)
            longestChainStart = start

        
    print('longest chain length: {}, for start: {}'.format(longestChainLength, longestChainStart))
        
        
def collatzFunc(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

def problem15():
    """ Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
        How many such routes are there through a 20×20 grid?"""
    # permutations :) 40 choose 20
    
    # factorise numerator and denominator
    factorisationDenominator, factorisationNumerator = dict(), dict()
    for n in range(1, 40+1):
        for (prime, exp) in factorise(n).items():
            factorisationNumerator[prime] = factorisationNumerator.get(prime, 0) + exp
    
    for n in range(1, 20+1):
        for (prime, exp) in factorise(n).items():
            factorisationDenominator[prime] = factorisationDenominator.get(prime, 0) + 2*exp
    
    # simplify both factorisations
    for (prime, exp) in factorisationDenominator.items():
        amountToRemove = min(exp, factorisationNumerator.get(prime, 0))
        factorisationDenominator[prime] -= amountToRemove
        factorisationNumerator[prime] -= amountToRemove
    
    productNumerator = product( [p**e for (p,e) in factorisationNumerator.items()] )
    productDenominator = product( [p**e for (p,e) in factorisationDenominator.items()] )
    
    print('number of routes: {:.0f}'.format(productNumerator / productDenominator))
    
    
def problem16():
    """ 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
        What is the sum of the digits of the number 2^1000?"""
    print( sum([int(digit) for digit in str(2**1000)]) )

    
def problem17():
    """ If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
        If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
        NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""
    
    # times thousands are named.
    # once, 1000
    lenThousands = len('onethousand')
    
    # times hundreds are named.
    # 9 times for each thousandfold
    # linking word for hundreds, "and" e.g. one hundred and one 
    lenLinkingWords = 9 * (100 - 1) * len('and')
    lenHundreds = 100 * sum([len(word + 'hundred') for word in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']])
    
    # times tens are named.
    # 10 times for every hundredfold, no linking words
    lenTens = 10 * (10*sum([len(word) for word in ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']]) + 1*len('ten'))
    
    # times single digits are named.
    # 9 times for each tenfold, difference in 10-19, no linking words
    lenSingles = 10 * (9*sum([len(word) for word in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]) + 1*sum([len(word) for word in ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']]))
    
    totalSize = lenLinkingWords + lenThousands + lenHundreds + lenTens + lenSingles
    print('total size: {}'.format(totalSize))
        

def problem18():
    """ By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)"""
    
    triangle = [ list(map(int, l.strip().split('  '))) for l in open('problem18.txt').readlines()]
    
    # deep copy of the triangle.
    sumTriangle = [[num for num in row] for row in triangle]
    
    # Traverse in reverse order, exluding the last row since it does not have any children
    for i in range(len(sumTriangle)-2, -1, -1):
        for n in range(len(sumTriangle[i])):
            lchild, rchild = sumTriangle[i+1][n], sumTriangle[i+1][n+1]
            sumTriangle[i][n] += max(lchild, rchild)
   
    print('max total =', sumTriangle[0][0])
   
   
def problem19():
    """You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
     
    monthToDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayindex, counter = 0, 0
    for year in range(1900,2001):
        isLeapYear = year % 400 == 0 or (year % 100 > 0 and year % 4 == 0)
        for i in range(12):
            if dayindex == 6 and year > 1900:
                counter += 1
            days = 29 if isLeapYear and i==1 else monthToDays[i]
            dayindex = (dayindex+days)%7
            
    print('amount of sundays on the first of the month:', counter)
    
    
def problem20():
    """n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!"""
    print(sum([int(x) for x in str(product(range(1,100+1)))]))
    
    
def problem21():
    """Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000."""
    d = {n: sum(getDivisors(n, False)) for n in range(2,10_000)}
    print("amicable pairs:")
    pairs = [(k,v) for (k,v) in d.items() if v>k and v in d and d[v]==k]
    print( sum( [k+v for (k,v) in pairs] ) )
    
    
def getDivisors(number, includeSelf=False):
    '''
    Returns a list of all the numbers that the input can be divided by without having a remainder.
    '''
    divisors = _getDivisors(factorise(number))
    # number itself is not a proper divisor
#    if not number in divisors:
#        print('number {} not in divisor list: {}'.format(number, divisors))
    if not includeSelf:
        divisors.remove(number)
#    divisors.sort()
    return divisors

    
def _getDivisors(primes):
    '''
    Helper function for the recursive calls of getDivisors. This accepts a list of primes and recursively finds all divisors.
    '''
    list = []
    if len(primes) == 0:
        list = [1]
    else:
        (k,v) = primes.popitem()
        others = _getDivisors(primes)
        list = [k**x * y for x in range(0, v+1) for y in others]
    
    return list
    
    
def problem22():
    """Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?"""
    names = sorted([name.strip('"') for line in open('p022_names.txt').readlines() for name in line.split(',')])
    print(sum( [(i+1)*alphabeticalValue(names[i]) for i in range(len(names))] ))

    
def alphabeticalValue(name):
    offset = ord('a')-1
    return sum( [ord(letter)-offset for letter in name.lower()] )
    
    
def problem23():
    """A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
    
    start = time.time()
    abs, undivisibles = list(), list()
    for x in range(2, 28123+1):
        if x%100==0:
            update_progress(x/28123)
        if sum(getDivisors(x))>x: #this is an abundant number
            isDivisible = False
            for a in abs:
                if x-a in abs:
                    isDivisible = True
                    break
            if not isDivisible:
                undivisibles.append(x)
            abs.append(x)
    update_progress(1)
    
    print('Time elapsed = {:2.1f} seconds'.format(time.time()-start))
    print(sum(undivisibles))
    
    
def problem24():
    """ A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    
    #calc first number: 
    limit = 1_000_000
    permutation, numbers = list(), list(range(10))
    for i in range(9,-1,-1):
        prod = product(range(1,i+1))
        if limit==0 or prod==0:
            fits = 0
        else:
            fits = (limit//prod)-1 if (limit % prod)==0 else limit//prod
        print('Found new char {} ({}), limit = {}'.format(fits, numbers[fits], limit))
        permutation.append(numbers.pop(fits))
        limit = limit - fits*prod
    
    print('permutation =', ''.join(map(str, permutation)))
    
    
def problem25():
    """ The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""
    
    
def problem26():
    """ A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

        1/2	= 	0.5
        1/3	= 	0.(3)
        1/4	= 	0.25
        1/5	= 	0.2
        1/6	= 	0.1(6)
        1/7	= 	0.(142857)
        1/8	= 	0.125
        1/9	= 	0.(1)
        1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
    
    
def problem27():
    """ Euler discovered the remarkable quadratic formula:

    n^2+n+41
    It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

    The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

    n^2+an+b, where |a|<1000 and |b|≤1000

    where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4
    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0."""
    
    
if __name__ == '__main__':
    problem24()