
import time
date = input('Date (mm/dd/yyyy): ')
try:
  valid_date = time.strptime(date, '%m/%d/%Y')
  print("validated")
except ValueError:
  print('Invalid date! ERROR type the write format')