import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def compress_images():
    # 获取用户选择的多个图片文件
    file_paths = filedialog.askopenfilenames()
    
    # 获取用户输入的压缩大小
    compress_size = entry.get()

    if not compress_size:
        messagebox.showerror("錯誤", "請輸入壓縮大小KB")
        return
    
    compress_size = int(compress_size)  # 将输入的压缩大小转换为整数

    # 获取当前文件夹路径
    current_folder_path = os.path.dirname(file_paths[0])

    # 创建新文件夹用于存放压缩后的图片
    new_folder_path = os.path.join(current_folder_path, "壓縮圖片")
    os.makedirs(new_folder_path, exist_ok=True)

    # 遍历每个选择的图片文件，压缩并保存到新文件夹中，保留原始文件名
    for file_path in file_paths:
        img = Image.open(file_path)
        
        # 初始化压缩质量
        quality = 100
        new_file_path = os.path.join(new_folder_path, os.path.basename(file_path))
        img.save(new_file_path, quality=quality)
        
        # 检查保存后的文件大小，如果大于目标大小，则逐步降低压缩质量直到满足条件
        while os.path.getsize(new_file_path)/1024 > compress_size:
            quality -= 5
            img.save(new_file_path, quality=quality)

# 建立視窗
root = tk.Tk()
root.title("圖片編輯器")

# 设置窗口大小
root.geometry("300x200")

# 建立提示文字
label = tk.Label(root, text="請輸入壓縮KB", font=("Arial", 14))
label.grid(row=0, column=0, padx=(20, 10), pady=(20, 10))

# 建立輸入框
entry = tk.Entry(root, width=10, font=("Arial", 14), fg="black", bg="white")
entry.grid(row=1, column=0, padx=(20, 10), pady=10)

# 建立按鈕
button = tk.Button(root, text="選擇多張圖片進行壓縮", font=("Arial", 14), command=compress_images)
button.grid(row=2, column=0, padx=(20, 10), pady=(10, 20))

# 设置行和列的权重，使其在垂直和水平方向上平分空间
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# 让组件保持在窗口正中央
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# 啟動視窗
root.mainloop()