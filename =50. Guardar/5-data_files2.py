from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob('**/*'):
    if path.is_file():
        stats = path.stat()
        # print(stats.st_ctime)
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime('%Y-%M-%d_%H_%M_%S')
        #print(date_created_str)
        new_filapath = f'{date_created_str}-{path.name}'
        path.rename(new_filapath)