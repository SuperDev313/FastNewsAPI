# FastAPI News API

This project is a simple API built with FastAPI that interacts with the GNews API to fetch news articles based on different parameters.

## Features

- Fetch top news articles.
- Search for news articles by keyword.
- Retrieve news articles by specific criteria (e.g., title, author).

## Prerequisites

Before running this project, you need to have the following installed:

- Python 3.12
- Poetry

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/fast-news-api.git
2. Navigate to the project directory:
   ```
   cd fast-news-api
3. Install dependencies using Poetry:
   ```
   poetry install

## Configuration
1. Obtain an API key from GNews API.
2. Create a .env file in the root directory of the project:

   ``` GNEWS_API_KEY="YOUR_GNEWS_API_KEY_HERE"
   Replace YOUR_GNEWS_API_KEY_HERE with your actual GNews API key.



## Usage
   ```Run the FastAPI application using uvicorn:
   poetry run uvicorn fastnewsapi.main:app --reload
   The API server will start locally at http://localhost:8000.

   Endpoints
   / : Root endpoint that displays a welcome message.
   /articles/ : Fetches news articles. Optional query parameters include q (keyword), lang (language), and max_results (maximum number of articles).

   Access the Swagger API documentation by visiting http://localhost:8000/docs in your web browser.

   