#code showing eligibility to vote
age=int (input("Enter your age"))
country=input("Enter your country")
if age >=20 and country.lower() in ["kenya", "uganda", "tanzania"]:
    print("you are eligible")
else:
    print("not eligible")
