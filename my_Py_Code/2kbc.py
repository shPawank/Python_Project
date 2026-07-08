#kaun banega crorepati with Pawan Sharma

questions = [
    ["What is color of sky?","Blue","Green","Red","Purple",1],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["How many players are there in a cricket team?", "9", "10", "11", "12", 3],
    ["Who directed the movie 'Dilwale Dulhania Le Jayenge'?", "Karan Johar", "Aditya Chopra", "Sanjay Leela Bhansali",
     "Raj Kumar Hirani", 2],
    ["What does 'www' stand for in a website URL?", "World Wide Web", "World Web Window", "Wide World Web",
     "Web World Wide", 1],
    ["Capital of India","Kolkata","Mumbai","Delhi","Chennai",3],
    ["Capital of India","Kolkata","Mumbai","Chennai","Delhi",4]
]
levels=[1000,2000,3000,5000,10000,20000,40000]

for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question {i+1}: {question[0]}")
    print(f"1:{question[1]}")
    print(f"2:{question[2]}")
    print(f"3:{question[3]}")
    print(f"4:{question[4]}")

    reply=int(input("Enter your choice:"))

    if reply==0:
        print("I want to quit \nYou have won ",levels[i-1])
        break

    if reply==question[-1]:
        print(f"Correct Answer, YOu have won {levels[i]}")
    else:
        print(f"Wrong Answer, {levels[i]}")
        if i == 3:  # ✅ safe zone 1
            money = 5000
            print("You'll take min amount: ₹", money)
        elif i == 4:  # ✅ safe zone 2
            money = 10000
            print("You'll take min amount: ₹", money)
        else:
            print("You'll take nothing!")  # ✅ no NameError
        break

