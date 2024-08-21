import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Cửa sổ GUI đơn giản")
root.geometry("400x300")

# Tạo nhãn (label)
label = tk.Label(root, text="Chào mừng bạn đến với GUI bằng Tkinter!")
label.pack(pady=20)

# Tạo nút (button)
def on_button_click():
    label.config(text="Bạn vừa nhấn nút!")

button = tk.Button(root, text="Nhấn vào đây", command=on_button_click)
button.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
