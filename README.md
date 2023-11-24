# Note Taking Application.
Note Taking Application with langchain for creating the notes summary using LLM.

# Project Setup Guide

## Prerequisites

Before you start, ensure that your system meets the following requirements:

- Python version **3.10** or higher is installed.
- PostgreSQL database is installed on your system.

## How to Run the App

Follow these steps to set up and run the application:

1. **Create a database named `note_taking`.**
2. **Navigate to the project directory where the `requirements.txt` file is located.**
3. **Install the required libraries by running the command:**
    ```
    pip install -r requirements.txt
    ```

4. **Update the `.env` file in the project directory with the following changes:**
   - Add the PostgreSQL database URL.
   - Add the OpenAPI secret key (ensure the key belongs to Tier 1 to avoid rate limit issues).

5. **Move into the `note_taking_app/app` directory.**

6. **Launch the FastAPI server using the command:**
    ```
    uvicorn app.main:app
    ```

7. **Open your browser and visit the Swagger page at [http://localhost:8000/docs](http://localhost:8000/docs).**

8. **Perform CRUD operations by making API calls using the Swagger interface.**
9. **To create notes summary:**
   Make a POST request to [http://localhost:8000/notes/](http://localhost:8000/notes/) and set the `create_summary` parameter to true. In response it will return the note summary.

Now you're all set to interact with the application! If you encounter any issues, double-check the prerequisites and steps above.

**Note**: For Langchain implementation explanation please visit the file named. `lanchain_imp_explanation.txt`