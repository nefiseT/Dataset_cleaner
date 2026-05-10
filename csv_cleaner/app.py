import os
from ui import CSVCleanerApp
from csv_service import read_csv_headers, process_csv_file
from utils import get_filepath
from tkinter import messagebox

class AppController:
    def __init__(self):
        self.view = CSVCleanerApp(select_file_cb = self.handle_file_selection, process_cb = self.handle_processing)

    def handle_file_selection(self, file_path):
        try:
            headers = read_csv_headers(file_path)

            self.view.populate_columns(headers)
        except Exception as e:
            self.view.set_status(f"Error:{str(e)}")
            messagebox.showerror("error reading file", f"couldnt read CSV File. \n Details: {e}")

    def handle_processing(self, input_path, selected_columns):
        try:
            output_path = get_filepath(input_path)
            process_csv_file(input_path, output_path, selected_columns)

            filename = os.path.basename(output_path)
            self.view.set_status("saved sucessfully.")

            messagebox.showinfo("successs", f"CSV processed succesfully!\n\nSaved as:\n{filename}")

        except Exception as e:
            self.view.set_status("erorr during process")
            messagebox.showerror("processing error", f"an error occured:\n{e}")
    
    def run(self):
        self.view.mainloop()

if __name__ == "__main__":

    app = AppController()
    app.run()
