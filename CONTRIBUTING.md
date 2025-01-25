# Contributing to CoreTech Solutions Custom Odoo Module

Thank you for your interest in contributing to the **CoreTech Solutions Custom Odoo Module** project! We value your input and expertise, and we are committed to fostering an open, inclusive, and collaborative environment. This document provides guidelines to ensure contributions are efficient, professional, and aligned with our project's goals.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
   - [Reporting Issues](#reporting-issues)
   - [Feature Requests](#feature-requests)
   - [Submitting Code Changes](#submitting-code-changes)
3. [Development Workflow](#development-workflow)
4. [Style Guidelines](#style-guidelines)
5. [Pull Request Process](#pull-request-process)
6. [Resources](#resources)
7. [Support](#support)

---

## Code of Conduct

All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the standards of behavior expected when contributing to this project.

---

## How to Contribute

### Reporting Issues

If you encounter a bug or an issue, please:

1. Check the [existing issues](https://github.com/manuelalejandrojimeneztorres/coretech-solutions-custom-odoo-module/issues) to avoid duplicates.
2. If the issue is new, create a detailed report including:
   - Steps to reproduce the issue.
   - Expected behavior.
   - Actual behavior.
   - Screenshots or logs, if applicable.

### Feature Requests

We welcome suggestions to improve the project! To propose a new feature:

1. Open a [feature request issue](https://github.com/manuelalejandrojimeneztorres/coretech-solutions-custom-odoo-module/issues/new).
2. Include a detailed description of the feature and its benefits.

### Submitting Code Changes

We accept contributions in the form of:

- Bug fixes
- New features
- Documentation improvements

Before submitting changes, ensure you:

1. Discuss the proposed change via an issue.
2. Follow the [Style Guidelines](#style-guidelines).
3. Test your changes thoroughly.

---

## Development Workflow

### Prerequisites

Ensure you have the following installed:

- **Backend**: Python, Odoo framework, PostgreSQL, WSL, and Docker.
- **Database Tools**: Adminer or pgAdmin for database management.

### Setup

1. Fork the repository.
2. Clone your fork:

   ```bash
   git clone https://github.com/your-username/coretech-solutions-custom-odoo-module.git
   ```

3. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Install dependencies (e.g., Python libraries or Docker images) based on the project requirements.

### Running the Application

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

---

## Style Guidelines

### Code Formatting

- Adhere to [Python's PEP 8 style guide](https://peps.python.org/pep-0008/).
- Use descriptive and meaningful variable, method, and class names.

### Naming Conventions

- Use `snake_case` for variables and functions.
- Use `PascalCase` for classes.
- Ensure all names reflect the purpose clearly.

### Commit Messages

- Begin with a verb (e.g., "Add," "Fix," "Update").
- Keep messages concise but informative.

Example:

```bash
Fix: Database connection issue in Docker setup
```

---

## Pull Request Process

1. Ensure your branch is up to date with the `main` branch:

   ```bash
   git pull origin main
   ```

2. Push your branch to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

3. Open a pull request:
   - Provide a clear description of your changes.
   - Link any related issues.

4. Address any requested changes promptly.

---

## Resources

- [Project Documentation](https://github.com/manuelalejandrojimeneztorres/coretech-solutions-custom-odoo-module/wiki)
- [Odoo Framework Documentation](https://www.odoo.com/documentation/18.0/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

---

## Support

For questions or assistance, please reach out via:

- **Email**: support@coretechsolutions.com
- **GitHub Issues**: [CoreTech Solutions Custom Odoo Module Issues](https://github.com/manuelalejandrojimeneztorres/coretech-solutions-custom-odoo-module/issues)

We appreciate your contributions and look forward to collaborating with you!
