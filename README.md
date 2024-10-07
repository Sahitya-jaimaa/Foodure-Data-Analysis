# Foodure Data Analysis Dashboard

## Overview
The **Foodure Data Analysis Dashboard** is a Streamlit application that provides insights into restaurant data, including ratings, votes, and online order availability. This interactive dashboard allows users to visualize and analyze food-related data efficiently.

## Features
- **Dynamic Filtering**: Users can filter data based on restaurant type and online order availability.
- **Multiple Visualizations**: Choose from various plot types, including:
  - Countplot of Restaurant Types
  - Votes vs. Restaurant Type
  - Online Order Availability Count
  - Ratings Distribution
  - Boxplot of Ratings by Online Order
  - Heatmap of Restaurant Types vs. Online Order
  - Interactive Scatter Plot
  - Correlation Heatmap
- **Data Summary**: View the number of rows in the filtered dataset.

## Installation
To run this application, ensure you have Python installed on your system. Then, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
2. **Install the required packages**: You can install the necessary libraries using pip:
   pip install pandas numpy matplotlib seaborn streamlit plotly
   Download the dataset: Ensure that the dataset file Foodure data .csv is in the same directory as the script.

3. **Running the Application**
    To run the Streamlit application, use the following command in your terminal:

    streamlit run demo.py
   

    Usage
    Open the application in your web browser (usually it opens automatically at http://localhost:8501).
    Use the sidebar to filter data by restaurant type and online order availability.
    Select different plot types to visualize the data.
 ## License
    This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
    Streamlit for creating a powerful data app framework.
    Pandas for data manipulation.
    Seaborn for beautiful statistical graphics.
    Plotly for interactive plots.
