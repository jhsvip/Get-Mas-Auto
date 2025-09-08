# Get-Mas-Auto
MAS Downloader / MAS 下载器
A convenient tool to download and run the latest Microsoft Activation Scripts (MAS), featuring multi-source downloading and simplified activation process.
一个便捷的工具，用于下载和运行最新的 Microsoft Activation Scripts (MAS)，具备多源下载和简化激活流程的功能。
Features / 功能特点
🚀 Automatically downloads the latest HWID activation script from official sources
🚀 自动从官方源下载最新的 HWID 激活脚本
🔗 Built-in multiple backup links to bypass network restrictions
🔗 内置多个备用链接，解决网络访问限制问题
🔒 Intelligent handling of SSL certificate verification issues
🔒 智能处理 SSL 证书验证问题，提高下载成功率
🖥️ Automatically runs activation scripts with administrator privileges
🖥️ 自动以管理员权限运行激活脚本
📱 Graphical user prompts for intuitive operation
📱 图形化提示界面，操作更直观
System Requirements / 适用环境
Operating System: Windows 7/8/8.1/10/11 (32-bit/64-bit)
操作系统：Windows 7/8/8.1/10/11（32 位 / 64 位）
Permissions: Requires administrator privileges (for activation process)
运行权限：需要管理员权限（激活操作要求）
Network: Internet connection required (to download activation scripts)
网络环境：需联网（用于下载激活脚本）
Installation & Usage / 安装与使用
Method 1: Use precompiled executable (Recommended) / 方法 1：使用编译好的程序（推荐）
Go to the Releases page and download the latest MAS-Downloader.exe
前往发布页下载最新版MAS-Downloader.exe
Right-click the program and select "Run as administrator"
右键点击程序，选择「以管理员身份运行」
Follow the prompts:
跟随提示完成操作：
The program will automatically download the activation script (with progress bar)
程序会自动下载激活脚本（显示进度条）
Automatically run the activation tool after download completion
下载完成后自动运行激活工具
Follow the instructions in the activation tool to complete the process
按激活工具内的提示完成最终激活
Method 2: Run from source code / 方法 2：从源码运行

Install dependencies:
安装依赖：
bash
pip install requests

Run the script (with administrator privileges):
运行脚本（需管理员权限）：
bash
python mas_downloader.py

Working Principle / 工作原理
The program retrieves the official HWID activation script from multiple sources (from the Microsoft-Activation-Scripts project)
程序通过多个来源获取官方 HWID 激活脚本（来自Microsoft-Activation-Scripts项目）
Saves the script to the user's Downloads folder (~/Downloads)
将脚本保存至用户下载目录（~/Downloads）
Automatically launches the script with necessary parameters and administrator privileges
自动以管理员权限启动脚本并传入必要参数
Notifies users of operation progress through graphical prompts
通过图形化提示告知用户操作进度
Notes / 注意事项
This tool only provides download and execution assistance for activation scripts. The core activation functionality is implemented by the official scripts
本工具仅提供激活脚本的下载与运行辅助，激活核心功能由官方脚本实现
Ensure your Windows system is a genuine licensed version or complies with Microsoft's license terms
请确保你的 Windows 系统为正版授权或符合微软许可条款的版本
Some antivirus software may falsely flag the activation tool. You can temporarily disable it or add to trusted list
部分杀毒软件可能误报激活工具，可暂时关闭或添加信任
If it fails to run, try:
若运行失败，建议：
Checking network connection
检查网络连接
Ensuring it's run with administrator privileges
确认已以管理员身份运行
Trying again after disabling VPN or proxy
尝试关闭 VPN 或代理后重试
License / 许可证
This project is open-source under the MIT License. You are free to use, modify, and distribute it, but must retain the original author information.
本项目基于MIT 许可证开源，你可以自由使用、修改和分发，但需保留原作者信息。

The activation scripts themselves are subject to the license of their original project (MIT License).
激活脚本本身遵循其原项目的许可协议（MIT License）。
Disclaimer / 免责声明
This tool is for educational and testing purposes only. Please ensure compliance with local laws and regulations and Microsoft's software license terms before use. The user assumes full responsibility for any issues arising from improper use.
本工具仅用于学习和测试目的，请在使用前确保符合当地法律法规及微软软件许可条款。对于违规使用导致的任何问题，使用者自行承担责任。
Screenshots / 程序截图<img width="1188" height="1011" alt="661e1926-4dc8-46f3-9071-ac3988bdb928" src="https://github.com/user-attachments/assets/04112050-8716-4551-a0bd-2761079d0cca" />

MAS official website ：/ mas官方网站：https://massgrave.dev/
