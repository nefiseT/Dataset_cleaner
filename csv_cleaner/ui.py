import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class CSVCleanerApp(tk.Tk):
    def __init__ (self, select_file_cb, process_cb):
        super().__init__()
        self.select_file_cb = select_file_cb
        self.process_cb = process_cb

        self.title(" csv column cleaning.exe")
        self.geometry("480x550")
        self.minsize(400, 450)

        self.file_path = ""
        self.checkboxes = {}
        self._build_ui()

    def _build_ui(self):
        file_frame = ttk.LabelFrame(self, text="select a file (csv format)", padding=10)
        file_frame.pack(fill="x", padx=15, pady=10)

        self.entry_file = ttk.Entry(file_frame, width=40)
        self.entry_file.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.entry_file.insert(0, "no file selected.....")
        self.entry_file.configure(state="readonly")

        btn_browse = ttk.Button(file_frame, text="browse", command=self._on_browse)
        btn_browse.pack(side="right")

        column_frame = ttk.LabelFrame(self, text= "found columns: ", padding=10)
        column_frame.pack(fill="both", expand= True, padx=15, pady=5)

        self.canvas = tk.Canvas(column_frame, borderwidth=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(column_frame, orient="vertical", command= self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>" , lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))


        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        actions_frame = ttk.Frame(self, padding=5)
        actions_frame.pack(fill="x", padx=15)
        
        self.btn_all = ttk.Button(actions_frame, text="select all", command= self._select_all, state="disabled")
        self.btn_all.pack(side="left", padx=2)

        self.btn_none = ttk.Button(actions_frame, text="unselect all", command=self._unselect_all, state="disabled")

        self.btn_none.pack(side="left", padx=2)

        self.btn_process = ttk.Button(self, text= "process dataset", command=self._on_process, state="disabled")

        self.btn_process.pack(fill="x", padx=15, pady=15)

        self.status_var = tk.StringVar(value=" ready")
        status_bar = ttk.Label(self, textvariable= self.status_var, relief="sunken", anchor="w", padding=5)
        status_bar.pack(side="bottom", fill="x")

    def _on_browse(self):
        file_selected = filedialog.askopenfilename(title="open csv file ", filetypes = [("csv files", "*.csv"), ("all files", "*.*")])

        if file_selected:
            self.file_path = file_selected
            self.entry_file.configure(state="normal")
            self.entry_file.delete(0, tk.END)
            self.entry_file.insert(0, file_selected)
            self.entry_file.configure(state="readonly")

            self.select_file_cb(file_selected)

    def populate_columns(self, headers):
        for chilld in self.scrollable_frame.winfo_children():
            child.destroy()
        self.checkboxes.clear()

        for header in headers:
            var = tk.BooleanVar(value=True)
            chk = ttk.Checkbutton(self.scrollable_frame, text=header, variable=var)
            chk.pack(anchor="w", pady=2)
            self.checkboxes[header] = var


        self.btn_all.configure(state="normal")
        self.btn_none.configure(state="normal")
        self.btn_process.configure(state="normal")
        self.set_status(f"Loaded{len(headers)} columns successfully")

    def _select_all(self):
        for var in self.checkboxes.values():
            var.set(True)

    def _unselect_all(self):
        for var in self.checkboxes.values():
            var.set(False)

    def _on_process(self):
        selected= [col for col, var in self.checkboxes.items() if var.get()]
        if not selected:
            messagebox.showwarning("warning", "select columnss to keep (min 1)")
            return
        
        self.set_status("processing...")
        self.btn_process.configure(state="disabled")
        self.update()

        self.process_cb(self.file_path, selected)
        self.btn_process.configure(state="normal")

    def set_status(self, text):
        self.status_var.set(f"status:{text}")
