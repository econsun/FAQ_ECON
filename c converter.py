import os
import re

source_folder_pathc = r'C:\Users\29848\OneDrive\Obsidian\问答精选\c 题库（伸长版）'
target_folder_pathc = r'C:\Users\29848\OneDrive\Obsidian\问答精选\c 题库（缩短版）'

if not os.path.exists(target_folder_pathc):
    os.mkdir(target_folder_pathc)

file_namesc = os.listdir(source_folder_pathc)

# 遍历每个文件名
for file_namec in file_namesc:
    source_file_pathc = os.path.join(source_folder_pathc, file_namec)
    target_file_pathc = os.path.join(target_folder_pathc, file_namec)

    if file_namec.endswith('.md'):
        with open(source_file_pathc, 'r', encoding='utf-8') as file:
            file_contentc = file.read()

        modified_contentc = re.sub(r'\（伸长版\）', r'（缩短版）', file_contentc)

        with open(target_file_pathc, 'w', encoding='utf-8') as file:
            file.write(modified_contentc)