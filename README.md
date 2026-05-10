##A SIMPLE APP TO CLEAN OUT UNWANTED COLUMNS IN A CSV FILE##

A small Tkinter desktop app that lets you keep only the columns you want in a CSV file.

## What it does
- Opens a `.csv` file
- Reads the header row (1st column)
- Shows all column names as checkboxes (select the ones u want in your new file)
- Writes a new CSV containing only the selected columns

## What works
- Loads headers from the first row (whitespace is stripped)
- Checkboxes for every detected column
- “Select all” / “Unselect all”
- Output file is saved next to the input with a `_processed` suffix

## How to run
1. Make sure you have Python installed. (tkinter , os)
2. Run:
   ```bash
   python app.py
   ```

3. or dist\ app.exe (to build .exe file pyinstaller --noconsole --onefile --icon=icon.ico app.py , if you dont have an icon, win will give automatically)

Using App:
   - Click **browse** and choose a CSV
   - Select the columns to keep
   - Click **process dataset**

## Output naming
If your input file is `data.csv`, the app writes:
- `data_processed.csv`
- If that name already exists, it creates `data_processed_2.csv`, `data_processed_3.csv`, etc.

