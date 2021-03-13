cv1 = {"name" : "Pe", "surname" : "One", "age" : 1, "email" :"1@gmail.com"}
cv2 = {"name" : "Per", "surname" : "Two", "age" : 2, "email" :"2@gmail.com"}
cv3 = {"name" : "Pers", "surname" : "Three", "age" : 3, "email" :"3@gmail.com"}
cv4 = {"name" : "Perso", "surname" : "Four", "age" : 4, "email" :"4@gmail.com"}
cv5 = {"name" : "Person", "surname" : "Five", "age" : 5, "email" :"5@gmail.com"}

cv = {"1" : cv1,
      "2" : cv2,
      "3" : cv3,
      "4" : cv4,
      "5" : cv5
      }

for id, info in cv.items():
    print("\nPerson:", id)

    for key in info:
        print(key + ":", info[key])
