'''
Declaration of views and routes.
'''
from flask import render_template, request, redirect
from pathlib import Path
from app import app
from datetime import datetime
import os
import dotenv

config = {
    "bg_color": "#dcdcdc"
}

def parse_tags(entry):
    file_path = Path(f'{entry}/tags.txt')
    with open(file_path) as f:
        return list(f)

def get_description(entry):
    file_path = Path(f'{entry}/description.txt')
    with open(file_path) as f:
        return f.read()

def get_file_sources(entry):
    file_path = Path(f'{entry}/files')
    _, _, files = next(os.walk(file_path))
    return files
        

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    base_dir = dotenv.get_key(".env", "DIR")
    base_dir = Path(f'{base_dir}/soda_files/data_sources')
    _, dirnames, _ = next(os.walk(base_dir))

    recent = []
    counter = 0

    for entry in dirnames:
        for path, dirs, files in os.walk(base_dir):
            if path.endswith(entry):
                tags = parse_tags(path)
                description = get_description(path)
                timestamp = datetime.fromtimestamp(os.path.getmtime(path))
                last_modified = timestamp.strftime("%m/%d/%y - %H:%M")
                recent.append({
                    "name": entry,
                    "tags": tags,
                    "description": description,
                    "timestamp": timestamp,
                    "last_updated": last_modified
                })
                counter += 1
            if counter == 3:
                break

    recent.sort(key=lambda entry : entry["timestamp"], reverse=True)

    return render_template('index.html', recent=recent, config=config)

@app.route('/data_source')
def data_source():
    args = request.args
    if(not bool(args)):
        return redirect('/')

    name = args['q']
    
    base_dir = dotenv.get_key(".env", "DIR")
    base_dir = Path(f'{base_dir}/soda_files/data_sources')
    _, dirnames, _ = next(os.walk(base_dir))

    if name not in dirnames:
        return "404"
   
    for path, _, _ in os.walk(base_dir):
        if path.endswith(name):
            tags = parse_tags(path)
            description = get_description(path)
            files_list = get_file_sources(path)
            # files_processed = [filename.split('.') for filename in files_list]
            timestamp = datetime.fromtimestamp(os.path.getmtime(path))
            last_modified = timestamp.strftime("%m/%d/%y - %H:%M")
            data = {
                "name": name,
                "tags": tags,
                "description": description,
                "files": files_list,
                "timestamp": timestamp,
                "last_updated": last_modified,
            }

    print(data['files'])
    return render_template('data_source.html', data=data, config=config)