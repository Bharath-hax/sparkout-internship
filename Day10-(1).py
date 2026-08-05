import csv
import json
import os

# ===========================
# STUDENT RECORDS SYSTEM
# ===========================

CSV_FILE = "students.csv"

# Create CSV file if it doesn't exist
def create_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Department", "Marks"])


# Add Student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    dept = input("Enter Department: ")
    marks = input("Enter Marks: ")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, dept, marks])

    print("Student record added successfully!\n")


# Display Students
def display_students():
    print("\n------ Student Records ------")

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    print()


# ===========================
# JSON CONFIGURATION MANAGER
# ===========================

CONFIG_FILE = "config.json"


# Create default config
def create_default_config():
    if not os.path.exists(CONFIG_FILE):
        config = {
            "college_name": "ABC Engineering College",
            "max_students": 100,
            "theme": "Light"
        }

        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)


# Load Config
def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


# Validate Config
def validate_config(config):

    required_keys = ["college_name", "max_students", "theme"]

    for key in required_keys:
        if key not in config:
            return False

    return True


# Update Config
def update_config():

    config = load_config()

    print("\nCurrent Configuration")
    print(config)

    config["college_name"] = input("Enter New College Name: ")
    config["max_students"] = int(input("Enter Maximum Students: "))
    config["theme"] = input("Enter Theme (Light/Dark): ")

    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

    print("Configuration Updated Successfully!\n")


# Show Config
def show_config():

    config = load_config()

    if validate_config(config):
        print("\nConfiguration")
        print(json.dumps(config, indent=4))
    else:
        print("Invalid Configuration File")


# ===========================
# MAIN MENU
# ===========================

create_csv()
create_default_config()

while True:

    print("========== MENU ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Show Configuration")
    print("4. Update Configuration")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        show_config()

    elif choice == "4":
        update_config()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice\n")