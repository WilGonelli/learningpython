import os
from pathlib import Path

def list_files(dir):
    files = []
    for entry in os.scandir(f'{dir}/files'):
            files.append(entry.name)
    return files

def organize_files(dir):
    
    files_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'docs': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'audio': ['.mp3', '.wav', '.aac'],
        'movie': ['.mp4', '.mov', '.avi'],
        'compacts': ['.zip', '.rar', '.tar', '.gz']
    }
    
    files = list_files(dir)
    
    for file in files:
        [_name, type] = os.path.splitext(file)
        if type:    
            for category, ext in files_types.items():
                if type.lower() in ext:
                    target_dir = os.path.join(dir,'organized',category)
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                    source_path = os.path.join(dir, 'files', file)
                    target_path = os.path.join(target_dir, file)
                    print(f'Moving {source_path} to {target_path}')
                    os.rename(source_path, target_path)
 

if __name__ == "__main__":
    target_directory = Path(".")
    organize_files(target_directory)
    
    