# Quick Start Guide - AI Data Visualization Dashboard

## Step-by-Step Setup

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate Sample Data (Optional)
```bash
python generate_samples.py
```
This creates test files you can use to explore the application.

### 3. Test Your Setup
```bash
python test_setup.py
```
Verifies all packages and modules are correctly installed.

### 4. Start the Application
```bash
python app.py
```

### 5. Open Your Browser
Navigate to: `http://localhost:5000`

## Using the Application

### Upload Files
1. Click the upload area or drag files
2. Select multiple files: Excel, Word, Text, or CSV
3. Files are validated automatically

### Choose a Theme
Select one of 6 available themes:
- **Plotly Default**: Professional, modern look
- **Plotly Dark**: Dark mode, great for presentations
- **Seaborn**: Statistical analysis style
- **GGPlot2**: R-inspired elegant design
- **Simple White**: Clean, minimalist
- **Presentation**: Bold, high-contrast colors

### Generate Dashboard
1. Click "Generate Dashboard"
2. Wait 5-30 seconds for processing
3. Dashboard opens in new tab automatically
4. All charts are interactive (zoom, pan, hover)

## What Charts Will Be Generated?

The AI automatically analyzes your data and creates:

### For Categorical + Numeric Data
- Bar charts showing comparisons
- Box plots showing distributions
- Pie charts showing proportions

### For Time Series Data
- Line charts showing trends
- Area charts showing cumulative data

### For Numeric Data
- Histograms showing distributions
- Scatter plots showing relationships
- Correlation heatmaps

### Advanced Charts
- Violin plots for detailed distributions
- Sunburst charts for hierarchical data

## File Format Requirements

### Excel Files (.xlsx, .xls)
- Multiple sheets supported
- First row = column headers
- Mix of text and numbers OK

### Word Files (.docx)
- Extracts all tables automatically
- Analyzes text for numerical patterns
- Combines with other data sources

### Text/CSV Files (.txt, .csv)
- Comma or tab-separated
- Can include unstructured text
- Numerical patterns extracted automatically

## Tips for Best Results

1. **Clear Column Headers**: Use descriptive names
2. **Consistent Data**: Same format across all files
3. **Avoid Empty Cells**: Or they'll be filled automatically
4. **Use Multiple Files**: Combine different data sources
5. **Try Different Themes**: Each has unique advantages

## Troubleshooting

### No Charts Appear
- Check browser console (F12)
- Ensure data has clear columns
- Try a different theme

### Application Won't Start
- Verify Python 3.8+
- Check all dependencies installed
- Ensure port 5000 is free

### Upload Fails
- Check file size (max 50MB)
- Verify file format is supported
- Try one file at a time first

## Features Comparison

| Feature | Basic Excel | This App |
|---------|------------|----------|
| Multiple Files | ❌ | ✅ |
| Auto Chart Selection | ❌ | ✅ |
| Interactive Charts | ❌ | ✅ |
| Multiple Themes | ❌ | ✅ |
| Word/Text Support | ❌ | ✅ |
| AI Analysis | ❌ | ✅ |

## What Makes This Special?

1. **Multi-Format Support**: Combines Excel, Word, and Text files
2. **AI-Powered**: Automatically selects best chart types
3. **Professional Themes**: 6 polished visualization styles
4. **Interactive**: All charts support zoom, pan, hover
5. **Comprehensive**: 10+ different chart types
6. **Easy to Use**: No coding required

## Next Steps

After getting familiar with the basic features:

1. Try different file combinations
2. Experiment with all themes
3. Use sample data to understand patterns
4. Upload your own business data
5. Share dashboards with colleagues

## Support

For issues or questions:
- Check README.md for detailed documentation
- Review the troubleshooting section
- Verify all requirements are met

---

**Project**: AI-Based Interactive Data Visualization  
**Author**: VALTINA A  
**Course**: B.Sc. Artificial Intelligence & Data Science  
**Year**: 3rd Year, Semester 6 (2023 Batch)  
**Date**: December 29, 2025
