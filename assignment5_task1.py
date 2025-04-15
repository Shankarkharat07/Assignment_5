mark_dictionary={"Shankar":34,"Sujay":65,"Alice":77}


try:
    Name = input("Enter the Student's name: ")
    Mark = mark_dictionary[Name]
    print(Name+"'s Marks: ",Mark)
except KeyError:
    print('Student not found')