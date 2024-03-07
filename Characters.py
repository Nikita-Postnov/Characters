import tkinter as tk

def count_characters():
    text = text_entry.get("1.0", tk.END)
    num_characters = len(text) - 1  # Исключаем символ новой строки в конце текста
    result_label.config(text=f"Количество символов: {num_characters}")

root = tk.Tk()
root.title("Считывание количества символов")

text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack(pady=10)

count_button = tk.Button(root, text="Посчитать", command=count_characters)
count_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()
