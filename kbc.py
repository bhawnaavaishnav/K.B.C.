print("Hello")
print()
player = input("Welcome to KBC!\nEnter your name sir/mam: ")
print()
print("Welcome", player, "! Here are the rules of the game:-\n1. There will be total of 13 questions.\n2. Each question has 4 options and only one of them is correct.\n3. Total cash prize is ₹ 5 crores.\n4. You have 2 lifeline and you can only use both of them only once.\n5. You have two milestone questions in this game if you have crosse the milestone question, you are guranteed to win that amount\n6. Press '0' for quit the game")
print()
print("Start the game, this is your first question")

KBC = [
    {
        "question": "1. Which one letter usually several products made by Apple Inc?",
        "options": ["A. p", "B. i", "C. j", "D. g"],
        "answer":"B",
        "50-50 lifeline":["B", "D"],
        "amount":"₹5,000",
        "hint":"Type of phone",
        "milestone":"",
        "quit":"0"
    },
    {
        "question": "Q 2. The ‘boondi’ of ‘boondi ke ladoo’ is primarily made of what?",
        "options": ["A. Besan", "B. Suji", "C. Potato", "D. Khoya"],
        "answer":"A",
        "50-50 lifeline":["A", "D"],
        "amount":"₹10,000",
        "hint":"Khandvi is also made from this",
        "milestone":"",
        "quit":"5,000"
    },
    {
        "question": "Q 3. Who is the lyricist of the evergreen song “Lag Ja Gale”?", 
        "options": ["A. Sahir Ludhianvi", "B. Javed Akhtar", "C. Gulzar", "D. Raja Mehdi Ali Khan"], 
        "answer":"D", "50-50 lifeline":["B", "D"], 
        "amount":"₹20,000", 
        "hint":"`Aapki nazro ne samjha pyar ke kabil hame` also written by that writer", 
        "milestone":"10,000", 
        "quit":"10,000"
    },
    {
        "question": "Q.4 When is International Yoga Day celebrated?", 
        "options": ["A. June 21", "B. March 21", 
        "C. April 22", "D. May 31"], 
        "answer":"A", 
        "50-50 lifeline":["A", "D"], 
        "amount":"₹40,000", 
        "hint":"This day is the longest day of the whole year", 
        "milestone":"10,000", 
        "quit":"20,000"
    },
    {
        "question": "Q5. What is the meaning of kalibangan in Rajasthan which shows the prehistoric and pre-Mauryan character of Indus Valley Civilization ?", 
        "options": ["A. Black River", "B. Black Bangles", "C. Black forest", "D. Black land"], 
        "answer":"B", 
        "50-50 lifeline":["A", "B"], 
        "amount":"₹80,000", 
        "hint":"Its name is related to the name of the jewelry.", 
        "milestone":"10,000", 
        "quit":"40,000"
    },
    {
        "question": "Q6. Which bird is the universal symbol of peace?", 
        "options": ["A. Bluebird", "B. Peacock", "C. Dove", "D. Kingfisher"], 
        "answer":"C", 
        "50-50 lifeline":["C", "D"], 
        "amount":"₹1,60,000", 
        "hint":"Name of soap", 
        "milestone":"10,000", 
        "quit":"80,000"
    },
    {
        "question": "Q7. Tower of Victory or Vijay Stambh in Rajasthan is located in__?", 
        "options": ["A. Ajmer", "B. Chittorgarh", "C. Jaipur", "D Udaipur"], 
        "answer":"B", 
        "50-50 lifeline":["B", "D"], 
        "amount":"₹3,20,000", 
        "hint":"Its architect was Rao Jaita", 
        "milestone":"3,20,000", 
        "quit":"1,60,000"
    },
    {
        "question": "Q8. Which god is also known as 'Gauri Nandan'?", 
        "options": ["A. Ganesha", "B. Indra", "C. Agni", "D. Hanuman"], 
        "answer":"A", 
        "50-50 lifeline":["A", "C"], 
        "amount":"₹6,40,000", 
        "hint":"He likes to eat modak", 
        "milestone":"3,20,000", 
        "quit":"3,20,000"
    },
    {
        "question": "Q9. What does not grow on tree according to a popular Hindi saying?", 
        "options": ["A. Fruits", "B. Money", "C. Leaves", "D. Flowers"], 
        "answer":"B", 
        "50-50 lifeline":["B", "D"], 
        "amount":"₹12,50,000", 
        "hint":"Everybody wants this", 
        "milestone":"3,20,000", 
        "quit":"6,40,000"
    },
    {
        "question": "Q10. Which city is known as Pink City in India?", 
        "options": ["A. Maysore", "B. Banglore", "C. Jaipur", "D. Kochi"], 
        "answer":"C", 
        "50-50 lifeline":["A", "C"], 
        "amount":"₹25,00,000", 
        "hint":"Jalmahal is situated", 
        "milestone":"3,20,000", 
        "quit":"12,50,000"
    },
    {
        "question": "Q11. Who is popularly called as the Iron Man of india?", 
        "options": ["A. Subhash Chandra Bose", "B. Sardar Vallabhbhai patel", "C. Jawaharlal Nehru", "D. Govind Ballabh pant"], 
        "answer":"B", 
        "50-50 lifeline":["B", "D"], 
        "amount":"₹50,00,000", 
        "hint":"He played a leading role in the Indian freedom struggle and became the first Deputy prime Minister and Home Minister of India. He is credited with achieving political integration of India.", 
        "milestone":"3,20,000", 
        "quit":"25,00,000"
    },
    {
        "question": "Q12. Name the national river of India?", 
        "options": ["A. Gangotri", "B. Narmada", "C. Ganga", "D. Godavari"], 
        "answer":"C", "50-50 lifeline":["A", "C"], 
        "amount":"₹1 Crore", 
        "hint":"This is the longest river in India", 
        "milestone":"3,20,000", 
        "quit":"50,00,000"
    },
    {
        "question": "Q13. Which of the followingis the capital of Arunachal Pradesh?", 
        "options": ["A. Dispur", "B. Itanagar", "C. Imphal", "D. Panaji"], 
        "answer":"B", 
        "50-50 lifeline":["A", "B"], 
        "amount":"₹5 Crore", 
        "hint":"Its fine Tibetan architecture and varied tribal culture", 
        "milestone":"3,20,000", 
        "quit":"1 Crore"
    }
]

count=0
# questions print krane ke liye for loop 
for i in KBC:
 print( )
 print(i["question"])
 print( )
# options print krane ke liye for loop
 for a in (i["options"]):
  print(a)
 print( )
 print("If you want lifeline you press `l` key\nIf you want quit the game you press `0`")
# answer ke liye ek user input or sure hai ya nhi uske liye dusra user input
 user=input("Enter your answer in A B C D:")
 sure=input("Are you sure lock your answer?(yes/no)")
 if sure =="yes":
  print("ok")
 elif sure=="no":
# agr user sure nhi hai to dobara answer ke liye user input
  user=input("Enter your answer in A B C D again:")
 if user=='0':
  print("Congratulation You Won ₹",i["quit"])
  break
 elif user== i["answer"]:
  print("Congratulation You Won",i["amount"])
 elif user =="l":
  print("If you want 50-50 lifeline you press `50`\nIf you want expert hint lifeline you press `h`")
# lifeline print krane or konsi lifeline chahiye uske liye ek user input 
  user2=input("Which lifeline do you want?\nEnter :")
  if count==2:
   print("You have used both lifelines")
  elif user2=="50":
   print(i["50-50 lifeline"])
  elif user2=="h":
   print(i["hint"])
   count=count+1
# uske liye user input
  user3=input("Enter your answer:")
  if user3==i["answer"]:
   print("Congratulation You Won",i["amount"])
  else:
   print("Ufff your answer is wrong")
   print("Write answer is",i["answer"])
   print(i["milestone"])
   break
 else:
  print("Ufff your answer is wrong")
  print("Write answer is",i["answer"])
  print(i["milestone"])
  break




