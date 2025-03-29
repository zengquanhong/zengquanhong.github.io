#!/bin/bash

# 从 user_list.txt 文件中读取每个用户名
while IFS= read -r username
do
    # 检查用户是否已经存在
    if id "$username" &>/dev/null; then
        echo "用户 $username 已存在，跳过创建。"
    else
        # 创建新用户
        useradd "$username"
        if [ $? -eq 0 ]; then
            echo "用户 $username 创建成功！"
        else
            echo "创建用户 $username 失败！"
        fi
    fi
done < user_list.txt
