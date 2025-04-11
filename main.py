import tkinter as tk

def calculate():
    try:
        a = int(a_entry.get())
        b_values = list(map(int, b_entry.get().split()))  # 将输入的 b 转换为整数列表
    except ValueError:
        result_label.config(text="请输入有效整数")
        return
    
    results = []
    for b in b_values:
        for x in range(1, 13):  # 遍历 x 的可能值
            for y in range(1, 13):  # 遍历 y 的可能值
                if x + b == a and 2 * b - a == y:
                    results.append(f"指定 {b} 星怪兽 -> 需要 2 张 {x} 星超量怪兽，1 张 {y} 星融合怪兽")
    
    if results:
        result_label.config(text="\n".join(results))
    else:
        result_label.config(text="无法发动联栗炮")

# 创建主窗口
window = tk.Tk()
window.title("联栗炮计算器")

# 输入字段和标签
tk.Label(window, text="双方场上和手牌数量和:").grid(row=0, column=0, padx=5, pady=5)
a_entry = tk.Entry(window)
a_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="对手场上怪兽星级\n(多只怪兽用空格分隔):").grid(row=1, column=0, padx=5, pady=5)
b_entry = tk.Entry(window)
b_entry.grid(row=1, column=1, padx=5, pady=5)

# 计算按钮
tk.Button(window, text="计算", command=calculate).grid(row=2, columnspan=2, padx=5, pady=5)

# 结果显示
result_label = tk.Label(window, text="", fg="blue")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

window.mainloop()