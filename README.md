# CSV Combiner - Offline Tool

A static HTML tool that combines multiple CSV files offline in your browser. No data leaves your computer.

## Features

- **100% Offline**: Works without internet connection
- **Secure**: All processing happens locally in your browser
- **Multiple CSV Import**: Drag & drop or browse for CSV files
- **Header Validation**: Ensures all files have identical headers
- **Duplicate Removal**: Remove duplicate rows (all columns must match)
- **Unique Column Enforcement**: Select specific columns where values must be unique
- **Combined Preview**: View combined data before export
- **Filename Column**: Automatically adds source filename as first column
- **Export**: Download combined CSV with timestamp
- **Responsive Design**: Works on desktop and mobile devices

## Requirements

No installation required! Just a modern web browser.

## Usage

1. **Open the tool**: Double-click `index.html` or run the local server
2. **Select CSV files**: Drag & drop or click to browse
3. **Combine**: Click "Combine Files" to merge all CSV data
4. **Process**: Apply filters like duplicate removal or unique column constraints
5. **Preview**: Check the combined data in the table (first 100 rows shown)
6. **Export**: Download the combined CSV with filename column added

## File Structure

```
combine_csv/
├── index.html          # Main HTML file
├── style.css          # Styles
├── icons.css          # Unicode icons for offline use
├── script.js          # Main application logic
├── serve.py           # Python HTTP server (optional)
├── sample1.csv        # Example CSV file
├── sample2.csv        # Example CSV file
└── README.md          # This file
```

## Running Locally

### Option 1: Direct File Access
Simply open `index.html` in your web browser.

### Option 2: Local HTTP Server (Recommended)
Run the included Python server:

```bash
python3 serve.py
```

Then open http://localhost:8080 in your browser.

### Option 3: Any HTTP Server
You can use any HTTP server like:
- `npx serve .` (Node.js)
- `python3 -m http.server 8000`
- `php -S localhost:8000`

## CSV Format Requirements

1. **First line must be headers** (column names)
2. **All files must have identical headers** (same columns in same order)
3. **Supported separators**: Comma (`,`)
4. **Quoted fields**: Fields containing commas, quotes, or newlines should be quoted with `"`
5. **Encoding**: UTF-8 recommended

## Processing Features

### Duplicate Row Removal
- **What it does**: Removes rows where all column values are identical
- **How to use**: Check "Remove duplicate rows (all columns must match)"
- **Result**: Only unique rows remain (first occurrence is kept)

### Unique Column Constraints
- **What it does**: Ensures selected columns have unique values across all rows
- **How to use**: 
  1. Check "Ensure unique values in selected columns"
  2. Select the columns that should be unique
- **Result**: Rows with duplicate values in selected columns are removed (first occurrence is kept)
- **Example**: If "Email" column is selected as unique, only rows with unique email addresses remain

### Processing Workflow
1. Combine files to create initial dataset
2. Apply processing filters as needed
3. View processing statistics showing rows removed
4. Reset to original data if needed
5. Export processed data

## How It Works

1. **File Reading**: Uses FileReader API to read CSV files locally
2. **CSV Parsing**: Custom parser handles quoted fields and commas
3. **Header Validation**: Compares headers across all files
4. **Data Combination**: Appends all rows with filename as first column
5. **Processing**: Applies duplicate removal and unique column filters
6. **Export**: Generates CSV content and triggers download

## Browser Compatibility

Works in all modern browsers that support:
- FileReader API
- Drag & Drop API
- Blob API for file download

Tested on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Privacy & Security

- **No server communication**: All processing happens in your browser
- **No data upload**: Files never leave your computer
- **No tracking**: No analytics, cookies, or external dependencies
- **No installation**: Zero dependencies or installation required

## Sample CSV Files

Two sample files are included:
- `sample1.csv`: 4 rows with Name, Age, City
- `sample2.csv`: 4 rows with Name, Age, City

You can use these to test the tool and its processing features.

## Troubleshooting

### "Files have different headers" error
Ensure all CSV files have identical first rows (same column names in same order).

### "Error parsing file" message
Check CSV format: first line headers, consistent columns, proper quoting.

### Drag & drop not working
Try clicking the upload area or using the file browser dialog.

### Export not working
Make sure you've combined files first (click "Combine Files").

### Processing not applying
Ensure you've selected processing options and clicked "Apply Processing".

### Columns not showing in unique columns selector
Combine files first to load headers, then enable unique columns option.

## License

This tool is provided as-is for personal and commercial use.

## Contributing

Feel free to modify and adapt for your needs. The code is simple and well-commented.