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

most_frequent_char('bookeeper') # -> 'e'
most_frequent_char('david') # -> 'd'
most_frequent_char('abby') # -> 'b'
most_frequent_char('mississippi') # -> 'i'
most_frequent_char('potato') # -> 'o'
most_frequent_char('eleventennine') # -> 'e'
most_frequent_char('riverbed') # -> 'r'

