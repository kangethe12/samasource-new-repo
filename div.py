def divid(number,divider):
  """dividing two numbers"""
  try:
    return number/divider
  except ZeroDivisionError:
     print ("Sorry, You can't divide by zero")
  else:
    print (divid(6,3))
