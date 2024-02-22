# Student_Management_System

## Development Setup

1. Create a repository using this template or clone the repository
    ```    
    git clone https://github.com/zahidhasanmilu/Student_Management_System.git
    ```

2. Create a virtual environment
   ```
   python -m venv env
   ```
3. Activate the virtual environment
   ```
   #in Windows
    .\env\Scripts\activate

    #in Linux
    source env/bin/activate
   ```
4. Install modules
   ```
   pip install -r requirements.txt
   ```
5. Migrate database
   ```
   python manage.py migrate
   ```
6. Create superuser
    ```
    python manage.py createsuperuser
    ```
7. Run the project
    ```
    python manage.py runserver
    ```
