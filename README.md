# Simple-Ticket-CRUD-and-Verification-API
 
Python - Backend, Django REST framework

# to run API server
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver

# Endpoints
/api/tickets/
Http Method: GET
Functionality: Display all tickets that exist on the database.

/api/tickets/:id
Http Method: GET, PUT, DELETE
Functionality: Display specific ticket with corresponding id, additional interface for updating values where the id belongs to and able to delete that specific data.

/api/tickets/create
Http Method: POST
Functionality: Create new ticket.

/api/tickets/verification
Http Method: PUT
Functionality: Validating ticket if the inputted TicketCode exist and hasn't been validated before.

/api/member
Http Method: GET, POST
Functionality: Display all member types on the database and create new member types.

/api/member/:id
Http Method: GET, PUT, DELETE
Functionality: Display specific member with corresponding id, additional interface for updating values where the id belongs to and able to delete that specific data.
