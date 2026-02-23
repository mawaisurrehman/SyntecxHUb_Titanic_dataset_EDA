# Titanic Dataset - Exploratory Data Analysis

An exploratory data analysis project on the famous Titanic dataset to uncover insights about passenger survival patterns.

## Overview

This project performs comprehensive exploratory data analysis on the Titanic dataset, exploring various factors that influenced passenger survival during the tragic sinking of the RMS Titanic.

## Features

The analysis includes:

- **Data Loading & Exploration**: Load and examine the dataset structure
- **Missing Values Analysis**: Visualize missing data patterns using heatmaps
- **Survival Rate Analysis**: Overall survival statistics
- **Gender Analysis**: Survival rates by gender
- **Passenger Class Analysis**: Survival rates by passenger class (1st, 2nd, 3rd)
- **Age Group Analysis**: Survival patterns across different age groups
- **Combined Analysis**: Survival by class and gender combined
- **Visual Insights**: Various visualizations including bar plots, violin plots, and boxplots

## Key Insights

1. Females have a much higher survival rate than males
2. First-class passengers survived more than second and third class
3. Children show relatively higher survival chances
4. Cabin column has many missing values and may not be useful directly
5. Passenger class strongly influences survival probability

## Installation

1. Clone the repository:
```
bash
git clone <repository-url>
```

2. Navigate to the project directory:
```
bash
cd SyntecxHUb_Titanic_dataset_EDA
```

3. Install the required dependencies:
```
bash
pip install -r requirements.txt
```

## Usage

Run the main analysis script:
```
bash
python main.py
```

The script will display various statistics and generate visualizations in a window format.

## Technologies Used

- **Python**: Programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization

## Dataset

The project uses the Titanic training dataset (`train.csv`) which contains information about the passengers including:
- PassengerId
- Survived (target variable)
- Pclass (passenger class)
- Name
- Sex
- Age
- SibSp (siblings/spouses aboard)
- Parch (parents/children aboard)
- Ticket number
- Fare
- Cabin
- Embarked (port of embarkation)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
