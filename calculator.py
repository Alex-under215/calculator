# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:42:17 2025

@author: Александр
"""

import tkinter as tk

def click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

# Создание окна
window = tk.Tk()
window.title("Калькулятор")

# Поле ввода
entry = tk.Entry(window, width=25, font=("Arial", 16), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Кнопки
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '=':
            btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
        else:
            btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click(t))
        btn.grid(row=i+1, column=j)

# Кнопка очистки
clear_btn = tk.Button(window, text="C", width=22, height=2, font=("Arial", 14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4)

# Запуск GUI
window.mainloop()
