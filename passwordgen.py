# Password Generator 20.22beta

# Construction de la base de characteres
from random import shuffle
combinaisons = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","L","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                "a","z","e","r","t","y","u","i","o","p","q","s","d","f",
                "g","h","j","k","l","m","w","x","c","v","b","n","0",
                "1","2","3","4","5","6","7","8","9","!","^","$","à",")","ù"]
print("Do You want new secure password ? Yes or No")
answer = input()
if answer == "Yes":
    shuffle(combinaisons)
    print(combinaisons[1]+combinaisons[2]+combinaisons[3]+combinaisons[5]+combinaisons[7]+
          combinaisons[8]+combinaisons[9]+combinaisons[7]+combinaisons[4]+combinaisons[6])
elif answer == "yes":
    shuffle(combinaisons)
    print(combinaisons[1]+combinaisons[2]+combinaisons[3]+combinaisons[5]+combinaisons[7]+
          combinaisons[8]+combinaisons[9]+combinaisons[7]+combinaisons[4]+combinaisons[6])
elif answer == "y":
    shuffle(combinaisons)
    print(combinaisons[1] + combinaisons[2] + combinaisons[3] + combinaisons[5] + combinaisons[7] +
          combinaisons[8] + combinaisons[9] + combinaisons[7] + combinaisons[4] + combinaisons[6])
else:
    print("No Worries, Bye.")
    exit()