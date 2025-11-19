def pairs(elements):
  pass # todo
  res = []
  for i in range(len(elements)):
    outer = elements[i]
    for j in range(i + 1, len(elements)):
      res.append([outer, elements[j]])
  return res