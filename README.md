# merp

A REST api written in Django

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ https://github.com/DanSheremeta/merp.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd merp
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ python -m venv env
            $ env/Scripts/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```
    
## All end-points:

<b>1. Admin Access</b>
<ul>
    <li>Admin Section: http://127.0.0.1:8000/dashboard/</li>
</ul>
<br>

<b>2. Accounts</b>
<ul>
    <li>Registration: http://127.0.0.1:8000/accounts/sign-in/</li>
    <li>Login: http://127.0.0.1:8000/accounts/login/</li>
    <li>Logout: http://127.0.0.1:8000/accounts/logout/</li>
</ul>
<br>

<b>3. Events</b>
<ul>
    <li>Events list: http://127.0.0.1:8000/events/</li>
    <li>Registration for specific event (IsAuthenticated permission): http://127.0.0.1:8000/events/&lt;int:event_id&gt;/register/</li>
    <li>Cancel a booking for event (IsAdmin permission): http://127.0.0.1:8000/events/reservation-code/&lt;int:reservation_code_id&gt;/cancel/</li>
</ul>
<br>
