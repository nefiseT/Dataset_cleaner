import csv
import json
import os

def read_headers(file_path):
    """Detects file type and extracts headers/keys safely."""
    # os.path.splitext split "/path/to/file.csv" into ("/path/to/file", ".csv")
    _, file_extension = os.path.splitext(file_path.lower())
    
    if file_extension == '.csv':
        with open(file_path, mode='r', encoding='utf-8-sig', newline='') as f:
            reader = csv.reader(f)
            headers = next(reader)
            if not headers:
                raise ValueError("The CSV file is empty.")
            return [h.strip() if h else "[Empty Header]" for h in headers]
            
    elif file_extension == '.json':
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list) or len(data) == 0:
                raise ValueError("JSON must be a non-empty list of objects.")
            if not isinstance(data[0], dict):
                raise ValueError("JSON array must contain key-value objects.")
            return list(data[0].keys())
            
    else:
        raise ValueError(f"Unsupported file format '{file_extension}'. Please use CSV or JSON.")


def process_file(input_path, output_path, selected_columns):
    """Processes either CSV or JSON based on file extension."""
    _, file_extension = os.path.splitext(input_path.lower())
    
    if file_extension == '.csv':
        with open(input_path, mode='r', encoding='utf-8-sig', newline='') as infile:
            reader = csv.reader(infile)
            headers = next(reader)
            header_map = [h.strip() if h else "[Empty Header]" for h in headers]
            indices_to_keep = [header_map.index(col) for col in selected_columns if col in header_map]
            
            with open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([headers[i] for i in indices_to_keep])
                for row in reader:
                    if row:
                        writer.writerow([row[i] for i in indices_to_keep])
                        
    elif file_extension == '.json':
        with open(input_path, mode='r', encoding='utf-8') as infile:
            data = json.load(infile)
            
        processed_data = []
        for item in data:
            if isinstance(item, dict):
                filtered_item = {k: item[k] for k in selected_columns if k in item}
                processed_data.append(filtered_item)
                
        with open(output_path, mode='w', encoding='utf-8') as outfile:
            json.dump(processed_data, outfile, indent=4)
