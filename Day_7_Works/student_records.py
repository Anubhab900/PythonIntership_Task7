def updateRecords(student):
    entriesForUpdate = int(input("Enter number of entries to update: "))
    for _ in range(entriesForUpdate):
        field = input(
            "Enter field to update (name, rollno, age, coarse, marks): "
        ).strip().lower()

        if field not in student:
            print("Invalid field name. Skipping update.")
            continue

        value = input(f"Enter new value for {field}: ")

        if field in ["rollno", "age"]:
            student[field] = int(value)
        elif field == "marks":
            student[field] = float(value)
        else:
            student[field] = value


def deleteRecords(student):
    entriesForDelete = int(input("Enter number of entries to delete: "))
    for _ in range(entriesForDelete):
        field = input(
            "Enter field to delete (name, rollno, age, coarse, marks): "
        ).strip().lower()

        if field not in student:
            print("Invalid field name. Skipping deletion.")
            continue

        student[field] = None   # deleted


def printStudentDetails(student):
    print("\nStudent Details:")
    for key, value in student.items():
        print(f"{key}: {value}")


def student_records():
    student = {
        "name": input("Enter Student Name: "),
        "rollno": int(input("Enter Roll No: ")),
        "age": int(input("Enter Age: ")),
        "coarse": input("Enter Course Name: "),
        "marks": float(input("Enter Marks: "))
    }

    option = input(
        "Do you want to update, delete or print records? (update/delete/print): "
    ).strip().lower()
    
    JsonOps=input("Do you want to display JSON from the file? (yes/no): ").strip().lower()

    if option == "update":
        updateRecords(student)
    elif option == "delete":
        deleteRecords(student)
    elif option == "print":
        pass
    else:
        print("Invalid option. Printing records.")

    printStudentDetails(student)

    DictToJSON(student) ## print json string.
    JsonFile = JSONToFile(student) ## write json string to file.

    if JsonOps=="yes":
        print("\nJSON Data from file:")
        #b=ReadJSONFromFile(JsonFile)
        print(ReadJSONFromFile(str(JsonFile)))


def DictToJSON(student):
    import json
    json_string =json.dumps(student, indent=4)
    return json_string

################################################################################

def JSONToFile(student):
    import json

    filename = "student_record.json"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []   # start fresh list

    data.append(student)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return filename
 
################################################################################       

def ReadJSONFromFile(file_path):
    import json
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)




# Usage
student_records()
