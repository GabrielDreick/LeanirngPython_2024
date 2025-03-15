# ordem de precedencia
#       1 ()
#       2 **
#       3 *, /, //, %
#       4 +, -

plus = 5 + 2
minus = 5-2
multi = 5*2
divide2 = 5/2
divide3 = 5/3
divide4 = 5/4
divide5 = 5/5
power2 = 5**2
power3 = 5**3
power4 = 5**4
power5 = 5**5
real2 = 5//2
real3 = 5//3
real4 = 5//4
real5 = 5//5
modulo2 = 5 % 2
modulo3 = 5 % 3
modulo4 = 5 % 4
modulo5 = 5 % 5

print('        plus', plus)
print('       minus', minus)
print('       multi', multi)
print(f'      divide 2/{divide2} 3/{divide3} 4/{divide4} 5/{divide5}')
print(f'       power 2**{power2} 3**{power3} 4**{power4} 5**{power5}')
print(f'real divide 2//{real2} 3//{real3} 4//{real4} 5//{real5}')
print(f'      modulo 2%{modulo2} 3%{modulo3} 4%{modulo4} 5%{modulo5}')
