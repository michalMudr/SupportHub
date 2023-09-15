Version 1.1 has Templates set up for UserDashboard, Ticket

SupportHub
SupportHub Web Application SupportHub is a web-based application developed using Django, designed to streamline customer support and ticket management.

Prerequisites Before you can run the SupportHub application, ensure you have the following prerequisites installed on your system:

Python 3.x: You can download Python from python.org. 

Django: Install Django using pip with the command: pip install django 

Getting Started Follow these steps to get the SupportHub application up and running on your local machine:

Clone the Repository: Clone the SupportHub repository to your local machine using Git:

bash Copy code git clone https://github.com/michalMudr/SupportHub.git 

Navigate to the Project Directory: Change your working directory to the project folder:

bash Copy code cd SupportHub-MichalM 

Create a Virtual Environment: It's good practice to create a virtual environment for your project to isolate dependencies. You can create one using virtualenv or venv (Python 3.3+). For example:

Copy code python -m venv venv 

Activate the Virtual Environment: Activate the virtual environment depending on your operating system:

On Windows: Copy code venv\Scripts\activate On macOS and Linux: bash Copy code source venv/bin/activate Install Dependencies: Install the required Python dependencies:

Copy code pip install -r requirements.txt 

Apply Migrations: Apply the database migrations to set up the database schema:


Copy code python manage.py migrate 

Create a Superuser (Admin User): You can create an admin user to manage the application:

Copy code python manage.py createsuperuser 

Run the Development Server: Start the Django development server:

Copy code python manage.py runserver 

Access the Application: Open your web browser and navigate to the following URL:

Copy code http://localhost:8000/userdashboard/ 
Admin Panel: Access the admin panel by going to:

bash Copy code http://localhost:8000/admin/ Log in with the superuser credentials you created earlier to manage the application.

Usage Explore the SupportHub application by creating and managing tickets, users, and support-related activities. Customize the application according to your needs by modifying the Django project files. Contributing

Support If you encounter any issues or have questions, please open an issue on GitHub.