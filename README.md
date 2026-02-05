# CI/CD Pipeline – URL Mini Shortener

This repository uses **GitHub Actions** to implement a complete CI/CD pipeline for the **URL Mini Shortener** application.  
The pipeline automates code quality checks, security scans, Docker image builds, and pushes images to Docker Hub on every push to the `main` branch.

---

## 📌 Pipeline Overview

The CI/CD pipeline performs the following tasks:

1. **Trigger**
   - Runs automatically on every push to the `main` branch.

2. **Code Checkout**
   - Fetches the latest source code from the repository.

3. **Python Setup**
   - Sets up Python **3.11** for dependency installation and analysis.

4. **Dependency Installation**
   - Installs required Python dependencies from:
     ```
     app/requirements.txt
     ```

5. **Versioning**
   - Generates:
     - A short Git commit SHA
     - A version number based on commit count  
   - Version format:
     ```
     v<commit-count>
     ```

6. **Static Code Analysis (SonarQube)**
   - Scans the application source code using **SonarQube**
   - Analyzes:
     - Code quality
     - Bugs and vulnerabilities
     - Maintainability issues

7. **Docker Image Build**
   - Builds a Docker image for the application.
   - Tags the image with:
     - Generated version (e.g. `v15`)
     - `latest`

### 🔒 **Container Security Scan (Trivy)**
Scans the Docker image for:
- OS-level vulnerabilities
- Library vulnerabilities
Reports HIGH and CRITICAL issues.

### 🔐 **Docker Hub Authentication**
Logs in securely using GitHub Secrets.

### 📤 **Docker Image Push**
Pushes both versioned and `latest` images to Docker Hub.

---

## 🛠️ Technologies Used

- **GitHub Actions** – CI/CD automation
- **Python 3.11** – Application runtime
- **Docker** – Containerization
- **SonarQube** – Static code analysis
- **Trivy** – Container vulnerability scanning
- **Docker Hub** – Image registry

---

## 🔐 Required GitHub Secrets

The following secrets must be configured in your repository:

| Secret Name | Description |
|-------------|-------------|
| `SONAR_TOKEN` | SonarQube authentication token |
| `SONAR_HOST_URL` | SonarQube server URL |
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub password or access token |

---

## 🧪 SonarQube Configuration

- **Project Key**: `url-mini`
- **Project Name**: URL Mini Shortener
- **Source Directory**: `app`
- **Python Version**: 3.11

---

## 🐳 Docker Image Details

**Repository**:
```txt
sachinviru/url-mini


