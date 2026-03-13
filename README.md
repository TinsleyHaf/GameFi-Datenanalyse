# GameFi-Datenanalyse

## Project Overview
This repository is dedicated to analyzing data related to the gaming platform Axie Infinity. The main focus is to utilize various data analysis and machine learning techniques to extract insights and build predictive models based on user interaction and in-game economics.

## Objectives for Axie Infinity Analysis
1. Understand user behaviors and in-game trends.
2. Predict market trends and asset valuation.
3. Establish relationships between different game variables and user engagement.

## Required Technologies
- **Python**: A programming language for data analysis and machine learning.
- **Pandas**: Library for data manipulation and analysis.
- **NumPy**: Library for numerical computations.
- **Scikit-Learn**: Tool for machine learning in Python.
- **PyTorch**: Framework for building machine learning models.
- **Plotly**: Library for interactive visualizations.
- **Matplotlib**: Library for static visualizations.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/TinsleyHaf/GameFi-Datenanalyse.git
   cd GameFi-Datenanalyse
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure
```
GameFi-Datenanalyse/
├── data/
│   └── ...                 # Directory for datasets
├── notebooks/
│   └── ...                 # Jupyter notebooks for analysis
├── src/
│   └── ...                 # Source code for models and analysis
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```  

## Features
- Data extraction from The Graph and OpenSea.
- Data cleaning and preprocessing.
- Exploratory data analysis.
- Model training and evaluation.
- Interactive visualizations for insights.

## API Keys Setup for The Graph and OpenSea
1. Sign up for access to The Graph and OpenSea.
2. Obtain your API keys from their respective developer platforms.
3. Store your API keys in a `.env` file as follows:
   ```
   THE_GRAPH_API_KEY=your_the_graph_api_key
   OPENSEA_API_KEY=your_opensea_api_key
   ```
4. Load these keys in your code using environment variable libraries like `dotenv`.

## Usage Examples
- To run data analysis scripts:
  ```bash
  python src/data_analysis.py
  ```
- To start the Jupyter notebook:
  ```bash
  jupyter notebook
  ```

---
This documentation will be updated as the project progresses and more features are implemented.