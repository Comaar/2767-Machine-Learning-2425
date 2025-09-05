# Assignment 1: TelCom Solutions Churn Crisis

## Context

TelCom Solutions, a leading telecom provider, is grappling with a significant customer churn crisis. Despite its reputation, rising churn rates and a recent major network outage have led to widespread dissatisfaction and customer exodus to competitors offering more reliable services and aggressive promotions. The COO notes severe revenue and reputation damage.

At a recent board meeting, the CEO expressed a "gut feeling" that 15% of churn customers originate from international plans. The VP of Marketing suspected higher churn among monthly contract customers, but admitted a lack of data for confirmation. The board demands immediate, data-driven insights to address this crisis.

## The Customer Retention Taskforce

You are a data scientist on the newly formed Customer Retention Taskforce. This cross-functional team is mandated to mitigate churn and stabilize customer retention using data-driven strategies. Operating under tight deadlines, your responsibilities include:

1.  **Data Analysis:** Conduct a thorough examination of customer data to identify churn patterns and trends, validating or disproving executive assumptions.
2.  **Predictive Modeling:** Develop machine learning models to predict high-risk churn customers, enabling proactive retention efforts.
3.  **Strategic Insights:** Deliver actionable recommendations to the executive team, forming the basis for new retention campaigns and operational adjustments.

Your work is critical for addressing the immediate crisis and positioning TelCom Solutions as a more customer-centric organization. You have access to detailed customer records covering demographics, service usage, and billing information.

## Instructions

1.  **Download the Dataset:** Use the Telecom Churn Dataset from [insert dataset link here, if available].
2.  **Complete All Tasks:** Follow the questions outlined below step-by-step.
3.  **Prepare Files for Submission:** Submit your work as a ZIP file named `StudentNumber_Churn_Assignment.zip`. This ZIP file should contain:
    *   A Jupyter Notebook file (`StudentNumber_Churn_Notebook.ipynb`).
    *   A trained model saved as a Pickle file (`StudentNumber_Model.pkl`).
4.  **Upload to Moodle:** Submit the ZIP file on Moodle under the appropriate assignment link before the deadline.

---

## Assignment Questions & Grading Breakdown

### Question 1 (4 points)

The CEO claims that 15% of customers churn are coming from international plan. Using the provided dataset, validate the CEO’s statement and extract additional insights. (In the submitted notebook you should clearly state all the steps done to answer the questions).

*   **Q1.1 – Is the CEO statement correct? [Yes, No] If not, what is the churn percentage? [Numeric]** (1 point)
*   **Q1.2 – Provide three insights you extracted from the EDA analysis [Free text + code]** (3 points)

### Question 2 (4 points)

The executive team needs a robust predictive solution to identify customers most at risk of churning. Machine learning models can provide the insights required for targeted retention strategies.

*   **Q2.1. Which kind of machine learning problem is Telecom facing? [Multiple choice: regression, classification, recommendation systems, foundational model]** (1 point)
*   **Q2.2. Train two models that are adequately suited to the problem. Justify why you chose those. [Free text + code]** (3 points)
    *   *In the code, document the hyperparameter tuning, train-test split, and all processing steps.*

### Question 3 (4 points)

To ensure the predictive models are reliable, the taskforce must evaluate their performance using appropriate metrics. This evaluation will determine which model is best suited for deployment.

*   **Q3.1. Which performance metric did you use to evaluate the performance? Why? [Free text + code]** (2 points)
*   **Q3.2. Which model provided the best results? [Free text]** (2 points)

### Question 4 (4 points)

The executive team has provided an external validation dataset with the same structure as the original data. To test the best model, the team must ensure it works seamlessly on new data. The model should predict churn using binary outputs: `0` (No Churn) and `1` (Churn).

*   Save the best-performing model as a Pickle file (`Firstname_Lastname_Model.pkl`).
*   Write code to reload the saved model and test it on the external validation dataset.
*   Ensure the model outputs predictions in the required format.

**How This Question Will Be Evaluated:**

1.  **Top 25% Models:** The models that perform the best on the external validation dataset will receive full marks for this task. Performance will be ranked based on accuracy.
2.  **Next 25% Models:** Students whose models perform in the following 25% will receive 3 points, and so on.
3.  **Non-Functional Models:** If your model fails to load, run, or provide predictions in the required format (0 for No Churn, 1 for Churn), you will receive zero marks for this task. Make sure your `.pkl` file and code are functional, tested, and well-documented.

*You can find a test set in the assignment.*

### Question 5 (4 points)

The executive team requires actionable insights to guide the strategy to address customer churn effectively. Your analysis will directly inform their decisions.

*   **Q5.1 What customer characteristics most strongly influence churn? [Free text]** (2 points)
*   **Q5.2 What actionable steps should the company take to reduce churn? Suggest two strategies. [Free text]** (2 points)
