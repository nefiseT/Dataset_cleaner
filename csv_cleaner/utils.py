import os

def get_filepath(orginal_path):
    directory, filename = os.path.split(orginal_path)
    name, ext = os.path.splitext(filename)

    base_new_name = f"{name}_processed"
    new_filename = f"{base_new_name}{ext}"
    candidate_path = os.path.join(directory, new_filename)
    
    counter = 2
    while os.path.exists(candidate_path):
        new_filename = f"{base_new_name}_{counter}{ext}"
        candidate_path = os.path.join(directory, new_filename)
        counter +=1

    return candidate_path