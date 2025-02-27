# Australian Apparel Limited (AAL) - Q4 2020 Sales Analysis

## Project Overview
This project analyzes the Q4 2020 sales data of Australian Apparel Limited (AAL) to provide insights into state-wise and category-wise performance. The goal is to help the company make data-driven investment and marketing decisions.

## Features
- **Data Wrangling**: Cleaning, handling missing values, and normalizing sales data.
- **Data Analysis**: Performing statistical analysis on sales trends across different states and groups.
- **Data Visualization**: Creating visual reports using Seaborn and Matplotlib.
- **Report Generation**: Compiling findings into a Jupyter Notebook.

## Dataset
- **Source**: Provided CSV file containing sales data for Q4 2020.
- **Columns**: 
  - `State`: Australian state where sales occurred.
  - `Group`: Customer category (Kids, Women, Men, Seniors).
  - `Sales`: Revenue generated.
  - `Time`: Time of sale.
  - `Week`, `Month`, `Quarter`: Time-based sales segmentation.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/AAL-Sales-Analysis.git
   cd AAL-Sales-Analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run Jupyter Notebook:
   ```sh
   jupyter lab
   ```
4. Open `AAL_Sales_Analysis.ipynb` to explore the analysis.

## Usage
- Execute each cell in the Jupyter Notebook to perform data wrangling, analysis, and visualization.
- Review the graphs and insights generated to understand sales trends.

## Results & Insights
- **Top-performing state:** Victoria
- **Lowest-performing state:** Western Australia
- **Peak sales month:** December
- **Most profitable category:** Men's apparel
- **Least profitable category:** Seniors' apparel
- **Time-of-day insights:** Sales peak in the afternoon and early evening.

## Recommendations
- Implement targeted marketing in low-performing states.
- Introduce discounts and promotions for the seniors' category.
- Optimize sales strategies based on peak shopping hours.

## Technologies Used
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook
