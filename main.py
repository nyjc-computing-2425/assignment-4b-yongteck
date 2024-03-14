stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
mantissa,expo = 0,0
validchar = "0123456789E-x.^"
valid = len(stdform) == sum([int(i in validchar) for i in stdform])
valid &= sum([(stdform.count(i)==1) for i in validchar[12:]]) == 3
if valid:
  expo = int(stdform[stdform.find("^")+1:])
  valid &= expo//1 == expo
  mantissa = stdform[:stdform.find("x")]
if valid:
  print("This number in E notation is {}E{}.".format(mantissa,expo))
else:
  print("Error converting to scientific E notation.")
