### NESTING IF AND ELSE

marks = int(input("enter the marks: "))

if marks >= 30:
    if marks > 80:
        print("A grade")
    else:
        print("you passed but you did'nt secure A grade")

else:
    print("fail")