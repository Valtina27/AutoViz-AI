# AutoViz AI

AI-Powered Multi-Format Data Analysis and Interactive Dashboard

## Overview

AutoViz AI is an AI-powered Streamlit web application developed as a final-year capstone project for the Bachelor of Science in Artificial Intelligence and Data Science.

The application enables users to upload multiple file formats, including Excel, CSV, Word, and Text files, and automatically extracts, cleans, analyzes, and visualizes the data. It generates interactive dashboards, performs Exploratory Data Analysis (EDA), and creates downloadable PDF reports, allowing users to gain meaningful insights with minimal manual effort.

The primary objective of this project is to simplify the data analysis process by providing an intelligent and user-friendly platform for data exploration and visualization.

---

## Key Features

- Supports Excel, CSV, Word, and Text file formats
- Automated data extraction and preprocessing
- Intelligent data cleaning
- Exploratory Data Analysis (EDA)
- Interactive dashboards using Plotly
- Multiple visualization techniques
- PDF report generation
- Light and Dark dashboard themes
- Responsive Streamlit user interface

---

## Technologies Used

### Programming Language

- Python

### Framework

- Streamlit

### Libraries

- Pandas
- NumPy
- Plotly
- OpenPyXL
- python-docx
- FPDF

---

## Project Structure

```text
AutoViz-AI
│
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_DOCUMENTATION.md
├── QUICKSTART.md
│
├── modules
│   ├── data_extraction.py
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── visualization.py
│   └── pdf_report.py
│
├── assets
│   └── screenshots
│
├── uploads
├── output
└── sample_data
```

---

## Application Screenshots

### Home Page

![Home Page](assets/screenshots/home-page.jpeg)

### Dashboard

![Dashboard](assets/screenshots/dashboard-ch-1.jpeg)

### Interactive Visualizations

![Visualization](assets/screenshots/dashboard-ch-2.jpeg)

### Data Analysis

![Analysis](assets/screenshots/dashboard-ch-3.jpeg)

### Generated Report

![Report](assets/screenshots/dashboard-ch-4.jpeg)

---

## Installation

Clone the repository.

```bash
git clone https://github.com/Valtina27/AutoViz-AI.git
```

Navigate to the project directory.

```bash
cd AutoViz-AI
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

---

## Workflow

1. Upload one or more supported data files.
2. Extract and preprocess the data automatically.
3. Perform Exploratory Data Analysis.
4. Generate interactive visualizations.
5. Create dashboards and PDF reports.
6. Export insights for further analysis.

---

## Future Enhancements

- AI-powered analytical recommendations
- Machine learning model integration
- Cloud deployment
- Dashboard sharing
- User authentication
- Real-time data analytics

---

## Documentation

Detailed project documentation is available in the repository.

- PROJECT_DOCUMENTATION.md
- QUICKSTART.md

---

## Developer

Valtina A

Bachelor of Science in Artificial Intelligence and Data Science

Rathinam College of Liberal Arts and Science @ TIPS Global Institute

GitHub: https://github.com/Valtina27

LinkedIn: Add your LinkedIn profile URL

---

## License

This project is licensed under the MIT License.
