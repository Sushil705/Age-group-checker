
from word2number import w2n
from datetime import datetime
def say_amazing(year):
   amazing={
1980:"Ic2onic music and films defined the era—Michael Jackson’s Thriller (1982), Back to the Future (1985), and the rise of MTV. The fall of the Berlin Wall (1989) symbolized the end of the Cold War.",
1990:"The World Wide Web went public (1991), and Netscape (1994) made the internet accessible. The first text message was sent in 1992. Amazon (1994) and Google (1998) were founded, reshaping commerce and information.",
2000:"The iPod (2001) and iPhone (2007) revolutionized music and mobile communication. Facebook (2004) and YouTube (2005) transformed social media and content sharing. Wikipedia (2001) democratized knowledge",
2010:"Tesla’s Model S (2012) accelerated electric vehicle adoption. AI advancements, like AlphaGo defeating a Go champion (2016), marked tech breakthroughs.",
2020:"SpaceX’s reusable rockets and Starlink (2020s) expanded space access and global internet. AI models like ChatGPT (2022) and Grok 3 (2024) transformed human-machine interaction."}
   if year<1981:
     print(amazing[1980])
     print(amazing[1990]) 
     print(amazing[2000]) 
     print(amazing[2010])

     print(amazing[2020])
   elif year<1991:        
     print(amazing[1990])
     print(amazing[2000])
     print(amazing[2010])
     print(amazing[2020])
     
   elif year<2001:  
     print(amazing[2000])
     print(amazing[2010])
     print(amazing[2020])
   elif year<2011:
     print(amazing[2010])
     print(amazing[2020])
   elif year>2024:
      print(" ")
   else:
     print(amazing[2020])
def get_year_from_input(user_input):
    try:
        # Try converting directly to integer 
        return int(user_input)
    except ValueError:
        try:
            # Convert words to number given by user
            return w2n.word_to_num(user_input.lower())
        except ValueError:
            print("Invalid input format.")
            return None

def get_age_group(age):
    if age<0:
        return "Invalid age. Please enter a valid year of birth."
    if age == 0:
        return "You are infant"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 35:
        return "Young Adult"
    elif age <= 59:
        return "Adult"
    elif age<=100:
        return "Senior Citizen"
    else:
        raise ValueError

def main():
    user_input = input("Enter your birth year (e.g., 2005 or 'Two Thousand Five'): ")
    birth_year = get_year_from_input(user_input)
    if birth_year<1925:
        raise ValueError
    else:
     say_amazing(birth_year)
     if birth_year is not None:
        current_year = datetime.now().year
        age = current_year - birth_year

        if age < 0:
            print("You entered a year in the future. Please try again.")
        else:
            group = get_age_group(age)
            print(f"Your age is: {age}")
            print(f"You belong to the '{group}' age group.")

try:
    main()
except:
    print("You entered wrong value")
