import math

equation = True
while equation:
   x = float(input('input x '))
   if x <= 0:
       print('try other constant')
       continue
   y = float(input('input y '))
   equation = False
print('result is', math.log(x) + (3.5*x + 1 )/(math.cos(2*y)))


calculation = True
while calculation:
   salary = int(input('input your salary '))
   if salary < 0:
       print('you entered incorrect answer')
       continue
   years = int(input('input years of your experience '))
   if years < 0:
       print('you entered incorrect answer')
       continue
   months = int(input('input months of your experience '))
   if months < 0:
       print('you entered incorrect answer')
       continue
   days = int(input('input days of your experience '))
   if days < 0:
       print('you entered incorrect answer')
       continue
   calculation = False
experience = years + (months/12) + (days/365)
if experience < 2:
   print('you have no salary allowance')
elif 2 <= experience <= 5:
   salary_allowance = salary * (2/100)
   salary_with_allowance = salary + salary_allowance
   print('your salary allowance is ' + str(salary_allowance) + ' and your salary with allowance is ' + str(salary_with_allowance))
else:
   salary_allowance = salary * (5/100)
   salary_with_allowance = salary + salary_allowance
   print('your salary allowance is ' + str(salary_allowance) + ' and your salary with allowance is ' + str(salary_with_allowance))


calculation = True
while calculation:
   n = int(input('input natural number '))
   if n <= 0:
       print('incorrect answer')
       continue
   factorial = 1
   for i in range(1,n+1):
       factorial = factorial * i
   calculation = False
print('factorial is', factorial)
