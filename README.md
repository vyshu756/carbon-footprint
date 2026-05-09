Coal Carbon Footprint Dashboard

A Django-based web application developed to monitor, calculate, and visualize carbon dioxide (CO₂) emissions generated from coal mining operations. The system enables tracking of emissions from various mining activities such as diesel consumption, electricity usage, explosives, and transportation through an interactive analytical dashboard.

The application automatically calculates CO₂ emissions using predefined emission factors and presents the results through graphical visualizations and emission analytics. It also provides an admin management system for maintaining operational and environmental data efficiently.

Features
Mining activity data management
Automated CO₂ emission calculation
Interactive dashboard with charts and analytics
Emission source tracking and comparison
Admin panel for data management
Responsive and user-friendly interface
Technology Stack
Python
Django Framework
SQLite Database
Matplotlib
HTML/CSS


Installation & Setup
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Run the development server
python manage.py runserver

# 5. Open in browser
http://127.0.0.1:8000/dashboard/
Project Structure
coal_carbon_app/
│
├── coal_carbon/
├── mines/
├── templates/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md


Purpose of the Project

The primary objective of this project is to support environmental sustainability in mining operations by providing a platform for monitoring carbon emissions, analyzing environmental impact, and generating visual analytical reports.
