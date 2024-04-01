learner_name = "sahdev"
studying = "python_for_data"
timing = 6
total_time = 1.5
is_studying = True
total_income = None

print(type(learner_name))  # str
print(type(studying))  # str
print(type(timing))  # int
print(type(total_time))  # float
print(type(is_studying))  # bool
print(type(total_income))  # Nonetype

# print(learner_name + 1)   # caught at runtime unlike java caught at compile time

print(timing + 4) # result is 10

print(timing) # result is 6 only, cause it's not holding back

## asigning the data to it

timing = timing + 4

print(timing) # result is now 10 again

timing = timing + ( timing * 0.1)

print(timing)