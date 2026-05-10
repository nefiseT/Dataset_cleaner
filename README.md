##A SIMPLE APP TO CLEAN OUT UNWANTED COLUMNS IN A CSV FILE##

A small Tkinter desktop app that lets you keep only the columns you want in a CSV file.

## What it does
- Opens a `.csv` file
- Reads the header row
- Shows all column names as checkboxes
- Writes a new CSV containing only the selected columns

## Why this exists
Instead of editing the CSV manually (or building a script every time), you can quickly select the columns to keep and export a cleaned file.

## What works
- Loads headers from the first row (whitespace is stripped)
- Checkboxes for every detected column
- “Select all” / “Unselect all”
- Output file is saved next to the input with a `_processed` suffix

## How to run
1. Make sure you have Python installed.
2. Run:
   ```bash
   python app.py
   ```

3. or dist\ app.exe

Using App: In the app:
   - Click **browse** and choose a CSV
   - Select the columns to keep
   - Click **process dataset**

## Output naming
If your input file is `data.csv`, the app writes:
- `data_processed.csv`
- If that name already exists, it creates `data_processed_2.csv`, `data_processed_3.csv`, etc.

