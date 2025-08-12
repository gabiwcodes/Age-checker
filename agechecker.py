print("Welcome to the local club age verifier!")
print("This program will check whether you are eligible to enter a local club.")
print("There are two clubs you can enter based on your age.")
print("Club Bizarre is for ages 18 and above. Club Minority is for ages 14 and above.")
print("If you are under 14, you cannot enter any club.")
print("Please follow the instructions below.")
name=input("Firstly, what is your name?")
print("Hello, "+name+"! Please enter your age.")

age=int(input("What is your age?"))

if age >= 18:print("✅ You are able to enter Club Bizarre. Have fun and stay safe!")
elif age >=14: print("✅ You are able to enter Club Minority. Enjoy!")
else: print("❌ Unfortunately, you are not allowed to enter any club. Please come back once you are older.")