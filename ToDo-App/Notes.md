Python based web-framework for building modern apis

Webpage → full stack application → Fast API server

python virtual environments: isolated environment with all dependencies installed

pip - python package manager - python3 -m pip —version

setting up Virtual Environment: use venv  - python3 -m venv fastapivenv

activate virtual Environment - source fastapivenv/bin/activate

Install fastapi: pip install fastapi

Install uvicorn - webserver for fastapi - pip install uvicorn[standard]

Fastapi uses UVICorn ASGI to respond to the requests. 

Web server → WSGI / ASGI → Web application

**Gateway Interfaces:**

1. WSGI - Web-server Gateway Interface
    1. Request → sequential execution of code in the endpoint → Response
    2. Sequential handle of requests by each worker. [Gunicorn]
    3. no. of workers = 2 x (no. of cpu cores) + 1
2. ASGI - Asynchronous Server Gatewar Interface
    1. Requests → Time of Execution → if more time → handle next request → get first request response → get next request response
    2. No. of requests handled are more. 
    3. Concurrent handle of request [UVCorn]

FastAPI has Swagger UI implemented already. /docs will have all the requests documented and we can call the API endpoints using the /docs itself. 

Project1: Creating and Enhancing books to learn the basics of FastAPI

CRUD → Create, Read, Update, Delete

Request: Webpage sends a request to the FastAPI server

Response: FastAPI sends response to the webpage

HTTP Request Methods: 

1. Create → Post
2. Read → Get
3. Update → Put
4. Delete → Delete

async stands for asynchronous. for FastAPI we don't need to explicitly use async because it is already asynchronous.

to run the application with main file as test: 

1. we can use uvicorn test: app —reload. here uvicorn is ASGI. Filename is test which contains app. once this is executed in the terminal it provides 127.0.0.1:8000 which will have a default page. 127.0.0.1 → [localhost](http://localhost) and 8000 is port where it runs. —reload is used because whenever a change is detected, the server gets reloaded. 
2. We can use for the newest version: fastapi run filename.py: this will run production or for development server we can use fastapi dev filename.py

Path Parameters: they are request parameters that have been attached to the URL. They are usually defined as a way to find information based on location

→  URL: 127.0.0.1:8000/info is static path. 

→ URL: 127.0.0.1:8000/info/info1 → for info 1. to make it dynamic we use path parameter. 

→ Order matters with path parameters. 

→ to encode “ “(space) we use %20 ex: title one → title%20one (%20 = space)

string.casefold() vs string.lower() or string.upper():

string.casefold() does not take any parameters and returns a new, fully lowercased string, optimized for Unicode-aware, case-insensitive comparisons.

string.lower() and string.upper() convert the string to lowercase/uppercase respectively, by changing the ASCII or Unicode values of the characters.

Query Parameters: request parameters that have been attached after a “?” → they have name=value pairs → Sort and filter through data that is not marked by a path parameter. 

ex: 127.0.0.1:8000/books/?category=math → query parameter category=math where the info is getting filtered with category =math 

GET → The GET method is used to **retrieve** data from the server. It is one of the standard HTTP methods used to interact with web APIs. @app.get() decorator is used. Get method cannot have a request body. 

POST → Used to **create** the data. Post can have the body that has additional information that get does not have. Ex: {’title’:’one’, ‘category’ : “Fiction’}. A **request** body is data sent by the client to your API. A **response** body is the data your API sends to the client. we don't necessarily have request body for all the apis end points but we will have response body for almost all the apis. 

**IMPORTANT NOTE: when sending request body, always use double quotes (” : ”)**

PUT → Used to **update** the data. PUT can have body that has additional data. ex: {’title’ : “Xam”, “category” : “Science”}

DELETE → Used to **delete** the data. 

Pydantics → library that is used for data modeling, data parsing and has efficient error handling. → commonly used as a resource for data validation and how to handle data coming into the FastAPI Application. → pydanctic field data validation can run on each variable/ element. 

BaseModel is the foundational class in the Pydantic library for defining data structures and enforcing data validation in Python.

Field(): used to provide extra information, customization, and metadata for the fields (variables). it also make validation before executing the code in the endpoint. 

model_config: we can set the basic schema of the request body. we use “json_schema_extra” to do this. 

Path → its a function/class where we can put data validations on path parameters

Query → its a function/class where we can put data validations on query parameters

Status Codes: International standards on how a client/server should handle the result of a request.

1xx → 100 series → Information response: request processing 

2xx → 200 series → Success: Request successfully complete

3xx → 300 series → Redirection: Further action must be complete

4xx → 400 series → Client Errors → An error was caused by the client

5xx → 500 series → Server Errors → An error occurred on the server side

Common status codes

200 → Okay

201 → Created

204 → No content

400 - Bad Request

401 → Unauthorized

404 - Not Found 

422 - Unprocessable Entity

500 → Internal server error

**Database**: structured information of data, which is stored in the system. → the data can be easily accessed, modified and can be controlled and organized. 

Many databases use a structured query language(SQL) to modify and write data. 

**SQL** → Standard language for dealing with relational databases. 

**SQLite** → it is a database engine which reads and writes directly to ordinary disk files. it does not have a separate server process 

**SQL-Alchemy** → SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

Basic Concepts:

1. primary key: A primary key is a unique column within a relational database.
2. Foreign key: A foreign key is a column within a relational database table that provide a link  between two separate tables. it references a primary key of another table. 

**Basic Queries:** 

1. Insertion: Insert Into `table_name` (Columns) values (column values)
2. Selection: select * from `table_name`  or select column_name from `table_name`
3. Update: Update `tablename` SET `column_name` = `new_value` where `condition`
4. Delete: Delete from `tablename` where `condition`
5. Alter: Alter table `tablename` Add `new_column_name` column definition. 
6. Where clause:  is used to extract only those records that fulfill a specified condition

Authentication: the process of verifying the identity of a user, device, or other entity, typically by confirming they possess certain credentials or attributes. 

| Feature | Explanation |
| --- | --- |
| **Dependency** | A function/class whose result is injected into a route |
| **Depends()** | Tells FastAPI to run and inject a dependency |
| **Common Uses** | DB connection, auth, validation, shared logic |
| **Benefits** | Cleaner code, reusable logic, auto validation, easier testing |

Scale Application using Router:  One application may have many fastapi files, to scale them and run one application which handles rest of the api files, we use Router package. This can be done using **APIRouter class** → A  FastAPI class used to create route groups in a modular way,
improving code readability, organization, and scalability of the application.

**APIRouter** helps to clean the code and handle multiple fastapi files which helps in code usability and code reusability. this also benefits in scalability of the application. 

**passlib:** passlib is a password hashing library which provides cross-platform implementations of over 30 password hashing algorithms. 

**bycript:** bcrypt is a cryptographic hashing algorithm designed specifically for secure password hashing. It's widely used in web applications and frameworks like FastAPI, Django, Flask, etc.A **salt** is a **random string** added to the password **before hashing**. 

### Why use Salt?

- Prevents **hash collisions** across users with the same password.
- Protects against **rainbow table** attacks.
- Makes brute-force attacks slower.

We are using passlib and bcrypt to hash the password and store the password. this is one of the strongest hashing technique where a random string is added to the password and then hashed which handles an edge case of same passwords for multiple users. 

**python-multipart:** Python-Multipart is a library for handling multipart/form-data POST requests. 

**OAuth2** (Open Authorization 2.0) is a **secure authorization framework** that allows one application (the *client*) to access resources (like user data) on behalf of a user, **without sharing the user's credentials**.

**OAuth2PasswordRequestForm:**
A FastAPI class that auto-handles username & password inputs from form data (via application/x-www-form-urlencoded). Used for login endpoints to simplify form parsing and inject username and password via dependency injection.

With OAuth2, users authenticate once, receive a token, and use that token for future access — keeping the password safe.

**application/x-www-form-urlencoded:**
A standard way to encode form data in HTTP POST requests (e.g., username=ajith&password=123). It's not encrypted, but safe when sent over HTTPS.

Authentication and Authorization with JWT:

JWT → Json Web Token is a self-contained way to securely transmit data and information between two parties using  a JSON Object. → it can be trusted because each jwt can be digitally signed.

→ It can be used when dealing with authorization. 

JSON Web Token Structure: 

→ A JWT is created of three separate parts separated by dots (.) which include:

Header: (A)

Payload: (B)

Signature: (C)

Header usually consists of two parts: (alg) → algorithm for signing → typ → specific type of token, then it is encoded using Base64 to create the first part of the JWT(A) 

{

“alg: : “HS256”,

“typ” : “JWT

}

Payload: Consists of Data. The payload data contains claims, and three different types of claims i.e., data being transmitted and additional information including the timestamp at which it was issued and the expiry time of the token. The payload is then **Base64Url** encoded to form the second part of the JSON Web Token. Payload is the second Part of JWT(B)

→ Registered  → Predefined : iss (issuer), exp (expiration time), sub (subject), aud (audience)

→ Public → These can be defined at will by those using JWTs.

→ Private → These are the custom claims created to share information between parties that agree on using them and are neither registered or public claims.

ex: for payload: 

{
"sub": "1234567890",
"name": "John Doe",
"admin": true
}

Signature: it is created by using the algorithm in the header to hash out the encoded header, encoded payload with a secret. A secret can be anything, but is saved somewhere on the server that client does not have the access to.  the signature is the third and final part of the JWT(C)

Example of JWT:

Header: {”alg” : “HS256” , “typ”: “JWT”}

Payload: 

{
"sub": "1234567890",
"name": "John Doe",
"admin": true
}

Signature:

HMACSHA256(
base64UrlEncode(header) + "." +
base64UrlEncode(payload),
secret)

This is how the JWT looks after encoded with signature.

![image.png](attachment:cf69a4c8-e2f8-4be0-8e7d-0b3d853f9835:image.png)

on server side, we can decode the encoded jwt and retrieve the credentials. but the jwt concept ususally works like: 

1. **User Logs In**: The client (browser) sends login credentials to the [server](https://www.geeksforgeeks.org/what-is-server/).
2. **Server Generates JWT**: If credentials are valid, the server creates a JWT containing user data and signs it with a secret key.
3. **Token Sent to Client**: The JWT is sent back to the client and stored (usually in [localStorage](https://www.geeksforgeeks.org/javascript-localstorage/) or a cookie).
4. **Client Sends Token in Requests**: For protected routes, the client includes the JWT in the Authorization header (Bearer Token).
5. **Server Verifies and Responds**: The server verifies the token, extracts user info, and processes the request if valid.

through this concept, the client doesn't have to send the credentials every time, it will just send the token and the server does validation and verification of the token shared. 

**JOSE** (JavaScript Object Signing and Encryption) is a set of specifications used for securely transmitting data between parties using JSON. In Python, the **`python-jose`** library is a commonly used implementation for working with these specifications.

- **JWT (JSON Web Tokens)**: Signing, verifying, and decoding tokens
- **JWS (JSON Web Signature)**: Signing data
- **JWE (JSON Web Encryption)**: Encrypting and decrypting data (less common)

It is useful in **authentication and authorization flows**, especially with OAuth2.

To generate a secret_key, we can use openssl rand -hex 32

**OAuth2PasswordBearer** is a class in FastAPI that is used for handling security and authentication. By using this we will create a dependency for api endpoints to actually validate and verify the token that is passed. 

Using user_dependency, we can authenticate and authorize requests. If the user is logged in and sends a valid token, user_dependency will decode the token and inject the current user into the request.

with FastAPI + Swagger :

When you use `OAuth2PasswordBearer`, Swagger UI (under `/docs`) automatically:

- **Shows a lock icon** on protected routes.
- Lets you **"Authorize"** with a token.
- **Sends that token in the Authorization header** with all secured requests.

Apply User authentication for all CRUD endpoints. 

Production Database:

→ SQL and Postgresql

SQLite3 vs Production DBMS:

→ SQLite3 provide Local Data storage for individual applications and devices

→ Sqlite3 emphasizes economy, efficiency and simplicity

→ SQLite3 small and medium applications

→ Production Databases (SQL and Postgresql) focuses on scalability, concurrency and control

→ SQLite3 runs in-memory or local disk, which allows development of a sqlite3 data to be easy. 

→ Production DBMS run on their server and port. which means we need to make sure database is running and have authentication linking to the DBMS. 

→ Production DBMS, we need to deploy the database separate from the application.

→ Postgresql is a production ready dbms and also RDBMS: Relational database management system which is opensource

→ Requires a server and very scalable. 

→ To setup: install postgresql, postgresqladmin. 

→ connect [localhost](http://localhost) through 5432 port and also create username and password. 

→ Once the server is created, creating database is easier and also can be done through pgadmin web page. we have installed web version, we need to run 

`sudo /usr/pgadmin4/bin/setup-web.sh`

→ **Psycopg** is the most popular PostgreSQL database adapter. This helps in connecting the postgresql with FastAPI application. 

→ SQLALCHEMY_DATABASE_URL = "postgresql://ajithbm01:Ajithbm%4001@localhost/TodoAppDatabase” this is to setup Database URL through SQLALCHEMY

→ Mysql → Opensource RDBMS → Requires Server → Runs on 3306

→ Similarly install myql server and run it. connect the Databse using local host through 3306 port and create username and password. 

**Alembic** → Lightweight database migration tool for when using SQLAlchemy

→ Migration tools allow us to plan, transfer and upgrade resources within databases. 

→ Alembic allows to change a SQLAlchemy database table after it has been created

→ SQLAlchemy creates tables but will not enhance it. → Alembic provides the creation and invocation of change management scripts. → this allows to be able to create migration environments and be able to change data.

Basic Commands in Alembic:

alembic init <foldername> → initialise a new, generic environment

alembic revision -m <message> → creates a new version of the environment

alembic upgrade <revision#> → Run upgrade migration to database

alembic downgrade -1 → Run downgrade migration to database

After initialization, two new items will appear: → alembic.ini and alembic directory

→ these are created automatically by alembic so we can upgrade and downgrade and keep data integrity of out application.

→ Alembic.ini → file that alembic looks for when invoked. 

→ contains a bunch of configuration information for alembic that we are able to change to match our project.

→ Alembic Directory: has all environmental properties for alembic and holds all revisions of our application. → we call migrations for upgrading and downgrading. 

Installation: → pip install alembic

### `env.py`

- Central config file.
- Tells Alembic how to connect to the database and where your models are.
- You’ll usually import your `Base` from SQLAlchemy here (e.g., `from models import Base`).

### `versions/`

- This contains **auto-generated migration files**.
- Each file has an autogenerated name

`alembic.ini` contains connection info. 

alembic.ini mostly contains:

| Setting | Purpose |
| --- | --- |
| `script_location` | Where your migration scripts live (`alembic/`) |
| `sqlalchemy.url` | DB connection string — format: `driver://user:pass@host` |
| `loggers` | Log settings (don't usually change) |

alembic revision: it is how we create a new alembic file where we can add some type of database upgrade. when we run `alembic revision -m “create phone number col on users table”`

it creates a new file where we can write the upgrade code and each file will have a revision id. 

to run alembic upgrade migration we use: `alembic upgrade <revisionID>` 

to run alembic downgrade migrate we use:  `alembic downgrade -1`

Changes in alembic.ini → put Database path for `sqlalchemy.url`

in env.py: import models and put the `target_metadata` = `models.Base.metadata`

**Pytest:** Testing framework for python → simple, scalable and has ability to handle both unit and integration tests. 

→ has native assertions

→ fixtures - feature setup and teadown

→ parameterized testing - run same tests with different data

To install Pytest: `pip install pytest`

→ Assertions → assertions are statements that check whether a specific condition is true during the execution of a program

→ Pytest will run all tests automatically that sit within files that have the name `test` in them. 

→ if condition is `true` = test passes

→ if condition is `false` = test fails

Pytest Basics:

1. validate integers
2. validate instances
3. validate booleans
4. validate types
5. validate greater than and less than

pytest objects:

1. Fixtures: Fixtures are functions decorated with @pytest.fixture that provide a defined, reliable, and consistent context for tests.

`TestClient` : in FastAPI, It is a utility for testing FastAPI applications without needing to run a live server. this comes form `fastapi.testclient`

→ import the app to test file: `from main import app`  

→ create a client instance: `client = TestClient(app)`

→ to disable warning: `pytest --disable-warnings`

→ Setup Test Dependencies and Database: 

→ create a fake database that can store data.

→ create testing dependencies that are separate from our production dependencies.

→ This way we can do integration testing to make sure our entire project is working correctly when we run our tests. 

→ App is live  = production dependencies

→ App is testing = testing dependencies

→ A connection pool is a standard technique used to maintain long running connections in memory for efficient re-use.

→ create an engine and create session

→ How does FastAPI know that we are in testing environment:

→ client = TestcClient(app) instead of app = FastAPI()

→ We need to override dependency: ex: db_dependency, user_dependency

while testing: test for both cases: → if found and if not found. 

`pytest-asyncio`  →  *async def functions are not natively supported*  hence we use pytest-asyncio is a pytest plugin. It facilitates testing of code that uses the asyncio library. pytest-asyncio provides support for coroutines as test functions. This allows users to *await* code inside their tests.

to install `pytest-asyncio`:  `pip install pytest-asyncio`

@pytest.mark.asyncio   

Full Stack:

1. Jinja Templating
    1.  Jinja is Fast, Expressive and extensible templating language. 
    2. Able to write cide similar to python in the DOM
    3. The template is passed data to render within the final document
    4. Jinja tags are similar to HTML and helps working with backend data. 
    5. In jinja templating we can use for loop and if else statements
    6. to install `pip install jinja2`
    
2. aiofiles
    1.  it is an Apache2 licensed library. 
    2. used for handling local disk files in asyncio applications. 
    3. simple analogy is: we request for disk writing or reading, pushes it to background and notifies once its done. in the mean time we can handle other requests. 
    4. to install: `pip install aiofiles`
3. bootstrap:
    1. Bootstrap is a free front-end framework for faster and easier web development

To return a template, Jinja2Templates need to accept the requests. to handle that in fastapi, we use Request class of Fastapi.