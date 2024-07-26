import os
import re

source_folder_pathb = r'C:\Users\29848\OneDrive\Obsidian\问答精选\b 月度（伸长版）'
target_folder_pathb = r'C:\Users\29848\OneDrive\Obsidian\问答精选\b 月度（缩短版）'

if not os.path.exists(target_folder_pathb):
    os.mkdir(target_folder_pathb)

file_namesb = os.listdir(source_folder_pathb)

for file_nameb in file_namesb:
    source_file_pathb = os.path.join(source_folder_pathb, file_nameb)
    target_file_pathb = os.path.join(target_folder_pathb, file_nameb)

    if file_nameb.endswith('.md'):
        with open(source_file_pathb, 'r', encoding='utf-8') as file:
            file_contentb = file.read()

        modified_contentb = re.sub(r'\（伸长版\）', r'（缩短版）', file_contentb)

        with open(target_file_pathb, 'w', encoding='utf-8') as file:
            file.write(modified_contentb)