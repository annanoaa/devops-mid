# DevOps Midterm Project Documentation

## Introduction

This project demonstrates a complete DevOps pipeline implementation in a local environment. It includes a simple Flask web application with CI/CD integration, Blue/Green deployment strategy, Infrastructure as Code (using Terraform and Ansible), and monitoring through health checks. The entire pipeline shows how modern software development practices can be implemented locally while following DevOps principles.

## Project Components

### 1. Web Application

A simple Flask application that allows users to submit messages with their name. Each message is timestamped, demonstrating basic form handling and data processing.

**[screens/homepage.png]**
*The Flask application home page with a form for submitting messages.*



### 2. Unit Tests

Automated tests verify the application's functionality, ensuring that both the homepage route and the form submission work correctly.

**[screens/test.png]**
*Terminal output showing all tests passing.*

### 3. Version Control

The project uses Git with two branches: main (production) and dev (development). Changes are made in the dev branch, tested, and then merged to main when ready.

**[screens/branches.png]**
*Git branch structure showing main and dev branches.*

**[screens/branches_2.png]**
*Commit history showing feature development and merges.*

### 4. Continuous Integration

GitHub Actions automatically runs tests on every push to both main and dev branches, ensuring code quality.

**[screens/actions.png]**
*GitHub Actions CI pipeline successfully running tests after code push.*

### 5. Infrastructure as Code

Terraform and Ansible work together to provision and configure the deployment environment:
- Terraform creates the directory structure for Blue/Green deployment
- Ansible handles the application deployment and environment switching

**[screens/terraform.png]**
*Terraform configuration files.*

**[screens/ansible.png]**
*Ansible playbook for deployment.*

### 6. Blue/Green Deployment

The application uses a Blue/Green deployment strategy to minimize downtime:
- Two identical environments (blue and green)
- Only one active at a time
- New deployments go to the inactive environment
- Switch only happens after successful health checks

## Challenges and Lessons Learned

### Challenges

1. **Local Environment Limitations**: Simulating a production environment locally presented challenges, particularly in maintaining separation between environments.

2. **Tool Integration**: Getting Terraform and Ansible to work together seamlessly required careful planning of the workflow and understanding how each tool handles state.

3. **Blue/Green Implementation**: Implementing a true Blue/Green deployment locally required creative solutions without the resources typically available in cloud environments.

4. **Test Reliability**: Ensuring tests were consistent and reliable across different environments required careful consideration of dependencies and environment variables.

5. **CI Pipeline Configuration**: Setting up GitHub Actions to work correctly with the local development workflow required several iterations to get right.

### Lessons Learned

1. **Infrastructure as Code Benefits**: Even for local development, IaC provides significant benefits in consistency and reproducibility.

2. **Deployment Strategies Matter**: Blue/Green deployment demonstrated significant advantages in reducing risk and downtime, even in a simulated environment.

3. **Automated Testing Value**: The CI pipeline caught several issues before they made it to the main branch, proving the value of automated testing.

4. **Tooling Flexibility**: DevOps tools like Ansible and Terraform are flexible enough to adapt to unusual use cases like local deployment.

5. **Documentation Importance**: Comprehensive documentation made the entire process more manageable and will make future maintenance easier.