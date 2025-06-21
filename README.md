# 💼 Financial Report Chatbot with Flask

A simple yet powerful **Flask-based chatbot** that interacts with financial data from companies like **MICROSOFT**, **APPLE**, and **GOOGLE**. It responds to both predefined and dynamic queries using regex-based natural language parsing.

---

## 📊 Key Features

- ✅ Answers financial queries such as:
  - Total revenue
  - Net income change
  - Cash flow from operating activities
  - Total liabilities and assets
- ✅ Supports **year-specific** and **company-specific** queries (e.g., "net income for Apple in 2024")
- ✅ Uses **regex extraction** for identifying year and company from user queries
- ✅ Powered by a backend **CSV dataset (`REPORT.csv`)**
- ✅ Minimal front-end using `index.html`

---

## 🧠 How It Works

1. Load financial data from `REPORT.csv`  
2. Match the user’s query to a known pattern  
3. Extract keywords like **company** and **year** using regex  
4. Respond using filtered data from the DataFrame  

Example:
```
Q: What is the total revenue for Microsoft in 2023?  
→ A: The total revenue for MICROSOFT in 2023 is 420000000.
```

---

## 🛠 Tech Stack

- 🐍 Python 3.x  
- 🌐 Flask  
- 📊 Pandas  
- 🧠 Regex (`re`)  

---

## 📁 Project Structure

```
financial-chatbot/
├── app.py                # Main Flask backend
├── REPORT.csv            # Financial dataset (ensure correct column names)
├── templates/
│   └── index.html        # Simple UI to enter queries
```

---

## 📦 Dependencies

Install with:

```
pip install flask pandas
```

---

## ▶️ How to Run

1. Place your `REPORT.csv` file in the same directory  
2. Launch the app:

```
python app.py
```

3. Open in browser:

```
http://localhost:5000
```

---

## 🗃️ Example Queries

- `What is the total revenue?`  
- `How has net income changed over the last year?`  
- `What is the total liabilities?`  
- `Cash flow from operating activities for Google in 2024`  
- `Total assets for Apple in 2023`

---

## ⚠️ Notes

- CSV file must contain columns:  
  `FISCAL YEAR`, `COMPANY`, `NET INCOME`, `TOTAL REVENUE`, `TOTAL ASSETS`, `TOTAL LIABILITIES`, `CASH FLOW FROM OPERATING ACTIVITIES`
- Supported companies: `MICROSOFT`, `APPLE`, `GOOGLE`  
  *(add more in `extract_year_and_company()` as needed)*  
- Supported years: `2023`, `2024`

---

