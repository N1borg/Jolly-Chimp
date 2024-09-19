# Jolly-Chimp

Jolly-Chimp is a web-monitor application that provides real-time information on various services, websites, and public APIs. It allows you to keep track of the status of your websites, monitor your services, check train schedules for specific routes, and view the operating hours of public trash facilities via an API.

## Features

- **Website Monitoring**: Displays the current status of all your websites with uptime and response time metrics.
- **Service Monitoring**: Monitors the health of various internal services and displays their current status.
- **Train Schedules**: Shows the next available trains for a given route using real-time train scheduling APIs.
- **Public Trash API**: Displays the operating hours for public trash facilities, keeping you informed about waste management services in your area.

## Technologies Used

- **Frontend**: [React](https://reactjs.org/) with [Vite](https://vitejs.dev/) and [TypeScript](https://www.typescriptlang.org/) for fast, type-safe development.
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) with [Python](https://www.python.org/) for serving the API endpoints.
- **Database**: [MySQL](https://www.mysql.com/) for persistent storage.
- **Authentication**: [JWT](https://jwt.io/) for secure token-based authentication.
- **Other Tools**:
  - [Axios](https://axios-http.com/) for making HTTP requests from the frontend.
  - [React Query](https://tanstack.com/query/v4/docs/framework/react/overview) for managing API state and caching on the frontend.
  - [Docker](https://www.docker.com/) for containerized deployment and scalability.

## Getting Started

### Prerequisites

 - **Docker** (Ensure you have Docker and Docker Compose installed)
 - **NPM** or Yarn (for managing frontend dependencies)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/N1borg/Jolly-Chimp.git
    cd Jolly-Chimp
    ```

2. Install dependencies:

    You will need environment files for both the frontend and backend. Copy the example .env files and configure them with your specific credentials and settings:

    ```bash
    cp backend/.env.example backend/.env
    cp frontend/.env.example frontend/.env
    ```

    Make sure the .env files contain information like API keys, database connection strings, etc.

3. Build and start the containers using Docker Compose:

    ```bash
    docker-compose up --build
    ```

    This will pull the necessary Docker images and run both the frontend and backend services in separate containers.

### Running the App

After running the `docker-compose` command, your app should be live. The default setup exposes the services at:

 - **Frontend (React)**: `http://localhost:3000`
 - **Backend (FastAPI)**: `http://localhost:8000`

You can interact with the FastAPI docs at `http://localhost:8000/docs` to test the API.

![Ian Insanity GIF](https://media1.tenor.com/m/zWMb9NKhylgAAAAd/ian-insanity.gif)