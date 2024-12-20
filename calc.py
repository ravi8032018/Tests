def calc():
	check='y'
	while(check=='Y' or check=="y"):
		try:
			a=float(input('Enter 1st no. : '))
			b=float(input('Enter 2nd no. : '))
			c=input('Enter the operator (+,-,*,/,%) : ')
			res=0
			msg='Result is : '

			if c=='+':
				res=a+b
			elif c=='-':
				res=a-b
			elif c=='*':
				res=a*b
			elif c=='/':
				res=a/b
			elif c=='%':
				res=a%b
			else:
				print('\n \t  Please Enter a valid operator!!\n')
			print(f'\t{msg}{res}')

		except ZeroDivisionError:
		 	print('Cannot divide by Zero!!')
		except ValueError:
			print('No text please!!')
		
		check=input('Wanna try this again Y/N : ')	
	print('\n \tExiting the Calculator\n')

calc()
print("fork successful")