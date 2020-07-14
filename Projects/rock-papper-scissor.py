import random
choices=["rock","paper","scissor"]
counterc,counteru=0,0
print("""
    rock    + paper   = paper
    rock    + scissor = rock
    paper   + scissor = scissor
    rock    + rock    = TIE
    paper   + paper   = TIE
    scissor + scissor = TIE \n\nlets START""")
for i in range(3):
    user_ch=input("your turn:").lower()
    comp_ch=random.choice(choices)
    if user_ch not in choices:
        print('invalid choice:you lose this turn')
        counterc+=1
        continue
    print('computer entered:',comp_ch)
    if user_ch!=comp_ch:
        if user_ch=="rock":
            if comp_ch=='paper':
                counterc+=1
            else:
                counteru+=1
        elif user_ch=='paper':
            if comp_ch=='scissor':
                counterc+=1
            else:
                counteru+=1
if counterc==counteru:
    print('TIE')
elif counterc>counteru:
    print('you lose')
else:
    print("you WON")
        
