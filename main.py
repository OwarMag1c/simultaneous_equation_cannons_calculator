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
        result_label.config(text=f"需要 2 张 {x} 星超量怪兽，1 张 {y} 星融合怪兽")
    else:
        result_label.config(text="无法发动联栗炮")

# 创建主窗口
window = tk.Tk()
window.title("联栗炮计算器")

# 输入字段和标签
tk.Label(window, text="双方场上和手牌数量和:").grid(row=0, column=0, padx=5, pady=5)
a_entry = tk.Entry(window)
a_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="指定对手场上怪兽星级:").grid(row=1, column=0, padx=5, pady=5)
b_entry = tk.Entry(window)
b_entry.grid(row=1, column=1, padx=5, pady=5)

# 计算按钮
tk.Button(window, text="计算", command=calculate).grid(row=2, columnspan=2, padx=5, pady=5)

# 结果显示
result_label = tk.Label(window, text="", fg="blue")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

window.mainloop()