# FastAPI Project

This is a FastAPI-based project that utilizes Docker and Alembic for database migrations.

## Prerequisites

Make sure you have the following installed on your system:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to set up and run the project:

### 1. Clone the Repository
```sh
git clone <repository-url>
cd <repository-name>
```

### 2. Switch to the Development Branch (Always Up to Date)
```sh
git checkout dev
```
The `dev` branch always contains the latest updates and bug fixes, ensuring you are working with the most recent version of the project.

### 3. Set Up Environment Variables
Rename the `.env.example` file to `.env` and modify any necessary variables.
```sh
mv .env.example .env
```

### 4. Build and Run the Docker Containers
Run the following command to build and start the containers:
```sh
docker-compose up --build
```

### 5. Apply Database Migrations
Once the containers are running, execute the following command inside the `app-1` container:
```sh
alembic upgrade head
```

### 6. Verify the API
Open your browser and navigate to:
```
http://127.0.0.1:8000/docs
```
This will open the interactive API documentation (Swagger UI) where you can check the endpoints.


### 7. Run Tests  
Execute the following command to run the tests:  
```sh
python -m pytest tests
```  
