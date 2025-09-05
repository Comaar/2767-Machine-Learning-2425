# Assignment 2: SmartRetail’s Growing Challenges in Customer Engagement

## Context

SmartRetail, a rapidly growing online retailer offering products across fashion, electronics, home essentials, and groceries, is facing significant challenges in customer engagement. Despite a large customer base, the company struggles with inefficient marketing campaigns and high customer acquisition costs, primarily due to its reliance on mass marketing tactics rather than data-driven strategies.

Customer retention rates have plateaued, and marketing efforts are failing to reach the intended audience effectively. While abundant customer data is collected, the marketing team lacks a systematic approach to leverage this information for personalized, high-converting strategies.

### The CEO’s Call for a Data-Driven Strategy

During a recent board meeting, CEO Sarah Lin expressed frustration over stagnant retention rates and ineffective discount campaigns. While the CMO advocated for more promotions, the CFO warned of potential profitability erosion. Sarah Lin initiated the **Customer Intelligence Taskforce** to pivot towards a strategic, data-driven approach using machine learning and business analytics. This taskforce aims to identify valuable customer segments, predict purchasing behavior, and craft highly personalized marketing campaigns.

## Your Role as a Business Analytics Consultant

You have been hired as a Business Analytics Consultant on SmartRetail’s newly formed Customer Intelligence Taskforce. Your primary responsibility is to utilize machine learning models and business analytics techniques to extract insights from customer data and formulate actionable recommendations for the company’s marketing team.

## Available Customer Data

SmartRetail has provided access to a dataset containing the following customer information about their last interaction with the company:

*   **Customer ID** - Unique identifier for each customer
*   **Age** - Age of the customer
*   **Gender** - Gender of the customer (Male/Female)
*   **Item Purchased** - The item purchased by the customer
*   **Category** - Category of the item purchased
*   **Purchase Amount (USD)** - The amount of the purchase in USD
*   **Location** - Location where the purchase was made
*   **Size** - Size of the purchased item
*   **Color** - Color of the purchased item
*   **Season** - Season during which the purchase was made
*   **Review Rating** - Rating given by the customer for the purchased item
*   **Subscription Status** - Indicates if the customer has a subscription (Yes/No)
*   **Shipping Type** - Type of shipping chosen by the customer
*   **Discount Applied** - Indicates if a discount was applied to the purchase (Yes/No)
*   **Promo Code Used** - Indicates if a promo code was used for the purchase (Yes/No)
*   **Previous Purchases** - The total count of transactions concluded by the customer at the store, excluding the ongoing transaction
*   **Payment Method** - Customer's most preferred payment method
*   **Frequency of Purchases** - Frequency at which the customer makes purchases (e.g., Weekly, Fortnightly, Monthly)

### The Urgency to Act

The executive team expects data-backed recommendations within the next quarter to inform SmartRetail’s marketing strategy. With rising competition, SmartRetail must adopt intelligent, data-driven decision-making to maintain market share. The Customer Intelligence Taskforce's mandate is clear: "Leverage machine learning to transition from mass marketing to targeted, high-conversion strategies while maintaining profitability." The company relies on your expertise to transform data into insights, and insights into action.

## Instructions

1.  **Download the Dataset:** Use the SmartRetail’s Dataset from Moodle.
2.  **Complete All Tasks:** Follow the tasks outlined below step-by-step.
3.  **Prepare Files for Submission:** Submit your work as a ZIP file named `StudentNumber_Assignment2.zip`. This ZIP file should contain:
    *   A Jupyter Notebook file (`StudentNumber_Assignment2.ipynb`).
4.  **Upload to Moodle:** Submit the ZIP file on Moodle under the appropriate assignment link before the deadline.

---

## Assignment Questions

### Question 1 (3 points)

SmartRetail’s marketing team needs to understand customer behavior better before implementing AI-driven solutions. The company lacks visibility into how different customer segments interact with its platform, leading to inefficient and untargeted marketing. A thorough data exploration is required to uncover trends, forming the foundation for segmentation and predictive modeling efforts.

*   **Q1.1 - Provide three insights you extracted from the EDA analysis [Free text + code]** (3 points)

### Question 2 (6 points)

SmartRetail’s marketing team recognizes that different customer groups have distinct shopping behaviors, preferences, and spending habits. A one-size-fits-all marketing approach risks alienating high-value customers and overspending on ineffective promotions for low-value segments. The goal is to identify actionable customer segments to tailor marketing campaigns for maximum impact.

*   **Q2.1. Please provide the number of customers segments. [Free text + code]** (3 points)
*   **Q2.2. Are the customers segments well defined? How did you measure it? [Free text + code]** (1.5 points)
*   **Q2.3. Interpret the customer segments [Free text]** (1.5 points)

### Question 3 (5 points)

Customer retention remains a key challenge for SmartRetail. The company is concerned about customer retention. Instead of predicting churn, SmartRetail wants to identify loyal customers who consistently shop and engage with the platform through subscriptions. This will help enhance loyalty programs and retention strategies.

*   **Q3.1. Develop two models to answer the company need. Why did you choose those models? [Free text + code]** (3 points)
*   **Q3.2. Which model would you choose to be deployed? Which metric did you consider in the decision? Why? [Free text]** (2 points)

### Question 4 (6 points)

SmartRetail is looking to enhance its customer engagement and increase sales by moving away from static product suggestions toward a more dynamic and personalized approach. Given the available data, the company wants to explore how customer shopping behavior, purchase frequency, and spending patterns can be leveraged to make more relevant recommendations.

*   **Q4.1 With this in mind, how can SmartRetail develop a recommendation system that better aligns with customer purchasing behavior and preferences? What approach would you take to ensure recommendations are relevant and personalized? Justify your choice and demonstrate your implementation. [Free text + code]** (4 points)
*   **Q4.2 How do you evaluate the model? [Free text + code]** (1 point)
*   **Q4.3 Please give two suggestions to improve the dataset in the context of the recommendations systems [Free text]** (1 point)
