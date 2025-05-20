#are you lebron small project using and/or/not conditionals by lanc 2025

team = input("What teams have you played for?: ").lower()
print("Hmmm...")

rings = int(input("How many rings do you have?: "))
print("Interesting...")

big3 = input("Are you, Luka Don, and A Reaves the real big 3?: ").lower()
print("Could it be...")

are_jordan = input("Are you Michael Jordan?: ").lower()
print("I'm getting a picture now.")

goat = input("Are you the REAL GOAT?: ").lower()

if (
    "cavs" in team and
    "heat" in team and
    "lakers" in team and
    (rings == 4 or rings >= 5) and
    (big3 == "yes" or big3 == "maychance") and
    are_jordan == "no" and
    "bulls" not in team and
    goat == "yes"
):
    print("Welcome back King Bron.")
else:
    print("You are no king of mine.")