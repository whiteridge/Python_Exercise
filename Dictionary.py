# Wap to Create a dictionary and take input from the user and return the meaning of the word from the dictionary
# Judo – Japanese Numbers
Dict = {"1": "Ichi","2": "Ni","3": "San","4": "Shi","5": "Go",
"6": "Roku", "7": "Nana", "8": "Hachi","9":"Kyu","10": "Juu",
"11": "Juu Ichi","12": "Juu Ni","13": "Juu San","14": "Juu Shi","15": "Juu Go",
"16": "Juu Roku","17" : "Juu Nana","18": "Juu Hachi","19" : "Juu Kyu","20" :"Ni Juu"}
print("Judo numbers in words")
print("Enter the numbers between 1-20")
Data1 = input()

if int(Data1)<21:
    print(Data1, "in japanese called as", Dict[Data1])
else:
    print("You have enter the invalid number")


