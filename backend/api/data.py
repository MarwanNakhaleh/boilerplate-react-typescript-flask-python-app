import json
 
def get_data(file_path):
    f = open(file_path)
    data = json.load(f)
    f.close()
    return data
