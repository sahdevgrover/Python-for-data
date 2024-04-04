## CONDITIONAL STATEMENTS

## if and else statements

# marks = input('enter the marks: ')

# if marks >= 35:
  #  print("pass")
# else:
  #  print("fail")

## result << it won't work as i have taken the input value as string, i have to first
## convert it into integer value

## typecasting

marks = int(input('enter the marks: '))

# marks = int(marks)  # converted the str into int

if marks >= 35:
    print("pass")
else:
    print("fail")

## results < will work smoothly
