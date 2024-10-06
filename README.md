# Jolly-Chimp

Jolly-Chimp is a web-monitor application that provides real-time information on various services, websites, and public APIs. It allows you to keep track of the status of your websites and monitor your services.

## Features

 - **Website Monitoring**: Displays the current status of all your websites with uptime and response time metrics.
 - **Service Monitoring**: Monitors the health of various internal services and displays their current status.

## Technologies Used

 - **Frontend**: [React](https://reactjs.org/) with [Vite](https://vitejs.dev/) and [TypeScript](https://www.typescriptlang.org/) for fast, type-safe development.
 - **Backend (API)**: [FastAPI](https://fastapi.tiangolo.com/) with [Python](https://www.python.org/) for serving the API endpoints.
 - **Database**: [MySQL](https://www.mysql.com/) for persistent storage.
 - **Other Tools**:
    - [Axios](https://axios-http.com/) for making HTTP requests from the frontend.
    - [React Query](https://tanstack.com/query/v4/docs/framework/react/overview) for managing API state and caching on the frontend.
    - [Docker](https://www.docker.com/) for containerized deployment and scalability.

## Getting Started

### Prerequisites

 - **Docker** (Ensure you have Docker and Docker Compose installed)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/N1borg/Jolly-Chimp.git
    cd Jolly-Chimp
    ```

2. Install dependencies:

    You will need an `.env` file and configure it with your specific credentials and settings. Copy the example environment file:

    ```bash
    cp .env.example .env
    ```

    Make sure the `.env` files contain information like API keys, database connection strings, etc.

3. Configure the scraper:

    Copy the example configuration file for the scraper and adjust it according to your requirements:

    ```bash
    cp scraper/config.json.example scraper/config.json
    ```

    Ensure the `config.json` file contains the necessary settings for the scraper to function correctly.

4. Build and start the containers using Docker Compose:

    ```bash
    docker compose up --build
    ```

    This will pull the necessary Docker images and run both the frontend and backend services in separate containers.

### Running the App

After running the `docker compose` command, your app should be live. The default setup exposes the services at:

 - **Frontend (React)**: `http://localhost:3000`
 - **Backend (FastAPI)**: `http://localhost:8000`

You can interact with the FastAPI docs at `http://localhost:8000/docs` to test the API.

![Ian Insanity GIF](https://media1.tenor.com/m/zWMb9NKhylgAAAAd/ian-insanity.gif)
