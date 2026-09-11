# Student Performance Analytics & AI-Driven Insights

## Project Objective

The main goal of this project is to analyze student study habits, attendance, and lifestyle factors to discover what drives academic success. It also includes an interactive Streamlit web dashboard to showcase data visualizations and metrics clearly.

## Dataset Description

The project utilizes `StudentPerformanceFactors.csv`, which contains comprehensive records of student metrics including `Hours_Studied`, `Attendance`, `Parental_Involvement`, `Previous_Scores`, `Tutoring_Sessions`, and final `Exam_Score`.

## Dataset Source

Sourced from a public data repository containing student lifestyle and academic records.

## Technologies Used

* **Python** (Core programming language)
* **Streamlit** (For the interactive web application dashboard)
* **Jupyter Notebook** (For exploratory data analysis and research)
* **Git & GitHub** (Version control and code hosting)

## Libraries Used

* `pandas` & `numpy` (Data manipulation and processing)
* `matplotlib` & `seaborn` (Data visualization and plotting)
* `streamlit` (Dashboard user interface)

## Project Workflow

1. **Data Loading:** Imported the CSV dataset using Python's Pandas library.
2. **Data Cleaning:** Checked for missing values, duplicates, and data consistency.
3. **Exploratory Data Analysis (EDA):** Analyzed feature distributions, correlations, and performance trends.
4. **Statistical Analysis:** Calculated mean, standard deviation, and key descriptive statistics.
5. **Visualizations:** Generated 10+ distinct plots (scatter plots, heatmaps, box plots) saved in the `images/` directory.
6. **Web Dashboard:** Developed a responsive Streamlit app (`app/app.py`) for live interactive data filtering and visualization.

## Major Findings

* **Attendance Impact:** Class attendance shows the strongest positive correlation with final exam grades.
* **Study Hours:** Consistent study hours significantly boost final scores.
* **Lifestyle Factors:** Auxiliary variables like sleep and physical activity show minimal direct impact on grades compared to attendance and active study time.

## How to Run the Project

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/Task_01_AI_ML.git
cd Task_01_AI_ML

```


2. **Install required libraries:**
```bash
pip install streamlit pandas matplotlib seaborn numpy

```


3. **Run the Streamlit Dashboard:**
```bash
python -m streamlit run app/app.py

```



## Author Name

Muhammad Hamza Waseem
