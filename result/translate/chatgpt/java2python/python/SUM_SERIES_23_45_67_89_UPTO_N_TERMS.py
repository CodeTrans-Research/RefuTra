def f_gold(n):
  i = 1
  res = 0.0
  sign = True
  while n > 0:
    n -= 1
    if sign:
      sign = not sign
      res = res + float(i+1) / float(i+2)
    else:
      sign = not sign
      res = res - float(i+1) / float(i+2)
    i += 2
  return res