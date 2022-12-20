
word = input('input sentence ')
print(len([i for i in word.split(' ') if i != '']))


b = True
while b:
   bnum = input('input binary number ')
   try:
       print(int('0b' + bnum, 2))
   except ValueError:
       print('try using only 0 and 1')
       continue
   b = False
