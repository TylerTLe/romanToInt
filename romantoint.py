s = input('please input a Roman numeral\n')

roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total=0

# for loop till len(s)-1 cause for last Roman Value we cant compare
for i in range(len(s)-1):
    if roman[s[i]] < roman[s[i+1]]:
        total -= roman[s[i]]
    else:   
        total += roman[s[i]]

print(total+roman[s[-1]])
