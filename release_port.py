#!/usr/bin/env python3

import subprocess

def release_port(port):
    try:
        # 查找使用指定端口的进程 ID（PID）
        process = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True, text=True)
        output = process.stdout.strip()
        lines = output.split('\n')
        if len(lines) <= 1:
            print(f"没有进程使用端口 {port}。")
            return

        pid = lines[1].split()[1]
        
        # 终止使用指定 PID 的进程
        subprocess.run(['kill', pid])
        print(f"PID 为 {pid} 的进程已被终止。端口 {port} 已被释放。")

    except subprocess.CalledProcessError as e:
        print(f"错误：{e.stderr}")

if __name__ == '__main__':
    #port = input("请输入要释放的端口号：")
    release_port(5000)
