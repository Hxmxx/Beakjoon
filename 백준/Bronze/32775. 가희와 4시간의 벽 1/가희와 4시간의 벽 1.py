import sys
input = sys.stdin.readline

S = int(input())
F = int(input())

if S > F :
    print('flight')
else : 
    print('high speed rail')