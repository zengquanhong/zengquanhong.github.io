#!/bin/bash

# 获取当前用户名
echo "当前用户: $(whoami)" >> system_report.txt

# 获取当前系统时间
echo "当前时间: $(date)" >> system_report.txt

# 获取系统 CPU 负载情况
echo "CPU 负载情况: $(uptime)" >> system_report.txt

# 获取磁盘使用情况
echo "磁盘使用情况: " >> system_report.txt
df -h >> system_report.txt

# 获取内存使用情况
echo "内存使用情况: " >> system_report.txt
free -m >> system_report.txt

echo "系统信息已保存到 system_report.txt"
