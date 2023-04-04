# This app can analyze text and provide words frequencies and English translations!

## introduction

When learning a language, don't you think it's important to know how often certain vocabulary is used in a particular genre of text? For example, studying vocabulary with high frequency of occrence in the field of economics would be more efficient. 

### Feature

So, this app provides users with the frequency of vocabulary and its English translations in Japanese text entered by user.

- Vocabulary Frequency Analysis: Easily obtain the frequency of vocabulary in a text using the `get_vovabulary_frequency function.
- English Translation Retrieval: In addition to obtaining the frequency of vocabulary, users can also retrieve the English translations of the vocabulary.


https://user-images.githubusercontent.com/92550379/227063434-79c77ddf-aa32-4e2d-a3c1-a10f2ae758a5.mp4



### Getting started

Before setup, please install Visual Studio Code[^1], PostgreSQL[^2], and Python[^3]. Installing the Python extension in Visual Studio Code allows you to use Python within the IDE, which is very convenient.

[^1]:Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux, and macOS. It is a popular tool for developers due to its lightweight design and wide range of features, such as debugging, code navigation, and extension support.

[^2]:PostgreSQL is a powerful open-source relational database management system known for its stability, scalability, and extensibility. Developed in the 1980s, it's free to use and runs on multiple operating systems. Its key features include ACID transaction support, advanced indexing, and query optimization.

[^3]:Python was first released in 1991 by Guido van Rossum and has since become one of the most popular programming languages in use today. It's used for a wide range of applications, including web development, data analysis, artificial intelligence, scientific computing, and more.

## Installation of backend

### 1. Clone the repository

```
https://github.com/Takahiro9-Murakami9/Japanese-frequency.git
```

### 2. Navigate to the project's backend and create a new virtual environment:

```
cd .\backend\
pipenv shell
```

### 3. Install the necessary dependencies:

```
pipenv install
```

## Configuration

### 1. Create a new database:

```
sudo -u postgres createdb your_database_name
```

### 2. Make a .flaskenv file:

```
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=1
DATABASE_URL=postgresql://postgres:your_postgresql's_password@localhost/your_database_name
```

##　Database Migrations

This application uses Flask-Migrate to manage database migrations.

Before running the application for the first time, you will need to create the database tables by running the following command:

```
flask db init
flask db migrate
flask db upgrade
```

The `flask db init`command initialize the migrations directory. You only need to run this command once.

The`flask db migrate` command generates a new migration script based on the changes you've made to the models in your application.

The `flask db upgrade` command applies the changes in the migration script to the database.

After the initial setup, you only need to run the following commands to apply any new changes to the database:

```
flask db migrate
flask db upgrade
```

## Installation of frontend

### 1. Navigate to the project's frontend:

```
cd .\frontend\

```

### 2. Install the necessary dependencies:

```
npm install
```

## Starting up the ASpplication

To run this application, you will need to start both the frontend and backend sever.
Follow the instrucitons below to get started.

### Starting up the Flask Backend Server

1. Open a new terminal window.
2. Navigate to the `backend` directory of the project.
3. Activate the virtual environment by running the following command:

```
pipenv shell
```
4. Run the following command to start the backend server:

```
flask run
```
5. The backend server should now be running on `http://localhost:5000`.

### Starting up the Frontend Server

1. Open a new terminal window.
2. Navigate to the `frontend` directory of the project.
3. Run the following command to start the frontend server:

```
npm start
```
This will start the frontend server on port 3000 by default. If you want use a different port number, you can specify it as an environment variable before running the `start` command. For example, to start the frontend server on port 8080, you can run the following command:

```
PORT=8080 npm start
```
4. The frontend server should now be running on `http://localhost:3000` (or the port number you specified).

Note: If the frontend server fails to start due to a port conflict, you may need to change the port number in the start script defined in your package.json file.

Congratulations! You have now started up both the frontend and backend servers for this web application. You should now be able to access the web application by visiting http://localhost:3000 (or the port number you specified) in your web browser.
