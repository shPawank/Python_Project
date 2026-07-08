#Kaun Banega Crorepati: Exercise 3 - Solution

questions = [
    # [Question, A, B, C, D, correct option (1-4)]

    # Easy (1000 - 5000)
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["How many players are there in a cricket team?", "9", "10", "11", "12", 3],
    ["Who directed the movie 'Dilwale Dulhania Le Jayenge'?", "Karan Johar", "Aditya Chopra", "Sanjay Leela Bhansali",
     "Raj Kumar Hirani", 2],
    ["What does 'www' stand for in a website URL?", "World Wide Web", "World Web Window", "Wide World Web",
     "Web World Wide", 1],

    # Medium (10000 - 40000)
    ["Who won the FIFA World Cup 2022?", "Brazil", "France", "Argentina", "Germany", 3],
    ["Which Indian scientist is known as the Missile Man of India?", "C.V. Raman", "Homi Bhabha", "APJ Abdul Kalam",
     "Vikram Sarabhai", 3],
    ["In which movie did Shah Rukh Khan play a hockey coach?", "Chak De India", "Dil To Pagal Hai", "Swades",
     "Kabhi Khushi Kabhie Gham", 1],

    # Hard (80000 - 320000)
    ["What is the full form of DNA?", "Deoxyribose Nucleic Acid", "Deoxyribonucleic Acid", "Deoxyribo Nucleus Acid",
     "Double Nucleus Acid", 2],
    ["Who holds the record for most Test centuries in cricket?", "Ricky Ponting", "Jacques Kallis", "Sachin Tendulkar",
     "Virat Kohli", 3],
    ["Which Bollywood film won India's first Oscar nomination in 1957?", "Mother India", "Mughal-E-Azam",
     "Do Bigha Zamin", "Boot Polish", 1],
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

print("🎬 Welcome to Kaun Banega Crorepati! 🎬")

for i in range(0,len(questions)):
    questions=questions[i]
    print(f"question of Rs.{levels[i]}")
    print(f"a. {questions[1]} ,b. {questions[2]}")
    print(f"c. {questions[3]} ,d. {questions[4]}")
    reply=int(input("ENter the choice: "))
    if (reply==questions[-1]):
        print(f" correct answer, You have won Rs.{levels[i]}")
        if i==4:
            money=10000
        elif i==9:
            money=320000
    else:
        print(f" incorrect answer, You have lost")
        break