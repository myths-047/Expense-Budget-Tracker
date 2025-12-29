# 💰 Smart Expense Tracker

A web-based expense tracking application built with Flask and SQLite. Track your expenses, set budgets for different categories, and monitor your spending habits.

## Features

- ✅ **Category Management**: Create and manage expense categories with spending limits
- 💸 **Expense Tracking**: Add, view, and delete expenses with descriptions and dates
- 📊 **Budget Monitoring**: Real-time tracking of spending vs budget limits
- 🎨 **Clean UI**: Responsive design with intuitive navigation
- 📈 **Dashboard**: Overview of total expenses, spending, and categories

## Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite3
- **Frontend**: HTML, CSS (inline), Jinja2 templating
- **Version Control**: Git, GitHub

## Project Structure
```
Smart expense tracker/
├── app.py                 # Main Flask application
├── expense_tracker.db     # SQLite database (auto-generated)
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Dashboard/home page
│   ├── add_category.html # Add category form
│   ├── add_expense.html  # Add expense form
│   ├── expenses.html     # View all expenses
│   └── categories.html   # Budget status page
├── static/               # Static files folder
├── venv/                 # Virtual environment
└── README.md            # This file
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR_USERNAME/smart-expense-tracker.git
   cd smart-expense-tracker
```

2. **Create virtual environment**
```bash
   python -m venv venv
```

3. **Activate virtual environment**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**
```bash
   pip install flask
```

5. **Run the application**
```bash
   python app.py
```

6. **Open in browser**
   Navigate to `http://127.0.0.1:5000/`

## Usage

### Adding a Category
1. Click "Add Category" in the navigation
2. Enter category name (e.g., "Food", "Transport")
3. Set spending limit
4. Click "Add Category"

### Adding an Expense
1. Click "Add Expense" in the navigation
2. Select category from dropdown
3. Enter date, description, and amount
4. Click "Add Expense"

### Viewing Expenses
- Click "Expenses" to see all expenses in a table
- Delete expenses using the delete button
- View total spending at the bottom

### Monitoring Budget
- Click "Budget Status" to see spending vs limits
- Color-coded status indicators:
  - ✅ Green: Under 80% of budget
  - ⚠️ Orange: 80-100% of budget
  - ❌ Red: Over budget

## Database Schema

### Categories Table
- `id`: INTEGER (Primary Key)
- `name`: TEXT
- `spending_limit`: REAL

### Expenses Table
- `id`: INTEGER (Primary Key)
- `category_id`: INTEGER (Foreign Key)
- `date`: TEXT
- `description`: TEXT
- `amount`: REAL

## Features in Action

- **Dashboard**: View overview with total expenses, spending, and category count
- **Real-time Updates**: All changes reflect immediately
- **Data Validation**: Form validation ensures data integrity
- **Confirmation Prompts**: Confirmation before deleting expenses

## Future Enhancements

Potential features for future versions:
- Edit category and expense functionality
- Date range filtering for expenses
- Export data to CSV
- Visualizations and charts
- Multiple user support with authentication
- Monthly/yearly expense reports

Feel free to fork and modify as needed!

## Author

- GitHub: https://github.com/myths-047


