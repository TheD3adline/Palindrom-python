#   Author:     Michael Fessler
#   Data:       2022/09/28
#   Version:    0.1
#               Reads 5 integer inputs into a list then feeds them one by one into
#               an algorithm to determine if the numbers are a palindrom or not
#
import palindrom

zahlen_liste = list()

# Loops through input prompts and checks them for validity (being an integer) until the list has 5 numbers stored
while len(zahlen_liste) < 5:
    num = input("Bitte geben sie eine Zahl ein: ")
    if num.isdigit():
        zahlen_liste.append(int(num))
    elif not num.isdigit():
        print("Falsche Eingabe!")

# The for loop to feed all numbers from the list into the algorithm
for i in range(len(zahlen_liste)):
    palindrom.palindrom(zahlen_liste[i])