git clone https://github.com/your-username/vendor-management-system.git
cd vendor-management-system

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
set the password (or you can use 'san' username and and password 'san')
python manage.py runserver

you can cheak database using /admin
Open Postman: Launch the Postman application on your computer.
Create a New Request: Click on the "New" button in the top left corner of the Postman window to create a new request.
Define Request Type: Select the appropriate HTTP method (GET, POST, PUT, DELETE) for the API endpoint you want to interact with.

List all Vendors (GET Request)
Request URL: http://127.0.0.1:8000/api/vendors/
Method: GET
 Create a New Vendor (POST Request)
Request URL: http://127.0.0.1:8000/api/vendors/
Method: POST
Headers: Add a header Content-Type: application/json





Retrieve a Specific Vendor (GET Request)
Request URL: http://127.0.0.1:8000/api/vendors/<vendor_id>/
(Replace <vendor_id> with the actual ID of the vendor you want to retrieve)
Method: GET

Update a Vendor (PUT Request)
Request URL: http://127.0.0.1:8000/api/vendors/<vendor_id>/
(Replace <vendor_id> with the ID of the vendor you want to update)
Method: PUT
Headers: Add a header Content-Type: application/json
Body (raw JSON):
json
Copy code
{
  "name": "Updated Vendor Name",
  "contact_details": "Updated Contact Info",
  "address": "Updated Vendor Address",
  "vendor_code": "V002"
}



 Delete a Vendor (DELETE Request)
Request URL: http://127.0.0.1:8000/api/vendors/<vendor_id>/
(Replace <vendor_id> with the ID of the vendor you want to delete)
Method: DELETE
 Sending Requests and Viewing Responses
Send Request: After setting up the request type, URL, method, headers, and body (if applicable), click the "Send" button in Postman to execute the request.
View Response: Postman will display the response received from the API server. You can view the response body, status code, headers, and more in the Postman interface.
 Handling Authentication (Optional)



or  you can directly cheak the api in chrome browser by using API endpoint  

## Contributing

Contributions By Sandeep Tale! 🚀

Thank you,

Happy coding! 😊



