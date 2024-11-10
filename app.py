import pandas as pd
from flask import Flask, request, render_template
import re

# Initialize Flask app
app = Flask(__name__)

# Function to load the CSV file and clean up column names
def load_data():
    df = pd.read_csv('REPORT.csv')
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names
    return df

# Function to extract year and company name from user query
def extract_year_and_company(query):
    # Use regex to extract year and company name from query
    year_match = re.search(r'(2023|2024)', query)
    company_match = re.search(r'(MICROSOFT|APPLE|GOOGLE)', query, re.IGNORECASE)
    
    year = None
    company = None
    
    if year_match:
        year = int(year_match.group(0))
    
    if company_match:
        company = company_match.group(0).upper()
    
    return year, company

# Simple chatbot function that handles predefined queries
def simple_chatbot(user_query):
    df = load_data()
    
    # Predefined queries with their respective logic
    if user_query == "What is the total revenue?":
        total_revenue = df['TOTAL REVENUE'].sum()
        return f"The total revenue is {total_revenue}."
    
    elif user_query == "How has net income changed over the last year?":
        # Get the net income for 2023 and 2024 to calculate the change
        net_income_2024 = df[df['FISCAL YEAR'] == 2024]['NET INCOME'].values[0]
        net_income_2023 = df[df['FISCAL YEAR'] == 2023]['NET INCOME'].values[0]
        change_in_net_income = net_income_2024 - net_income_2023
        return f"The net income has changed by {change_in_net_income} over the last year."
    
    elif user_query == "What is the total liabilities?":
        total_liabilities = df['TOTAL LIABILITIES'].sum()
        return f"The total liabilities are {total_liabilities}."
    
    elif user_query == "What is the cash flow from operating activities?":
        total_cash_flow = df['CASH FLOW FROM OPERATING ACTIVITIES'].sum()
        return f"The total cash flow from operating activities is {total_cash_flow}."
    
    elif user_query == "What are the total assets?":
        total_assets = df['TOTAL ASSETS'].sum()
        return f"The total assets are {total_assets}."
    
    # More dynamic queries (extract year and company name)
    elif "net income" in user_query.lower():
        year, company = extract_year_and_company(user_query)
        if year and company:
            net_income = df[(df['FISCAL YEAR'] == year) & (df['COMPANY'] == company)]['NET INCOME'].sum()
            return f"The net income for {company} in {year} is {net_income}."
        else:
            return "Sorry, I could not extract the year or company from your query. Please try again."
    
    elif "total revenue" in user_query.lower():
        year, company = extract_year_and_company(user_query)
        if year and company:
            total_revenue = df[(df['FISCAL YEAR'] == year) & (df['COMPANY'] == company)]['TOTAL REVENUE'].sum()
            return f"The total revenue for {company} in {year} is {total_revenue}."
        elif year:
            total_revenue = df[df['FISCAL YEAR'] == year]['TOTAL REVENUE'].sum()
            return f"The total revenue for the year {year} is {total_revenue}."
        else:
            return "Sorry, I could not extract the year or company from your query. Please try again."
    
    elif "total liabilities" in user_query.lower():
        year, company = extract_year_and_company(user_query)
        if year and company:
            total_liabilities = df[(df['FISCAL YEAR'] == year) & (df['COMPANY'] == company)]['TOTAL LIABILITIES'].sum()
            return f"The total liabilities for {company} in {year} is {total_liabilities}."
        elif year:
            total_liabilities = df[df['FISCAL YEAR'] == year]['TOTAL LIABILITIES'].sum()
            return f"The total liabilities for the year {year} is {total_liabilities}."
        else:
            return "Sorry, I could not extract the year or company from your query. Please try again."
    
    elif "total assets" in user_query.lower():
        year, company = extract_year_and_company(user_query)
        if year and company:
            total_assets = df[(df['FISCAL YEAR'] == year) & (df['COMPANY'] == company)]['TOTAL ASSETS'].sum()
            return f"The total assets for {company} in {year} is {total_assets}."
        elif year:
            total_assets = df[df['FISCAL YEAR'] == year]['TOTAL ASSETS'].sum()
            return f"The total assets for the year {year} is {total_assets}."
        else:
            return "Sorry, I could not extract the year or company from your query. Please try again."
    
    elif "cash flow" in user_query.lower():
        year, company = extract_year_and_company(user_query)
        if year and company:
            total_cash_flow = df[(df['FISCAL YEAR'] == year) & (df['COMPANY'] == company)]['CASH FLOW FROM OPERATING ACTIVITIES'].sum()
            return f"The cash flow from operating activities for {company} in {year} is {total_cash_flow}."
        elif year:
            total_cash_flow = df[df['FISCAL YEAR'] == year]['CASH FLOW FROM OPERATING ACTIVITIES'].sum()
            return f"The cash flow from operating activities for the year {year} is {total_cash_flow}."
        else:
            return "Sorry, I could not extract the year or company from your query. Please try again."
    
    else:
        return "Sorry, I can only provide information on predefined queries or ask about net income, revenue, assets, liabilities, or cash flow."

# Flask route to handle web requests
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["user_query"]
        response = simple_chatbot(user_query)
        return render_template("index.html", response=response)
    return render_template("index.html", response="")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
