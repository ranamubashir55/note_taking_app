# Note Taking Application with Langchain

Welcome to the Note Taking Application! This application allows you to create, read, update, and delete notes. Additionally, it leverages Langchain to generate summaries for your notes using Large Language Models.

## Project Setup Guide

### Prerequisites

Before you start, make sure your system meets the following requirements:

- Docker installed with docker-compose
- OpenAI secret key (at least Tier 1, as the free tier may result in rate limit exceeded errors)

### How to Run the App

1. Move into the directory `note_taking_app/`
2. Add your OpenAI Secret key in the file `.env` located at path `note_taking_app/.env`

2. Run the FastAPI server with the following command:
    ```bash
    docker-compose up --build
    ```

3. Open your browser and visit the Swagger page at [http://localhost:5000/docs](http://localhost:5000/docs).

4. Perform CRUD operations by making API calls using the Swagger interface.

5. To create notes summary:
    - Make a POST request to [http://localhost:5000/notes/](http://localhost:5000/notes/) and set the `create_summary` parameter to true.
    - In response, it will return the note summary.

Now you're all set to interact with the application! If you encounter any issues, double-check the prerequisites and steps above.

**Note:** For Langchain implementation explanation, please visit the file named `lanchain_imp_explanation.txt`.
