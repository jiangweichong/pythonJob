import pygetwindow as gw
import pyautogui

# 获取所有浏览器窗口（以Chrome为例）
browser_windows = [w for w in gw.getAllWindows() if 'chrome' in w.title.lower()]

if not browser_windows:
    print("未检测到Chrome浏览器窗口。")
else:
    print("检测到以下Chrome窗口：")
    for idx, win in enumerate(browser_windows):
        print(f"{idx}: {win.title}")

    idx = int(input("请选择窗口编号："))
    selected_win = browser_windows[idx]
    selected_win.activate()  # 激活窗口

    # 示例：在窗口中心点击
    x, y, width, height = selected_win.left, selected_win.top, selected_win.width, selected_win.height
    pyautogui.click(x + width // 2, y + height // 2)
    print("已在窗口中心点击。")