import sqlite3
import tkinter as tk
from tkinter import ttk

# Создаем базу данных и таблицу для хранения информации о сотрудниках
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    full_name TEXT,
                    phone_number TEXT,
                    email TEXT,
                    salary REAL)''')
conn.commit()

def add_employee():
    full_name = full_name_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()

    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (full_name, phone_number, email, salary) VALUES (?, ?, ?, ?)",
                   (full_name, phone_number, email, salary))
    conn.commit()
    conn.close()

    full_name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)

def search_employee():
    full_name = full_name_search_entry.get()
    
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE full_name LIKE ?", ('%' + full_name + '%',))
    employees = cursor.fetchall()
    conn.close()
    
    result_list.delete(0, tk.END)
    
    if employees:
        for employee in employees:
            result_list.insert(tk.END, f"ID: {employee[0]}, ФИО: {employee[1]}, Номер телефона: {employee[2]}, Email: {employee[3]}, Заработная плата: {employee[4]}")
    else:
        result_list.insert(tk.END, "Сотрудник не найден.")

# Создаем графический интерфейс с использованием Tkinter
root = tk.Tk()
root.title("Список сотрудников компании")

# Ввод информации о сотруднике
add_frame = tk.Frame(root)
add_frame.pack(pady=20)
full_name_label = tk.Label(add_frame, text="ФИО")
full_name_label.grid(row=0, column=0)
full_name_entry = tk.Entry(add_frame)
full_name_entry.grid(row=0, column=1)
phone_number_label = tk.Label(add_frame, text="Номер телефона")
phone_number_label.grid(row=1, column=0)
phone_number_entry = tk.Entry(add_frame)
phone_number_entry.grid(row=1, column=1)
email_label = tk.Label(add_frame, text="Email")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(add_frame)
email_entry.grid(row=2, column=1)
salary_label = tk.Label(add_frame, text="Заработная плата")
salary_label.grid(row=3, column=0)
salary_entry = tk.Entry(add_frame)
salary_entry.grid(row=3, column=1)
add_button = tk.Button(add_frame, text="Добавить сотрудника", command=add_employee)
add_button.grid(row=4, columnspan=2)

# Поиск сотрудника
search_frame = tk.Frame(root)
search_frame.pack(pady=20)
full_name_search_label = tk.Label(search_frame, text="Поиск по ФИО")
full_name_search_label.grid(row=0, column=0)
full_name_search_entry = tk.Entry(search_frame)
full_name_search_entry.grid(row=0, column=1)
search_button = tk.Button(search_frame, text="Найти сотрудника", command=search_employee)
search_button.grid(row=1, columnspan=2)
result_list = tk.Listbox(search_frame, width=50)
result_list.grid(row=2, columnspan=2)

root.mainloop()
