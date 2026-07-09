# AI-Based Interactive Data Visualization Web Application

## Overview

This project is an **AI-powered web application** that automatically converts raw data from multiple file formats (Excel, Word, Text) into beautiful, interactive visualizations with multiple theme options and diverse chart types.

## Features

### 🎯 Core Capabilities
- **Multi-Format Data Extraction**: Supports Excel (.xlsx, .xls), Word (.docx), and Text files (.txt, .csv)
- **Automated Data Cleaning**: Handles missing values, data type detection, and preprocessing
- **Intelligent Chart Selection**: AI automatically recommends and generates appropriate chart types
- **Multiple Themes**: 6 professional themes (Plotly, Plotly Dark, Seaborn, GGPlot2, Simple White, Presentation)
- **Interactive Dashboards**: All charts are fully interactive with zoom, pan, and hover tooltips

### 📊 Chart Types
- **Bar Charts**: Compare categorical data
- **Pie Charts**: Show proportions and distributions
- **Line Charts**: Display trends over time
- **Histograms**: Show data distributions
- **Scatter Plots**: Visualize relationships between variables
- **Box Plots**: Display statistical distributions
- **Heatmaps**: Show correlations between numeric variables
- **Area Charts**: Display cumulative trends
- **Violin Plots**: Advanced distribution visualization

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Create Required Directories
The application will automatically create these directories on first run:
- `uploads/` - Temporary storage for uploaded files
- `output/` - Generated dashboard files
- `templates/` - HTML templates (already included)

## Usage

### Starting the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Using the Web Interface

1. **Upload Files**: 
   - Click the upload area or drag and drop files
   - Supports multiple files at once
   - Accepted formats: .xlsx, .xls, .docx, .doc, .txt, .csv

2. **Select Theme**:
   - Choose from 6 available themes
   - Each theme offers different color schemes and styling

3. **Generate Dashboard**:
   - Click "Generate Dashboard"
   - Wait for processing (typically 5-30 seconds)
   - Dashboard opens automatically in a new tab

## Project Structure

```
AI_DASHBOARD_PROJECT/
├── app.py                          # Main Flask application
├── modules/
│   ├── __init__.py                # Package initializer
│   ├── data_extraction.py         # File reading and parsing
│   ├── data_cleaning.py           # Data preprocessing
│   ├── eda.py                     # Exploratory data analysis
│   └── visualization.py           # Chart generation
├── templates/
│   └── index.html                 # Web interface
├── uploads/                        # Temporary file storage
├── output/                         # Generated dashboards
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Module Descriptions

### 1. `data_extraction.py`
- Extracts data from Excel, Word, and text files
- Handles multiple sheets in Excel files
- Parses tables from Word documents
- Detects structured data in text files
- Extracts numerical data from unstructured text

### 2. `data_cleaning.py`
- Automatic data type detection
- Missing value imputation
- Duplicate removal
- Data normalization
- Column type identification

### 3. `eda.py`
- Statistical analysis
- Data profiling
- Chart type recommendations
- Correlation analysis
- Distribution analysis

### 4. `visualization.py`
- Dynamic chart generation
- Theme application
- Interactive plot creation
- HTML dashboard generation
- Responsive layout design

## API Endpoints

### `GET /`
Returns the main web interface

### `POST /upload`
Accepts file uploads and generates dashboard

**Parameters**:
- `files`: Multiple file uploads (multipart/form-data)
- `theme`: Selected theme name (string)

**Returns**:
```json
{
    "success": true,
    "dashboard_url": "/view_dashboard/dashboard_plotly.html",
    "eda_summary": { ... }
}
```

### `GET /view_dashboard/<filename>`
Serves the generated dashboard HTML file

### `GET /themes`
Returns list of available themes

## Themes

1. **Plotly Default**: Clean, modern default theme
2. **Plotly Dark**: Dark mode for presentations
3. **Seaborn**: Statistical visualization style
4. **GGPlot2**: R-inspired elegant theme
5. **Simple White**: Minimalist white background
6. **Presentation**: Bold colors for presentations

## Data Requirements

### Excel Files
- Can contain multiple sheets
- First row typically treated as headers
- Supports numeric, text, and date columns

### Word Files
- Extracts both text and tables
- Tables are converted to structured data
- Attempts to extract numerical patterns from text

### Text Files
- CSV files are parsed automatically
- Tab-separated files are detected
- Unstructured text is analyzed for patterns

## Advanced Features

### Automatic Chart Recommendations
The system analyzes your data and automatically selects appropriate charts:
- Categorical + Numeric → Bar/Box charts
- Single Categorical → Pie charts
- Time Series → Line/Area charts
- Numeric Only → Histograms/Scatter plots
- Multiple Numerics → Correlation heatmap

### Data Cleaning Pipeline
1. **Type Detection**: Automatically identifies numeric, categorical, and datetime columns
2. **Missing Value Handling**: Fills missing data with appropriate strategies
3. **Outlier Management**: Identifies potential outliers
4. **Normalization**: Prepares data for visualization

## Troubleshooting

### Issue: No charts generated
- **Solution**: Ensure your files contain structured data with clear columns
- Check that files are not corrupted
- Verify file formats are supported

### Issue: Application won't start
- **Solution**: Ensure all dependencies are installed
- Check Python version (3.8+)
- Verify port 5000 is available

### Issue: Charts not displaying
- **Solution**: Check browser console for JavaScript errors
- Ensure internet connection (Plotly CDN required)
- Try a different theme

## Performance Tips

1. **File Size**: Keep individual files under 50MB
2. **Data Points**: Optimal performance with <100,000 rows
3. **Multiple Files**: Process similar data types together
4. **Themes**: Dark themes may perform better on some systems

## Future Enhancements

- [ ] Export dashboards as PDF
- [ ] Custom chart configuration
- [ ] Database integration
- [ ] Real-time data streaming
- [ ] Machine learning predictions
- [ ] Advanced filtering options
- [ ] User authentication
- [ ] Dashboard sharing capabilities

## Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Visualization**: Plotly.js
- **Data Processing**: Pandas, NumPy
- **Document Parsing**: python-docx, openpyxl

## Contributing

This is an academic project. For improvements or bug reports, please document them in your project report.

## License

Educational use only. Part of B.Sc. Artificial Intelligence & Data Science program.

## Author

**VALTINA A**  
B.Sc. Artificial Intelligence & Data Science  
3rd Year, Semester 6  
2023 Batch  
December 29, 2025

## Acknowledgments

- Plotly for interactive visualization library
- Flask for web framework
- Pandas for data manipulation
- Python community for excellent documentation
