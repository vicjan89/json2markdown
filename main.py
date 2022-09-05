import json
import os


path = r'C:\Users\Viktar\Downloads\takeout-20220903T151814Z-001\Takeout\Google Keep'
for filename in os.listdir(path):
    if filename[-4:] == 'json':
        with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
            note = json.load(f)
            md_out = '#' + note.get('title', False) + '\n'
            textContent = note.get('textContent', False)
            if textContent:
                md_out += textContent + '\n'
            labels = note.get('labels', False)
            if labels:
                md_out += 'tags: '
                for label in labels:
                    md_out += '#' + label['name'] + ' '
                md_out += '\n'
            attachments = note.get('attachments', False)
            if attachments:
                for attachment in attachments:
                    md_out += '![](' + attachment['filePath'].replace('jpeg', 'jpg') + ')\n'
        with open(os.path.join(path, filename.replace('json', 'md')), 'w', encoding='utf-8') as f:
            f.write(md_out)

