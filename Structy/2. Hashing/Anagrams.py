def anagrams(s1, s2):
  pass # todo
  if len(s1) != len(s2): return False

  s1Counter = {}
  s2Counter = {}

  for i in range(len(s1)):
    s1Counter[s1[i]] = s1Counter.get(s1[i], 0) + 1
    s2Counter[s2[i]] = s2Counter.get(s2[i], 0) + 1
    
  return s1Counter == s2Counter 
