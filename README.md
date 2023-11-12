# User Registry
A FastAPI application to generate random passwords of specified length.

## Installation
1. Clone the project from GitHub
    ```git
    git clone https://github.com/koushikromel/fluvi-task2.giit
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```
    uvicorn main:app --host 0.0.0.0 --port 3000
    ```

## Endpoints
1. Create User
    Create new user
    -   Method: POST
    -   Endpoint: http://0.0.0.0:3000/user/create
    -   Parameters:
        - name: str
        - email: EmailStr
    -   Request: POST /user/create
    -   Response: 
        ```json
            {
                "_id": "4c02c44d-c49b-459a-a9b6-e5eec393d146",
                "name": "new_user",
                "email": "newuser@example.com",
                "created_at": "2023-11-12T18:15:38.095147"
            }
        ```
2. Get User
    Get user by user_id
    -   Method: GET
    -   Endpoint: http://0.0.0.0:3000/user/get
    -   Parameters:
        - user_id: uuid
    -   Request: GET /user/get
    -   Response: 
        ```json
            {
                "name": "updated_name",
                "email": "updated_mail@example.com"
            }
        ```
3. Update User
    Update user by user_id and updating data
    -   Method: PUT
    -   Endpoint: http://0.0.0.0:3000/user/update
    -   Parameters:
        - user_id: uuid
        - name: str(Optional)
        - email: EmailStr(Optional)
    -   Request: PUT /user/update
    -   Response: 
        ```json
            {
                "name": "new_user_updated",
                "email": "updated_email@example.com"
            }
        ```
4. Delete User
    Delete user by user_id
    -   Method: DELETE
    -   Endpoint: http://0.0.0.0:3000/user/delete
    -   Parameters:
        - user_id: uuid
    -   Request: DELETE /user/delete
    -   Response: 
        ```json
            {
                "message": "User with email: second_user@example.com is deleted successfully"
            }
        ```
## License
This Project is licensed under the MIT License - see the [License](https://choosealicense.com/licenses/mit/) file for details.