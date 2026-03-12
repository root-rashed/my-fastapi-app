<div align="center">

# ⚡ my-fastapi-app

### A blazing-fast, modern REST API built with FastAPI & Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4c1130?style=for-the-badge)](https://www.uvicorn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> _High-performance asynchronous API — auto-documented, production-ready, and built for scale._

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
- [API Documentation](#-api-documentation)
- [Development in VS Code](#-development-in-vs-code)
- [Environment Variables](#-environment-variables)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Overview

**my-fastapi-app** is a lightweight yet powerful REST API built with [FastAPI](https://fastapi.tiangolo.com/) — one of the fastest Python web frameworks available. It features automatic OpenAPI documentation, async request handling, and a clean, scalable architecture designed for real-world applications.

Whether you're prototyping a new idea or building a production microservice, this project gives you a solid foundation to launch from.

---

## 🛠 Tech Stack

| Layer        | Technology                          |
|--------------|--------------------------------------|
| Language     | Python 3.10+                        |
| Framework    | FastAPI                             |
| Server       | Uvicorn (ASGI)                      |
| Validation   | Pydantic v2                         |
| Docs         | Swagger UI / ReDoc (auto-generated) |
| IDE          | Visual Studio Code                  |

---

## 📁 Project Structure

```
my-fastapi-app/
│
├── main.py                  # Application entry point & route definitions
├── fastapi-quickstart.txt   # Quick reference notes
├── requirements.txt         # Python dependencies (add this)
├── .env                     # Environment variables (do NOT commit)
├── .gitignore
└── README.md
```

> As the project grows, consider organizing routes into `routers/`, models into `models/`, and database logic into `db/`.

---

## 🏁 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)
- [VS Code](https://code.visualstudio.com/) _(recommended)_

---

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/root-rashed/my-fastapi-app.git
cd my-fastapi-app
```

**2. Create a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install fastapi uvicorn
```

> Or if you have a `requirements.txt`:
> ```bash
> pip install -r requirements.txt
> ```

---

### Running the Server

```bash
uvicorn main:app --reload
```

| Flag       | Description                                  |
|------------|----------------------------------------------|
| `--reload` | Auto-restarts on code changes (dev mode)     |
| `--port`   | Specify a custom port (default: `8000`)      |
| `--host`   | Bind to a specific host (default: `127.0.0.1`) |

The API will be live at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI generates beautiful interactive documentation automatically. Once the server is running, visit:

| Interface   | URL                                          |
|-------------|----------------------------------------------|
| Swagger UI  | http://127.0.0.1:8000/docs                  |
| ReDoc       | http://127.0.0.1:8000/redoc                 |
| OpenAPI JSON| http://127.0.0.1:8000/openapi.json          |

---

## 💻 Development in VS Code

For the best development experience in VS Code:

**1. Install recommended extensions:**

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) — language support & IntelliSense
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) — fast type checking
- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) — test API endpoints directly in VS Code
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) — enhanced Git features

**2. Select the Python interpreter:**

Press `Ctrl+Shift+P` → `Python: Select Interpreter` → choose your `venv`.

**3. Run with the integrated terminal:**

```bash
uvicorn main:app --reload
```

**4. Debug with VS Code:**

Create a `.vscode/launch.json` file:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI Debug",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["main:app", "--reload"],
      "jinja": true
    }
  ]
}
```

Then press `F5` to start debugging with breakpoints.

---

## 🔐 Environment Variables

Create a `.env` file in the root directory for sensitive configuration:

```env
APP_NAME=my-fastapi-app
APP_VERSION=1.0.0
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./app.db
```

> ⚠️ **Never commit your `.env` file to version control.** Add it to `.gitignore`.

Load variables in your app using `python-dotenv`:

```bash
pip install python-dotenv
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get involved:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Built with ❤️ by [root-rashed](https://github.com/root-rashed)

⭐ If this project helped you, please consider giving it a star!

</div>
