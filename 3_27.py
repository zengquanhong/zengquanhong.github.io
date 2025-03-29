import tkinter as tk
from tkinter import messagebox

# 计算阶乘的函数
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 判断质数的函数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 生成斐波那契数列的函数
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# 当点击按钮时执行相应的操作
def calculate():
    try:
        n = int(entry.get())  # 获取用户输入的数字
        choice = var.get()  # 获取用户选择的功能

        if choice == 1:
            result = factorial(n)
            messagebox.showinfo("结果", f"{n} 的阶乘是 {result}")
        elif choice == 2:
            result = "是质数" if is_prime(n) else "不是质数"
            messagebox.showinfo("结果", f"{n} {result}")
        elif choice == 3:
            result = fibonacci(n)
            messagebox.showinfo("结果", f"前 {n} 项斐波那契数列是 {result}")
        else:
            messagebox.showerror("错误", "请选择一个有效的功能")
    except ValueError:
        messagebox.showerror("错误", "请输入一个有效的数字")

# 创建主窗口
root = tk.Tk()
root.title("功能选择")

# 标签
label = tk.Label(root, text="请输入一个数字:")
label.pack(pady=10)

# 输入框
entry = tk.Entry(root)
entry.pack(pady=10)

# 单选框：选择功能
var = tk.IntVar()
radio_factorial = tk.Radiobutton(root, text="计算阶乘", variable=var, value=1)
radio_prime = tk.Radiobutton(root, text="判断质数", variable=var, value=2)
radio_fibonacci = tk.Radiobutton(root, text="生成斐波那契数列", variable=var, value=3)

radio_factorial.pack()
radio_prime.pack()
radio_fibonacci.pack()

# 按钮：执行计算
button = tk.Button(root, text="计算", command=calculate)
button.pack(pady=20)

# 启动主循环
root.mainloop()
