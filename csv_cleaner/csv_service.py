import csv

def read_csv_headers(file_path):
    with open(file_path, mode='r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        if not headers:
            raise ValueError("csv file empty or no column.")
        return [h.strip() if h else "[empty header]" for h in headers]

def process_csv_file(input_path, output_path, selected_columns):
    with open(input_path, mode='r', encoding='utf-8-sig', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)

        header_map = [h.strip() if h else "[Empty Header]" for h in headers]
        indices_to_keep = [header_map.index(col) for col in selected_columns if col in header_map]
        
        if not indices_to_keep:
            raise ValueError("nO matching columns found to processs")
        
        with open(output_path, mode='w', encoding='utf-8-sig', newline='') as outfile:
            writer = csv.writer(outfile)

            writer.writerow([headers[i] for i in indices_to_keep])

            for row in reader:
                if row:
                    writer.writerow([row[i] for i in indices_to_keep])