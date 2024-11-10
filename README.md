# chatbot_project
# Financial Chatbot
A simple chatbot built with Flask that answers financial queries based on data from a CSV file (REPORT.csv). The chatbot can provide key financial insights such as total revenue, net income change, total liabilities, cash flow from operating activities, and more.

Features
Predefined Queries: The chatbot can answer specific financial questions such as:

Total revenue, Net income change over the last year, Total liabilities, Cash flow from operating activities, Total assets

Company-Specific Queries: Users can ask about specific companies and financial data for particular years.

Data Handling: The chatbot reads from a CSV file (REPORT.csv) and provides answers based on that data.

Prerequisites

Python 3.x

Flask

pandas

Installation

pip install Flask pandas

Add the REPORT.csv file: Make sure the REPORT.csv file containing the financial data is in the same directory as the application file (app.py).

Usage

Run the Flask app:

python app.py

Interact with the chatbot:

Open your web browser and go to http://127.0.0.1:5000/.

Type your query into the input box, and the chatbot will respond with the answer based on the available data in REPORT.csv.

Example Queries

"What is the total revenue?"

"How has net income changed over the last year?"

"What is the cash flow from operating activities?"

"What are the total assets?"

"What is the net income for Microsoft in 2024?"

Limitations

The chatbot can only respond to queries defined in the code.
It relies on the REPORT.csv file for data. If the required data is missing or incorrectly formatted, the chatbot may not provide meaningful answers.
It is limited to financial data and does not handle other types of queries.

