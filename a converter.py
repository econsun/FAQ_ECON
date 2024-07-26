import os
import re

source_folder_patha = r'C:\Users\29848\OneDrive\Obsidian\问答精选\a 知识（缩短版）'
target_folder_patha = r'C:\Users\29848\OneDrive\Obsidian\问答精选\a 知识（伸长版）'

if not os.path.exists(target_folder_patha):
    os.mkdir(target_folder_patha)

file_namesa = os.listdir(source_folder_patha)

for file_namea in file_namesa:
    source_file_patha = os.path.join(source_folder_patha, file_namea)
    target_file_patha = os.path.join(target_folder_patha, file_namea)

    if file_namea.endswith('.md'):
        with open(source_file_patha, 'r', encoding='utf-8') as file:
            file_contenta = file.read()

        modified_contenta = re.sub(r'\（缩短版\）', r'（伸长版）', file_contenta)

        with open(target_file_patha, 'w', encoding='utf-8') as file:
            file.write(modified_contenta)