import sys
import os
import ctypes
import requests
import tempfile
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
import threading
from tkinter import font

class ActivationTool:
    def __init__(self, root):
        # 设置窗口标题和大小
        self.root = root
        self.root.title("激活工具内部测试专用")
        self.root.geometry("800x650")
        self.root.resizable(False, False)
        
        # 确保中文显示正常并设置默认字体
        default_font = font.Font(family="SimHei", size=12)
        self.root.option_add("*Font", default_font)
        
        # 设置样式
        self.style = ttk.Style()
        
        # 顶部标题样式
        self.style.configure("Header.TLabel", font=("SimHei", 14, "bold"), foreground="#2c3e50")
        # 版本信息样式
        self.style.configure("Version.TLabel", font=("SimHei", 12), foreground="#7f8c8d")
        # 主标题样式
        self.style.configure("Title.TLabel", font=("SimHei", 14, "bold"), foreground="#e74c3c")
        # 按钮样式
        self.style.configure("Primary.TButton", font=("SimHei", 12, "bold"), padding=10)
        # 说明标题样式
        self.style.configure("DescTitle.TLabel", font=("SimHei", 12, "bold"), foreground="#3498db")
        # 说明文本样式
        self.style.configure("DescText.TLabel", font=("SimHei", 11), foreground="#34495e")
        
        # 创建主容器
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建顶部信息区域
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, text="激活工具内部测试专用", style="Header.TLabel").pack(anchor=tk.W)
        ttk.Label(header_frame, text="及叔原创工具 2025.9.2", style="Version.TLabel").pack(anchor=tk.W)
        
        # 创建分隔线
        ttk.Separator(main_frame, orient="horizontal").pack(fill=tk.X, pady=10)
        
        # 创建大标题区域
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(
            title_frame, 
            text="激活工具内部测试，本工具仅供测试交流请勿用作商业用途，侵删",
            style="Title.TLabel",
            wraplength=750,
            justify=tk.CENTER
        )
        title_label.pack(anchor=tk.CENTER)
        
        # 创建按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # 第一个按钮
        self.btn_all_in_one = ttk.Button(
            button_frame,
            text="下载并运行全功能激活工具",
            command=self.download_and_run_all_in_one,
            style="Primary.TButton",
            width=35
        )
        self.btn_all_in_one.pack(pady=10)
        
        # 第二个按钮
        self.btn_hwid = ttk.Button(
            button_frame,
            text="下载并启动单数字激活工具",
            command=self.download_and_run_hwid,
            style="Primary.TButton",
            width=35
        )
        self.btn_hwid.pack(pady=10)
        
        # 创建分隔线
        ttk.Separator(main_frame, orient="horizontal").pack(fill=tk.X, pady=15)
        
        # 创建说明区域
        desc_frame = ttk.Frame(main_frame)
        desc_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 全功能工具说明
        ttk.Label(desc_frame, text="全功能激活工具说明：", style="DescTitle.TLabel").pack(anchor=tk.W, pady=(0, 5))
        all_in_one_desc = """
这是一个集成了多种激活方式的综合工具，包含以下功能：
- 支持Windows和Office多种版本激活
- 提供多种激活方法选择（数字许可证、KMS等）
- 包含激活状态检查和维护功能
- 适合需要灵活选择激活方式的用户使用

运行后请根据提示选择适合的激活选项，通常选择推荐选项即可。
        """
        ttk.Label(
            desc_frame, 
            text=all_in_one_desc.strip(), 
            style="DescText.TLabel",
            wraplength=750,
            justify=tk.LEFT
        ).pack(anchor=tk.W, pady=(0, 15))
        
        # 单数字激活工具说明
        ttk.Label(desc_frame, text="单数字激活工具说明：", style="DescTitle.TLabel").pack(anchor=tk.W, pady=(0, 5))
        hwid_desc = """
这是一个专注于数字许可证激活的工具，特点如下：
- 采用HWID（硬件ID）数字激活方式
- 激活后与硬件绑定，重装系统可自动激活
- 操作简单，一键完成激活过程
- 适合个人用户永久激活Windows系统

运行后工具会自动执行激活过程，无需额外操作，完成后会显示激活结果。
        """
        ttk.Label(
            desc_frame, 
            text=hwid_desc.strip(), 
            style="DescText.TLabel",
            wraplength=750,
            justify=tk.LEFT
        ).pack(anchor=tk.W)
        
        # 状态标签
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=10)
        
        self.status_label = ttk.Label(status_frame, text="就绪", font=("SimHei", 11), foreground="green")
        self.status_label.pack(anchor=tk.W)
        
        # 定义下载链接
        self.all_in_one_links = [
            "https://gh.xmly.dev/github.com/massgravel/Microsoft-Activation-Scripts/raw/refs/heads/master/MAS/All-In-One-Version-KL/MAS_AIO.cmd",
            "https://gh-proxy.com/github.com/massgravel/Microsoft-Activation-Scripts/raw/refs/heads/master/MAS/All-In-One-Version-KL/MAS_AIO.cmd",
            "https://github.com/massgravel/Microsoft-Activation-Scripts/raw/refs/heads/master/MAS/All-In-One-Version-KL/MAS_AIO.cmd"
        ]
        
        self.hwid_links = [
            "https://gh.xmly.dev/github.com/massgravel/Microsoft-Activation-Scripts/raw/refs/heads/master/MAS/Separate-Files-Version/Activators/HWID_Activation.cmd",
            "https://gh-proxy.com/github.com/massgravel/Microsoft-Activation-Scripts/raw/refs/heads/master/MAS/Separate-Files-Version/Activators/HWID_Activation.cmd",
            "https://github.com/massgravel/Microsoft-Activation-Scripts/raw/refs/heads/master/MAS/Separate-Files-Version/Activators/HWID_Activation.cmd"
        ]
    
    def update_status(self, message, is_error=False):
        """更新状态标签"""
        self.status_label.config(text=message, foreground="red" if is_error else "green")
        self.root.update_idletasks()
    
    def download_file(self, url_list, filename):
        """尝试从多个链接下载文件"""
        for url in url_list:
            try:
                domain = url.split('//')[1].split('/')[0]
                self.update_status(f"尝试从 {domain} 下载...")
                response = requests.get(url, timeout=15)
                if response.status_code == 200:
                    # 创建临时文件
                    temp_dir = tempfile.gettempdir()
                    file_path = os.path.join(temp_dir, filename)
                    
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    
                    self.update_status(f"下载成功: {filename}")
                    return file_path
            except Exception as e:
                self.update_status(f"从 {domain} 下载失败: {str(e)}", is_error=True)
                continue
        
        self.update_status("所有链接都下载失败", is_error=True)
        return None
    
    def run_command_file(self, file_path):
        """以管理员身份运行CMD文件"""
        try:
            self.update_status("准备运行脚本...")
            # 使用管理员权限运行
            subprocess.run(
                f'cmd /c "{file_path}"',
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.update_status("脚本运行完成")
            return True
        except Exception as e:
            self.update_status(f"运行脚本时出错: {str(e)}", is_error=True)
            return False
    
    def download_and_run_all_in_one(self):
        """下载并运行全功能激活工具"""
        self.disable_buttons()
        threading.Thread(target=self._download_and_run, args=(self.all_in_one_links, "MAS_AIO.cmd")).start()
    
    def download_and_run_hwid(self):
        """下载并运行HWID激活工具"""
        self.disable_buttons()
        threading.Thread(target=self._download_and_run, args=(self.hwid_links, "HWID_Activation.cmd")).start()
    
    def _download_and_run(self, links, filename):
        """下载并运行的内部实现"""
        file_path = self.download_file(links, filename)
        if file_path:
            self.run_command_file(file_path)
        self.enable_buttons()
    
    def disable_buttons(self):
        """禁用按钮"""
        self.btn_all_in_one.config(state=tk.DISABLED)
        self.btn_hwid.config(state=tk.DISABLED)
    
    def enable_buttons(self):
        """启用按钮"""
        self.root.after(0, lambda: self.btn_all_in_one.config(state=tk.NORMAL))
        self.root.after(0, lambda: self.btn_hwid.config(state=tk.NORMAL))

def is_admin():
    """检查程序是否以管理员身份运行"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """以管理员身份重新启动程序"""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )

def main():
    # 检查是否以管理员身份运行，如果不是则重新启动
    if not is_admin():
        run_as_admin()
        sys.exit()
    
    # 创建主窗口
    root = tk.Tk()
    app = ActivationTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    