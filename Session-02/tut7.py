### LOGICAL OPERATORS << AND , OR

age = int(input("please enter the age: "))
crime_record = input("are there any criminal record yes/no: ")

if not age < 18 and crime_record == "no":
    print("yes vote")
else:
    print("no vote")

## AND << BOTH CONDITIONS SHOULD BE SATISFY
## OR << ONE OF THE CONDITIONS SHOULD BE SATISFY
## NOT << SHOULD'NT BE LARGER OR SMALLER