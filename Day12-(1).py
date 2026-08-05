import sqlite3

def connect_db():
    conn = sqlite3.connect("todo_app.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
 
def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        )
    """)
    
    conn.commit()
    conn.close()

def create_category(name):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def create_task(title, category_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO tasks (title, completed, category_id) VALUES (?, 0, ?)", 
            (title, category_id)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def read_all_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT tasks.id, tasks.title, tasks.completed, categories.name 
        FROM tasks 
        LEFT JOIN categories ON tasks.category_id = categories.id
    """
    cursor.execute(query)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def read_tasks_by_category(category_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, completed FROM tasks WHERE category_id = ?", (category_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, completed):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
    conn.commit()
    conn.close()

def update_task_details(task_id, new_title, new_category_id):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE tasks SET title = ?, category_id = ? WHERE id = ?", 
            (new_title, new_category_id, task_id)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_category(category_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    conn.commit()
    conn.close()
# Add this at the very bottom of your file to see the formatted output

if __name__ == "__main__":
    # Initialize the database and add test data
    init_db()
    create_category("Office Tasks")
    create_task("Review database code", category_id=1)
    create_task("Submit intern progress report", category_id=1)
    
    # Fetch the tasks
    tasks = read_all_tasks()
    
    # Print the table header
    print(f"\n{'ID':<5} | {'Task Title':<35} | {'Status':<10} | {'Category':<15}")
    print("-" * 75)
    
    # Loop and print each row cleanly
    for task_id, title, completed, category_name in tasks:
        status = "✅ Done" if completed == 1 else "⏳ Pending"
        category = category_name if category_name else "None"
        print(f"{task_id:<5} | {title:<35} | {status:<10} | {category:<15}")
    print()
def show_menu():
    """Displays the interactive options menu."""
    print("\n" + "="*30)
    print("      📝 TO-DO APP MENU")
    print("="*30)
    print("1. ➕ Add a Category")
    print("2. 📝 Add a Task")
    print("3. 📋 View All Tasks")
    print("4. ✅ Mark Task as Done")
    print("5. ❌ Delete a Task")
    print("6. 🚪 Exit")
    print("="*30)

if __name__ == "__main__":
    # Ensure database tables exist before launching menu
    init_db()
    
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            cat_name = input("Enter new category name: ").strip()
            if cat_name:
                if create_category(cat_name):
                    print(f"🎉 Category '{cat_name}' added successfully!")
                else:
                    print("⚠️ Category already exists.")
                    
        elif choice == "2":
            task_title = input("Enter task title: ").strip()
            if task_title:
                print("\nLeave empty if uncategorized.")
                cat_id_input = input("Enter Category ID (Number): ").strip()
                cat_id = int(cat_id_input) if cat_id_input.isdigit() else None
                
                if create_task(task_title, cat_id):
                    print(f"🚀 Task '{task_title}' added!")
                else:
                    print("⚠️ Failed to add task. Make sure the Category ID exists.")
                    
        elif choice == "3":
            tasks = read_all_tasks()
            if not tasks:
                print("\n📭 Your to-do list is completely empty!")
            else:
                print(f"\n{'ID':<5} | {'Task Title':<35} | {'Status':<10} | {'Category':<15}")
                print("-" * 75)
                for task_id, title, completed, category_name in tasks:
                    status = "✅ Done" if completed == 1 else "⏳ Pending"
                    category = category_name if category_name else "None"
                    print(f"{task_id:<5} | {title:<35} | {status:<10} | {category:<15}")
                    
        elif choice == "4":
            task_id = input("Enter the ID of the task to complete: ").strip()
            if task_id.isdigit():
                update_task_status(int(task_id), 1)
                print(f"🎯 Task {task_id} marked as completed!")
            else:
                print("⚠️ Invalid ID number.")
                
        elif choice == "5":
            task_id = input("Enter the ID of the task to delete: ").strip()
            if task_id.isdigit():
                delete_task(int(task_id))
                print(f"🗑️ Task {task_id} deleted successfully.")
            else:
                print("⚠️ Invalid ID number.")
                
        elif choice == "6":
            print("\n👋 Goodbye! Your tasks are safely saved in the database.")
            break
            
        else:
            print("⚠️ Invalid choice. Please select a number between 1 and 6.")
