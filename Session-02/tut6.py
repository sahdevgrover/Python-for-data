### ASSIGNMENTS << taking two inputs as age and crime record whether this person is eligible
## to vote or not

person_age = int(input("enter the age of the person : "))
person_crime_record = input("Does the person have a crime record? (yes/no): ").lower()

if person_age >= 18:
    if person_crime_record == "yes":
        print("the person is not eligible to vote")
    else:
        print("the person is eligible to vote")
else:
    print("the person is not eligible to vote")

## DONE!!