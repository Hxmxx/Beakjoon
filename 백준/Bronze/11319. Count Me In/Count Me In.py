N=int(input())

for i in range(N):
    S= [x for x in input().split()]
    consonants=0
    vowels=0
    for t in S:
        t=t.lower()
        s=list(t)
        for j in s:
            if j=='a' or j== 'e' or j== 'i' or j== 'o' or j=='u':
                vowels +=1
            else:
                consonants+=1 
    print(consonants, vowels)