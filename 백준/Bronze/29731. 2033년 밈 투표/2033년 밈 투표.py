d = ["Never gonna give you up", "Never gonna let you down", 
     "Never gonna run around and desert you", "Never gonna make you cry", 
     "Never gonna say goodbye", "Never gonna tell a lie and hurt you", 
     "Never gonna stop"]

n = int(input())
s = [input() for _ in range(n)]

if all(phrase in d for phrase in s):
    print("No")
else:
    print("Yes")
