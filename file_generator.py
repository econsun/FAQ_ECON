# 本脚本用于生成 c 题库（伸长版）中的文件

import os

start = 82
end = 90

save_dir = r'C:\Users\29848\OneDrive\Obsidian\问答精选\c 题库（伸长版）'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

base_content = '''
联系方式：<a href="https://qm.qq.com/q/iA1sKuakak">2629223739 (QQ)</a> <a href="mailto:econsunrq@outlook.com">econsunrq@outlook.com (邮箱)</a>

[[c 题库（伸长版）/Problem {next}|下一题]]，[[c 题库（伸长版）/Problem {prev}|上一题]]

[[0 主页|回到主页]]，[[4 操作流水|操作流水]]

![[1 汇总问题（伸长版）#^{current}]]
'''

for i in range(start, end + 1):
    current = f'{i:04d}'
    next_problem = f'{i + 1:04d}' if i < end else f'{start:04d}'  
    prev_problem = f'{i - 1:04d}' if i > start else f'{end:04d}'  
    
    content = base_content.format(current=current, next=next_problem, prev=prev_problem)
    
    file_name = os.path.join(save_dir, f'Problem {current}.md')
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content.strip())

print("Markdown files have been created！")
