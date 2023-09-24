# a = ['IV', 'IX', 'I','V','XL', 'XC', 'X','L','CD', 'CM', 'C','D']
# a = ['D', 'CM', 'CD', 'C', 'L', 'XC', 'XL', 'X', 'V',  'IX', 'IV','I']
roman_num = 'MCMXCIV'
arabic_num = 0
di = {'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D': 500, '0': 0}
ex = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

for key, val in ex.items():
    if key in roman_num:
        arabic_num += val
        roman_num = roman_num.replace(key, '')
for key, val in di.items():
    if key in roman_num:

        arabic_num += val * roman_num.count(key)
print(arabic_num)