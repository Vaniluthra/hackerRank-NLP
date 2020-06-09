import sys
n = int(input())
data = sys.stdin.read().lower().split('\n\n')
mon = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august','september', 'october', 'november', 'december', 'jan', 'feb', 'mar', 'apr','may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
for _ in range(n):
    s = str(data[_]).replace('"','').split()
    print(s)
    print(s.count('a'))
    print(s.count('an'))
    print(s.count('the'))
    print(s.count(mon))