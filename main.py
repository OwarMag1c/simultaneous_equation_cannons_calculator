import tkinter as tk

def calculate():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
    except ValueError:
        result_label.config(text="请输入有效整数")
        return
    
    x = a - b
    y = 2 * b - a
    
    if x > 0 and y > 0 and x < 13 and y < 13:
        result_label.config(text=f"超量怪兽星级：{x}，融合怪兽星级：{y}")
    else:
        result_label.config(text="无法发动")

# 创建主窗口
window = tk.Tk()
window.title("卡片星级计算器")

# 输入字段和标签
tk.Label(window, text="场上和手牌卡数总和（a）:").grid(row=0, column=0, padx=5, pady=5)
a_entry = tk.Entry(window)
a_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="对手怪兽星级总和（b）:").grid(row=1, column=0, padx=5, pady=5)  # 已修正
b_entry = tk.Entry(window)
b_entry.grid(row=1, column=1, padx=5, pady=5)

# 计算按钮
tk.Button(window, text="计算星级", command=calculate).grid(row=2, columnspan=2, padx=5, pady=5)

# 结果显示
result_label = tk.Label(window, text="", fg="blue")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

window.mainloop()