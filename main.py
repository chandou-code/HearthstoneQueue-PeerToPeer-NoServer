import json

import requests
from bs4 import BeautifulSoup
import time
import os
import subprocess
import pyautogui
import time
import threading
import requests


def fetch_data(url, headers):
    # 发送 GET 请求
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # 解析网页内容
        soup = BeautifulSoup(response.content, 'html.parser')
        # 使用 CSS 选择器找到目标元素
        item = soup.select_one('#item_55700674 > div:nth-of-type(2) > a')
        # 检查是否找到了元素，并获取文本
        if item:
            return item.get_text(strip=True)
        else:
            print("未找到指定的元素")
            return None
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None


def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)


def read_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    return None


def compare_results(old_data, new_data,file_path):
    if old_data == new_data:
        return 1
    else:
        run_(file_path)
        return 0


def read_config(filename='config.json'):
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    config = read_config()
    url = "http://www.xnote.cn/note/"
    headers = config['headers']
    sleep_time = config['sleep_time']
    file_path = config['file_path']
    filename = 'data.txt'

    while True:
        new_data = fetch_data(url, headers)

        if new_data is not None:
            old_data = read_data(filename)
            save_data(new_data, filename)
            if old_data is not None:
                result = compare_results(old_data, new_data,file_path)
                print(f"比较结果: {result}")
            else:
                print("没有先前的数据进行比较")

        time.sleep(sleep_time)


def run_(file_path):
    # 定义文件路径
    # file_path = r"E:\Battle.net\Battle.net.exe"

    # 使用 subprocess 打开程序
    try:
        subprocess.Popen(file_path)
        print("Hearthstone 启动成功！")

        # 添加延迟，以便用户可以切换到目标窗口
        time.sleep(1)  # 等待 5 秒
        pyautogui.press('enter')  # 按下回车键
        time.sleep(1)  # 等待 5 秒
        # 连续按下 Tab 键 16 次
        for _ in range(16):
            pyautogui.press('tab')  # 按下 Tab 键
            time.sleep(0.1)  # 可选：添加短暂延迟，避免过快

        # 按下回车键
        pyautogui.press('enter')  # 按下回车键
        print("回车键已按下")

    except Exception as e:
        print(f"启动失败: {e}")


if __name__ == '__main__':
    # print(read_config()['file_path'])
    main()