# Medical Insurance

Health insurance costs have risen dramatically over the past decade in response to the rising cost of health care services and are determined by a multitude of factors. Let's look at the cost of healthcare for a sample of the population given age, sex, bmi, number of children, smoking habits, and region.

The purpose of this project is to determine the contributing factors and predict health insurance cost by performing exploratory data analysis and predictive modeling on the Health Insurance dataset. This project makes use of Numpy, Pandas, Sci-kit learn, and Data Visualization libraries.


## DATA DESCRIPTION
1. age: age of primary beneficiary
2. sex: insurance contractor gender, female, male
3. bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
4. children: Number of children covered by health insurance / Number of dependents
5. smoker: Smoking
6. region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest
7. charges: Individual medical costs billed by health insurance

# CONCLUSION
Based on the predictive modeling, Linear Regression algorithm has the best score compared to the others, with MAE Score 4305.20, RMSE Score 6209.88, & R2 Score 0.77.

Therefore, Linear Regression algorithm is the best fitted model based on the training and testing accuracy


# How to excecute Medical Insurance Project
```python
python app.py
```
