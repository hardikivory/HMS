

PROJECT NAME: HOSTEL MANAGEMENT SYSTEM ( HMS )

Description:
        - This project is based on Hostel Management System. Its helps for managing 'Guests' and 'Workers' data. so many features likes Guest and Worker Registation,
        Guest Room Booking, Room Services, Guest Fees collect.


Requirements:
        - python 3.9.10
        - Django==4.0.4

Instalation:
        1. python 3.9.10
        Command - pip3 install python 2.9.10

        2. Django==4.0.4
        Command - pip3 install Django==4.0.4



Repository Structure:

        HMS
         |
         |---- accounts
         |        |
         |        |--- __pycache__
         |        |
         |        |--- migrations
         |        |
         |        |--- __init__.py
         |        |
         |        |--- admin.py
         |        |
         |        |--- apps.py
         |        |
         |        |--- forms.py
         |        |
         |        |--- models.py
         |        |
         |        |--- test.py
         |        |
         |        |--- urls.py
         |        |
         |        |--- views.py
         |         
         |---- HMS
         |      |
         |      |--- __pycache__
         |      |
         |      |--- __init__.py
         |      |
         |      |--- asgi.py
         |      |
         |      |--- settings.py
         |      |
         |      |--- urls.py
         |      |
         |      |--- wsgi.py
         |
         |---- static
         |       |
         |       |--- admin
         |              |
         |              |--- css
         |              |--- fonts
         |              |--- img
         |              |--- js
         |
         |---- templates
         |       |
         |       |--- guestdashboard.html
         |       |
         |       |--- guestupdate.html
         |       |
         |       |--- home.html
         |       |
         |       |--- login.html
         |       |
         |       |--- nav.html
         |       |
         |       |--- register.html
         |       |
         |       |--- workerdashboard.html
         |       |
         |       |--- workerupdate.html
         |
         |---- db.sqlite3
         |
         |---- manage.py
         |
         |---- README.md





All the APIs:
                

                1. User related APIs

                - Home page
                        url - http://127.0.0.1:8000/accounts/
                        Description - rediret home page.

                - Register
                        url - http://127.0.0.1:8000/accounts/register/
                        Description - rediret Register page. where user register account.

                - Login
                        url - http://127.0.0.1:8000/accounts/login/
                        Description - rediret login page. where user login account.

                - Logout
                        url - http://127.0.0.1:8000/accounts/logout/
                        Description - rediret logout page. where user logout own account.

                - Guest Dashboard
                        url - http://127.0.0.1:8000/accounts/guest/dashboard/
                        Description - rediret guest dashboard page. where guest show own personal and room informations.

                - Guest Update Profile
                        url - http://127.0.0.1:8000/accounts/guest/update/<id>
                        Description - rediret guest update profile page. where user update own information.

                - Guest Delete Profile
                        url - http://127.0.0.1:8000/accounts/guest/delete/<id>
                        Description - Delete guest profile and redirect home page.

                - Worker Dashboard
                        url - http://127.0.0.1:8000/accounts/worker/dashboard/
                        Description - rediret worker dashboard page. where worker show own personal and work informations.

                - Worker Update Profile
                        url - http://127.0.0.1:8000/accounts/worker/update/<id>
                        Description - rediret worker update profile page. where worker update own information.

                - Worker Delete Profile
                        url - http://127.0.0.1:8000/accounts/worker/delete/<id>
                        Description - Delete worker profile and redirect home page.

                
                




                
                2. Admin related APIs


                -Admin Pannel Login Page
                        url - http://127.0.0.1:8000/admin/login/?next=/admin/login
                        Description - redirect admin login page.

                - Admin Pannel
                        url - http://127.0.0.1:8000/admin/
                        Description - redirect the admin pannel. where admin can show all the tables.

                - Guest table
                        url - http://127.0.0.1:8000/admin/accounts/guest/
                        Description - redirect the guest table. where show all the guest data.

                - Worker table
                        url - http://127.0.0.1:8000/admin/accounts/worker/
                        Description - redirect the worker table. where show all the worker data.

                - User table
                        url - http://127.0.0.1:8000/admin/accounts/user/
                        Description - redirect the user table. where show all the user (worker and guest) data.

                - Admin Logout
                        url - http://127.0.0.1:8000/admin/logout/
                        Description - Admin can logout. when this api call. and rediret to admin login page.

                - Room Type
                        url - http://127.0.0.1:8000/admin/accounts/roomtype/
                        Description - show all the types of room.

                - Add Room Type
                        url - http://127.0.0.1:8000/admin/accounts/roomtype/add/
                        Description - Add new room type.

                - Room
                        url - http://127.0.0.1:8000/admin/accounts/room/
                        Description - show all the room informations.

                - Add Room
                        url - http://127.0.0.1:8000/admin/accounts/room/add/
                        Description - Add new room.
