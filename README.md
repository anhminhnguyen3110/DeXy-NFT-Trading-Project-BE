# DeXy Platform - NFT Trading Backend

## Overview

Welcome to the DeXy platform backend repository! DeXy is a platform designed for trading Non-Fungible Tokens (NFTs). This README provides an overview of the backend structure and implementation details.

## Features

- **FastAPI Framework**: Utilizes the FastAPI framework for building high-performance APIs with Python.
- **Layered Architecture**: Implements a scalable architecture with separate layers for controller, service, model, entity, and repository.
- **Best Practices**: Adheres to best practices for structuring code, ensuring maintainability, scalability, and ease of feature management.

## Structure

The backend follows a structured approach with the following layers:

- **Controllers**: Handles incoming requests, validates input, and orchestrates interactions between different layers.
- **Services**: Implements business logic, performs data processing, and interacts with repositories.
- **Models**: Defines data models and schema for the application.
- **Entities**: Represents domain entities, encapsulating business logic and behavior.
- **Repositories**: Manages data storage and retrieval, interacts with the database or external data sources.

## Technologies Used

- **Python**: Primary programming language.
- **FastAPI**: Web framework for building APIs with Python.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite/PostgreSQL/MySQL**: Database options for storing application data.

## Getting Started

To get started with the DeXy platform backend:

1. Clone this repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt`.
3. Configure database settings in `config.py`.
4. Run the backend server using `uvicorn main:app --reload`.
