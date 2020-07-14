from random import choice
b='BOLLYWOOD'
L=9
picture=[]
vowel=['a','e','i','o','u']
print('Before playing BOLLYWOOD lets add some movies')
n=int(input("How many movies you would like to register?:"))
file=open('movie.txt','a')
print('Enter movies')
for i in range(n):
    take=input(i+1)
    file.write(take)
    file.write('  ')
print('your movies are registered succussfully to play')
file.close()
#you can saparate the above code so that u wont have to make file again n again
print('lets play\n')
file=open('movie.txt','r')
content=file.read()
new=content.split('  ')
movie=choice(new)
length=len(movie)
file.close()
for i in range(length):
    if movie[i] in vowel or movie[i]==' ':
        picture.append(movie[i])
    else:
        picture.append('_')
while L!=0:
    print(b[:L])
    print(picture)
    guess=input("Guess:")
    for i in range(length):
        if guess==movie[i]:
            picture[i]=guess
    if guess not in movie:
        L-=1
    c=0    
    for i in range(length):
        if picture[i]!=movie[i]:
            c+=1
            break
    if c==0:
        print("you won")
        break
    else:
        continue
if c!=0:
    print('you lose')
    print('Movie was ',movie)
input()
            
        
    




        
    

    
