## TAKING USER INPUT

salary = input("what is your current salary: ")
hike = input("what is the hike percentage: ")

## manually typecasting here

new_salary = int(salary) + (int(salary) * int(hike)/100)

print(f"the new salary after the hike is {new_salary}")

