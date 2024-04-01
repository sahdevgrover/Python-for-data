##TYPECASTING

# in data world, we read the text file from .csv

price = "850"

print(type(price))

## manually typecastinggg

## price = price + (price * 0.1)

## print(price) ## result << can't multiply non-int to type float, as price is string

price = int(int(price) + (int(price) * 0.1)) ## done the typecasting << typecasting it to int

print(price) ## result will be in integer

#### if errors occurs it caught at runtime not compile time unlike java



