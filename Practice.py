# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  
  return count

# anagrams('restful', 'fluster') # -> True
# anagrams('cats', 'tocs') # -> False
# anagrams('monkeyswrite', 'newyorktimes') # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('abbc', 'aabc') # -> False
# anagrams('po', 'popp') # -> false
# anagrams('pp', 'oo') # -> false

# Write a function, most_frequent_char, that takes in a string as an argument. 
# The function should return the most frequent character of the string. 
# If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

def most_frequent_char(s):
  counter = {}

  for char in s:
    if char not in counter:
      counter[char] = 0

    counter[char] += 1

  max = 0
  result = ""

  for key in counter:
    if counter[key] > max:
      max = counter[key]
      result = key

  return result

# most_frequent_char('bookeeper') # -> 'e'
# most_frequent_char('david') # -> 'd'
# most_frequent_char('abby') # -> 'b'
# most_frequent_char('mississippi') # -> 'i'
# most_frequent_char('potato') # -> 'o'
# most_frequent_char('eleventennine') # -> 'e'
# most_frequent_char('riverbed') # -> 'r'

# Write a function, pair_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a pair of indices whose elements sum to the given target. 
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

def pair_sum(numbers, target_sum):
  previous = {}

  for index, num in enumerate(numbers):
    complement = target_sum - num
    
    if complement in previous:
      return (previous[complement], index)

    previous[num] = index

pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
pair_sum([1, 6, 7, 2], 13) # -> (1, 2)
pair_sum([9, 9], 18) # -> (0, 1)
pair_sum([6, 4, 2, 8 ], 12) # -> (1, 3)
numbers = [ i for i in range(1, 6001) ]
pair_sum(numbers, 11999) # -> (5998, 5999)

# Write a function, pair_product, that takes in a list and a target product as arguments. 
# The function should return a tuple containing a pair of indices whose elements multiply to the given target. 
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.

def pair_product(numbers, target_product):
  previous_product = {}

  for index, num in enumerate(numbers):
    complement = target_product // num

    if complement in previous_product:
      return (previous_product[complement], index)

    previous_product[num] = index

