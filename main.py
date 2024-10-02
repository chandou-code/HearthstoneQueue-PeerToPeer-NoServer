import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import time
import os
import subprocess
import pyautogui
import time
import threading
import requests
import psutil


def fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        item = soup.select_one('#item_55700674 > div:nth-of-type(2) > a')

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


def compare_results(old_data, new_data, file_path):
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
    file_path = config['file_path']
    filename = 'data.txt'
    check_log_file = 'check_log.txt'

    check_count = read_check_count(check_log_file)

    while True:
        current_time = datetime.now()

        current_hour = current_time.hour

        if (current_hour >= 23) or (current_hour < 9):
            print("当前时间在休眠区间，暂停运行...")
            time.sleep(60)
            continue

        try:

            new_data = fetch_data(url, headers)

            if new_data is not None:
                old_data = read_data(filename)
                save_data(new_data, filename)
                if old_data is not None:
                    result = compare_results(old_data, new_data, file_path)
                    if result == 1:
                        print("在线笔记未变化")
                    elif result == 0:
                        print("已变化，启动排队")
                else:
                    print("没有先前的数据进行比较")

            log_check_count(check_count, check_log_file)
            check_count += 1
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            time.sleep(30)
            continue

        time.sleep(8)


def read_check_count(log_file):
    """读取上次检查次数"""
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                count_str = last_line.split(':')[-1].strip()
                print(count_str)
                return int(count_str)  # 转换为整数并返回
    except (FileNotFoundError, ValueError):
        return 0  # 文件不存在或内容格式错误时返回0


def log_check_count(count, log_file):
    """记录检查次数到文件"""
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now()} - 检查次数: {count}\n")


def run_(file_path):
    try:
        while 1:
            subprocess.Popen(file_path)
            process_name = 'Battle.net.exe'
            count, pids = get_process_count(process_name)
            print(count, pids)
            if count < 5:
                time.sleep(5)
                continue

            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)

            for _ in range(16):
                pyautogui.press('tab')
                time.sleep(0.05)

            # 按下回车键
            pyautogui.press('enter')
            print("回车键已按下")
            break



    except Exception as e:
        print(f"启动失败: {e}")


def get_process_count(process_name):
    count = 0
    pids = []
    for process in psutil.process_iter(['name', 'pid']):
        try:
            if process.info['name'] == process_name:
                count += 1
                pids.append(process.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return count, pids


if __name__ == '__main__':
    # print(read_config()['file_path'])

    main()
    # file_path = r"E:\Battle.net\Battle.net.exe"
    # run_(file_path)
