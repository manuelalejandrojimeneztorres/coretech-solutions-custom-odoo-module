# CoreTech Solutions Custom Odoo Module

![Odoo](https://img.shields.io/badge/Odoo-18.0-32CD32?style=for-the-badge&logo=odoo)
![Docker Desktop](https://img.shields.io/badge/Docker-4.37.1-2A2D32?style=for-the-badge&logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-4169E1?style=for-the-badge&logo=postgresql)
![pgAdmin](https://img.shields.io/badge/pgAdmin-4-800080?style=for-the-badge&logo=postgresql)
![Adminer](https://img.shields.io/badge/Adminer-4.8.1-228B22?style=for-the-badge&logo=adminer)
![License](https://img.shields.io/badge/License-Apache%202.0-FF8C00?style=for-the-badge)
![Build Status](https://img.shields.io/github/actions/workflow/status/manuelalejandrojimeneztorres/coretech-solutions-custom-odoo-module/backend-ci.yml?style=for-the-badge)
![Coverage](https://img.shields.io/codecov/c/github/manuelalejandrojimeneztorres/coretech-solutions-custom-odoo-module?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-Up%20to%20date-brightgreen?style=for-the-badge)

## Description

The **CoreTech Solutions Custom Odoo Module** is a robust, enterprise-grade solution tailored for managing the distribution of electronic and IT components across CoreTech Solutions' global network of distribution centers. Designed with **Docker**, **PostgreSQL**, and tools like **pgAdmin** and **Adminer**, this module offers flexibility, security, and efficiency, ensuring seamless integration with Odoo 18.0.

---

## Table of Contents

1. [Key Features](#key-features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
   - [Project Setup](#project-setup)
   - [Environment Configuration](#environment-configuration)
   - [Starting Services](#starting-services)
4. [Custom Scripts](#custom-scripts)
5. [Makefile Commands](#makefile-commands)
6. [Security Practices](#security-practices)
   - [Environment Variables](#environment-variables)
   - [Docker Secrets](#docker-secrets)
7. [Technologies and Tools Used](#technologies-and-tools-used)
8. [Dependencies](#dependencies)
9. [Troubleshooting](#troubleshooting)
   - [Common Issues](#common-issues)
   - [Logs](#logs)
10. [Contributing Guidelines](#contributing-guidelines)
11. [Support](#support)
12. [License](#license)
13. [Acknowledgments](#acknowledgments)

---

## Key Features

- **Integrated Distribution Management**: Comprehensive tools for managing distribution networks.
- **Dockerized Setup**: Easy deployment and scalability using Docker.
- **Database Operations**: Reliable PostgreSQL integration with backup and restore functionality.
- **Web Interfaces**: Manage databases using **pgAdmin** and **Adminer**.
- **Customizable**: Flexible scripts and Makefile commands for developer convenience.

[🔼 Back to Top](#table-of-contents)

---

## Prerequisites

Ensure the following tools are installed:

- [Docker Desktop v4.37.1](https://www.docker.com/products/docker-desktop/) - Tool to develop, create and manage Docker containers.
- [WSL v2](https://learn.microsoft.com/en-us/windows/wsl/) - Feature that allows running Linux distributions inside Windows.
- [Ubuntu v24.04.1 (Noble Numbat)](https://releases.ubuntu.com/24.04/) - Popular and easy to use Linux distribution.

[🔼 Back to Top](#table-of-contents)

---

## Installation

### Project Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/manuelalejandrojimeneztorres/coretech-solutions-custom-odoo-module.git
   ```

2. Navigate to the project directory:

   ```bash
   cd coretech-solutions-custom-odoo-module
   ```

[🔼 Back to Top](#table-of-contents)

### Environment Configuration

1. Create a `.env` file in the root directory based on `.env.example`:

   ```env
   # Database configuration
   HOST=db
   PORT=5432
   USER=odoo
   POSTGRES_USER=odoo
   PASSWORD=your_password_here
   POSTGRES_PASSWORD=your_password_here
   POSTGRES_DB=postgres
   PGDATA=/var/lib/postgresql/data/pgdata

   # pgAdmin configuration
   PGADMIN_DEFAULT_EMAIL=your_email_here@example.com
   PGADMIN_DEFAULT_PASSWORD=your_password_here
   ```

> [!IMPORTANT]
> `HOST`: The address of the postgres server. If you used a postgres container, set to the name of the container. Defaults to `db`.
> `PORT`: The port the postgres server is listening to. Defaults to `5432`.
> `USER`: The postgres role with which Odoo will connect. If you used a postgres container, set to the same value as `POSTGRES_USER`. Defaults to `odoo`.
> `POSTGRES_USER`: The postgres role used for the postgres container. This should match the value of `USER`. Defaults to `odoo`.
> `PASSWORD`: The password of the postgres role with which Odoo will connect. If you used a postgres container, set to the same value as `POSTGRES_PASSWORD`. Defaults to `odoo`.
> `POSTGRES_PASSWORD`: The password of the postgres role used for the postgres container. Defaults to `odoo`.
> `POSTGRES_DB`: The name of the default database used by the postgres container. Defaults to `postgres`.
> `PGDATA`: The directory where PostgreSQL stores data. Defaults to `/var/lib/postgresql/data/pgdata`.
> `PGADMIN_DEFAULT_EMAIL`: The default email address for pgAdmin. Set this to your desired email address. Example: `your_email_here@example.com`.
> `PGADMIN_DEFAULT_PASSWORD`: The default password for pgAdmin. Set this to your desired password. Example: `your_password_here`.

[🔼 Back to Top](#table-of-contents)

### Starting Services

1. Use the `run.sh` script or the `make up` command to build and start the containers:

   ```bash
   bash scripts/run.sh
   ```

   or

   ```bash
   make up
   ```

2. Access services:
   - **Odoo**: [http://localhost:8069](http://localhost:8069)
   - **PostgreSQL**: [http://localhost:5432](http://localhost:5432)
   - **Adminer**: [http://localhost:8080](http://localhost:8080)
   - **pgAdmin**: [http://localhost:15080](http://localhost:15080)

> [!TIP]
> If you encounter an error indicating that a port configured for one of the services in `docker-compose.yml` is already in use, it means that another process on your system is occupying that port. Refer to the [Troubleshooting](#troubleshooting) section for detailed steps to resolve the issue.

[🔼 Back to Top](#table-of-contents)

---

## Custom Scripts

### `run.sh`

- Builds and starts containers.
- Creates necessary directories for logs.

### `stop.sh`

- Stops all services and removes orphaned containers.

### `backup.sh`

- Creates a backup of the PostgreSQL database.

### `restore.sh`

- Restores a PostgreSQL database from a backup file.

[🔼 Back to Top](#table-of-contents)

---

## Makefile Commands

### `build`

- Builds Docker containers.

  ```bash
  make build
  ```

### `up`

- Starts Docker containers in detached mode.

  ```bash
  make up
  ```

### `down`

- Stops and removes Docker containers.

  ```bash
  make down
  ```

### `logs`

- Displays real-time logs from containers.

  ```bash
  make logs
  ```

### `backup`

- Runs the backup script.

  ```bash
  make backup
  ```

### `restore`

- Runs the restore script.

  ```bash
  make restore
  ```

[🔼 Back to Top](#table-of-contents)

---

## Security Practices

### Environment Variables

Store sensitive data using environment variables. Examples:

- `HOST`: Database host (default: `db`).
- `PORT`: Database port (default: `5432`).
- `USER`: PostgreSQL user for Odoo (default: `odoo`).
- `PASSWORD`: PostgreSQL password (to be set by the user).

> [!WARNING]
> Ensure that the file containing the environment variables (e.g., the `.env` file) is not accidentally included in your repository. If you are using version control, exclude the `.env` file by adding it to your `.gitignore` file: `echo ".env" >> .gitignore`.

[🔼 Back to Top](#table-of-contents)

### Docker Secrets

1. Create a `secrets/` directory:

   ```bash
   mkdir secrets
   ```

2. Add secrets:

   ```bash
   echo "your-odoo-postgres-password" > secrets/odoo_pg_pass
   echo "your-pgadmin-default-password" > secrets/pgadmin_default_password
   ```

3. Initialize Docker Swarm:

   ```bash
   docker swarm init
   ```

4. Create secrets:

   ```bash
   docker secret create odoo_pg_pass secrets/odoo_pg_pass
   docker secret create pgadmin_default_password secrets/pgadmin_default_password
   ```

5. Secure secrets directory:

   ```bash
   chmod 600 secrets/*
   ```

> [!WARNING]
> Ensure that the directory containing the secrets (e.g., the `secrets/` directory) is not accidentally included in your repository. If you are using version control, exclude the `secrets/` directory by adding it to your `.gitignore` file: `echo "secrets" >> .gitignore`.

[🔼 Back to Top](#table-of-contents)

---

## Technologies and Tools Used

- **Backend**:
  - Odoo: Open-source ERP framework for business applications
  - Python: Core programming language for Odoo modules

- **Deployment**:
  - Docker: Containerization for consistent environments
  - Docker Compose: Multi-container orchestration

- **Database**:
  - PostgreSQL: Advanced relational database

- **Development Tools**:
  - Visual Studio Code: Code editor
  - Adminer: Lightweight database management interface
  - pgAdmin: Database management tool
  - Docker CLI: Command-line interface for Docker

[🔼 Back to Top](#table-of-contents)

---

## Dependencies

Key dependencies include:

- **Odoo v18.0**: Open-source ERP framework for building and customizing business applications.
- **Docker Desktop v4.37.1**: Desktop application for managing Docker containers and images on macOS and Windows.
- **Docker Compose v2.32.4**: Tool for defining and running multi-container Docker applications.
- **Docker Swarm**: Native clustering and orchestration tool for managing Docker containers across multiple hosts.
- **WSL v2**: Windows Subsystem for Linux, enabling a full Linux kernel on Windows for Docker and other tools.
- **Ubuntu v24.04.1 (Noble Numbat)**: Linux distribution for the host environment, providing compatibility and stability for server-side applications.
- **PostgreSQL v17**: Relational database management system used by Odoo.
- **pgAdmin v4**: Web-based interface for managing PostgreSQL databases.
- **Adminer v4.8.1**: Lightweight database management tool supporting multiple database systems, including PostgreSQL.
- **Python v3.13.1**: Programming language for running Odoo and managing various scripts and automation tasks.
- **Git v2.48.1**: Distributed version control system for tracking changes in source code during software development.

> [!NOTE]
> For a full list of dependencies and services, see the `requirements.txt` file and `docker-compose.yml`.

[🔼 Back to Top](#table-of-contents)

---

## Troubleshooting

### Common Issues

- **Odoo Container Not Starting**:
  - Verify that the Docker daemon is running.
  - Ensure the `docker-compose.yml` file is correctly configured.

- **Database Connection Errors**:
  - Check the `db` service in `docker-compose.yml`.
  - Ensure PostgreSQL credentials match those in the Odoo configuration.

- **Module Not Loading**:
  - Ensure the module directory is correctly mapped in the `addons_path`.
  - Check the Odoo logs for detailed error messages.

- **Port Already in Use**:
  - Identify which process is using the port:

    - On Linux or macOS:

      ```bash
      lsof -i :<port-number>
      ```

    - On Windows (PowerShell):

      ```bash
      netstat -aon | findstr :<port-number>
      ```

  - Stop the conflicting process or change the port in the `docker-compose.yml` file:

    ```yaml
    ports:
      - "<new-port>:<container-port>"
    ```

  - Save the changes and restart the services using the appropriate script or command:

    - Stop the services:

      ```bash
      bash scripts/stop.sh
      ```

      or

      ```bash
      make down
      ```

    - Start the services:

      ```bash
      bash scripts/run.sh
      ```

      or

      ```bash
      make up
      ```

[🔼 Back to Top](#table-of-contents)

### Logs

Use the following commands to view logs:

- **Odoo Logs**:

  ```bash
  docker-compose logs odoo
  ```

- **Database Logs**:

  ```bash
  docker-compose logs db
  ```

[🔼 Back to Top](#table-of-contents)

---

## Contributing Guidelines

We welcome contributions to improve the CoreTech Solutions Custom Odoo Module. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes with detailed messages:

   ```bash
   git commit -m "Add: Description of your feature"
   ```

4. Push your branch and open a pull request.

> [!NOTE]
> For guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

[🔼 Back to Top](#table-of-contents)

---

## Support

For any issues, please contact **CoreTech Solutions** at [support@coretechsolutions.com](mailto:support@coretechsolutions.com).

[🔼 Back to Top](#table-of-contents)

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE.txt](LICENSE.txt) file for more details.

[🔼 Back to Top](#table-of-contents)

---

## Acknowledgments

Special thanks to:

- The [Odoo](https://www.odoo.com/) community for providing a powerful and extensible framework.
- [Docker](https://www.docker.com/) for streamlining containerization and deployment processes.
- [PostgreSQL](https://www.postgresql.org/) for its reliability as a database solution.
- [GitHub](https://github.com/) for enabling seamless collaboration and version control.

[🔼 Back to Top](#table-of-contents)

---

Enjoy using the **CoreTech Solutions Custom Odoo Module** and feel free to contribute to its development! 🚀

[🔼 Back to Top](#table-of-contents)
