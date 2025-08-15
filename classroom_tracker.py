# Classroom Resource Tracker 

classrooms = {}  

while True:
    print("\n--- Classroom Resource Tracker ---")
    print("1. Add Classroom")
    print("2. Update Classroom")
    print("3. View Classroom")
    print("4. View All Classrooms")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        room = input("Enter classroom number: ")
        if room in classrooms:
            print("Classroom already exists!")
        else:
            chairs = int(input("Enter chairs: "))
            fans = int(input("Enter fans: "))
            projectors = int(input("Enter projectors: "))
            classrooms[room] = {"chairs": chairs, "fans": fans, "projectors": projectors}
            print("Classroom added!")

    elif choice == "2":
        room = input("Enter classroom number: ")
        if room in classrooms:
            chairs = int(input("Enter chairs: "))
            fans = int(input("Enter fans: "))
            projectors = int(input("Enter projectors: "))
            classrooms[room]["chairs"] = chairs
            classrooms[room]["fans"] = fans
            classrooms[room]["projectors"] = projectors
            print("Classroom updated!")
        else:
            print("Classroom not found!")

    elif choice == "3":
        room = input("Enter classroom number: ")
        if room in classrooms:
            print("Classroom:", room)
            for item, count in classrooms[room].items():
                print(item, ":", count)
        else:
            print("Classroom not found!")

    elif choice == "4":
        if len(classrooms) == 0:
            print("No classrooms available!")
        else:
            for r in classrooms:
                print(r, ":", classrooms[r])

    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
