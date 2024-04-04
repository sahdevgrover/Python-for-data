## ARITHMETIC OPERATIONS << ( + , * , - , % , // )

## * AND // << ARE AT EQUAL PRIORITY
## + AND - << ARE AT EQUAL PRIORITY

## FIRST * AND // WILL HAPPEN THEN + AND - WILL HAPPEN

## PRECEDENCE IS FROM LEFT TO RIGHT

bigdata_fees = 800
azure_fee = 600
big_data_enrollments = 20
azure_enrollments = 40

## ONE METHOD << WITH BACKSLASH
#total_revenue = bigdata_fees * big_data_enrollments \
   #              + azure_fee * azure_enrollments

## SECOND METHOD << WITH BRACKETS ENCLOSED

total_revenue = (bigdata_fees * big_data_enrollments
                 + azure_fee * azure_enrollments)

avg_order_price = (bigdata_fees * big_data_enrollments
                 + azure_fee * azure_enrollments) / (big_data_enrollments + azure_enrollments)

print(f"total_revenue is {total_revenue}")

print(f"avg order price is {avg_order_price}")

