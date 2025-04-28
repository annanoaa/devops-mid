# DevOps Midterm Project

This project demonstrates a simplified DevOps pipeline using local resources. It includes a small web application with automated testing, CI/CD, and Infrastructure as Code components.

## Project Overview

This project implements a complete DevOps workflow with:
- A simple Flask web application
- Version control with Git
- Continuous Integration with GitHub Actions
- Infrastructure as Code using Terraform and Ansible
- Blue/Green deployment strategy
- Health checks and monitoring
- Rollback mechanism

## Tools and Technologies

- **Web Application**: Flask (Python)
- **Version Control**: Git and GitHub
- **CI/CD**: GitHub Actions
- **Infrastructure as Code**: 
  - Terraform for infrastructure provisioning
  - Ansible for configuration management and deployment
- **Monitoring**: Simple Python-based health check script
- **Deployment Strategy**: Blue/Green deployment

## Project Structure

```
.
├── app.py                  # Flask application
├── templates/              # HTML templates
│   ├── index.html          # Home page with form
│   └── result.html         # Result page
├── test_app.py             # Unit tests
├── main.tf                 # Terraform configuration
├── deploy.yml              # Ansible playbook
├── health_check.py         # Health check script
├── rollback.sh             # Rollback script
├── requirements.txt        # Python dependencies
├── .github/workflows/      # GitHub Actions
│   └── ci-cd.yml           # CI/CD pipeline
└── deploy/                 # Deployment directories
    ├── blue/               # Blue environment
    ├── green/              # Green environment
    └── active_env.txt      # Tracks active environment
```

## CI/CD Pipeline Explanation

1. **Continuous Integration**:
   - Automated tests run on every push to main and dev branches
   - GitHub Actions pipeline runs tests and reports results

2. **Continuous Deployment**:
   - After successful tests, the deployment step is triggered
   - Terraform creates necessary infrastructure (directories)
   - Ansible deploys the application to the inactive environment
   - Health checks verify the deployment
   - If successful, the active environment is switched

3. **Blue/Green Deployment**:
   - Two identical environments (blue and green)
   - Only one is active at a time
   - New deployments go to the inactive environment
   - Switch happens only after successful health checks
   - Minimizes downtime and allows easy rollbacks

## How to Use This Project

### Prerequisites

- Python 3.8+
- Terraform
- Ansible
- Git

### Setup and Run

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd devops-midterm
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run tests**:
   ```
   pytest
   ```

4. **Initialize Terraform**:
   ```
   terraform init
   terraform apply
   ```

5. **Deploy with Ansible**:
   ```
   ansible-playbook deploy.yml
   ```

6. **Run the application**:
   ```
   cd deploy/$(cat deploy/active_env.txt)
   flask run
   ```

7. **Perform a rollback if needed**:
   ```
   ./rollback.sh
   ```

## Workflow Diagram

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│             │         │             │         │             │
│  Developer  │───┬────▶│     Git     │────────▶│   GitHub    │
│             │   │     │             │         │  Actions    │
└─────────────┘   │     └─────────────┘         └──────┬──────┘
                  │                                    │
                  │                                    │ Tests Pass
                  │                                    ▼
┌─────────────┐   │     ┌─────────────┐         ┌─────────────┐
│             │   │     │             │         │             │
│  Rollback   │◀──┴─────│ Blue/Green  │◀────────│  Terraform  │
│  Script     │         │ Deployment  │         │  & Ansible  │
└─────────────┘         └─────────────┘         └─────────────┘
                               ▲
                               │
                        ┌──────┴──────┐
                        │             │
                        │Health Check │
                        │             │
                        └─────────────┘
```

## Screenshots

[Screenshots of deployment, pipeline execution, and application will be added here] 