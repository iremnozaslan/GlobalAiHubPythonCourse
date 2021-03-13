questions = [
"What is the longest river in the world?\na)Ganges\nb)Amazon\nc)Nile",
"What is the highest mountain in the world?\na)Everest\nb)Alps\nc)Diran",
"What is the largest coffee growing country in the world?\na)Italy\nb)Brazil\nc)France",
"What is the name of the biggest desert in the world?\na)Sahara\nb)Antartic\nc)Namib",
"Which of the following is used as a moderator in nuclear reactor?\na)Diamond\nb)Graphite\nc)Uranium",
"In 1610, Galileo Galilei discovered four moons of which planet?\na)Mars\nb)Saturn\nc)Jupiter",
"Which instrument is wind instrument?\na)Piano\nb)Tuba\nc)Flute",
"Who is the author of 'Diplomacy'?\na)Henry Kissinger\nb)George Orwell\nc)Pluton",
"Which country in the world's largest fishing industry?\na)Korea\nb)China\nc)Russia",
"Which city is called as 'City of Golden Gate?\na)San Francisco\nb)Newyork\nc)Los Angeles"
]
answers = {
    questions[0] : "c",
    questions[1] : "a",
    questions[2] : "b",
    questions[3] : "a",
    questions[4] : "b",
    questions[5] : "c",
    questions[6] : "c",
    questions[7] : "a",
    questions[8] : "b",
    questions[9] : "a",
}
correctAns = 0
for i in range(0,10):
    print(questions[i])
    answer = input()
    if(answer == answers.get(questions[i])):
        correctAns+=10
    else:
        continue
if(correctAns<=50):
    print("Unsuccesful")
else:
    print("Succesful")
