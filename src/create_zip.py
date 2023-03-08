import os
import zipfile
    
folder_path = 'tmp/' # script will create zip for tmp folder content
zip_file_name = 'test.zip' # here you can also pass output directory name / zip file name

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(folder_path, zipf)
