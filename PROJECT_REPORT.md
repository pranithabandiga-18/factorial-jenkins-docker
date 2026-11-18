# Factorial CI project report

**Repository:** pranithabandiga-18/factorial-jenkins-docker  
**Application:** Python command-line factorial calculator  
**Automation:** Jenkins Pipeline  
**Container:** Docker

## Project goal

This project calculates the factorial of a non-negative integer and packages the program in a Docker image. The Jenkins pipeline is defined to retrieve the code from GitHub, run the Python program, build the image, and run the container.

## Program design

The command-line program accepts one integer. Its factorial function begins with a result of 1, then multiplies by each integer from 2 to the input. This returns 1 for both 0! and 1!, and rejects negative input. The loop makes the calculation steps explicit.

Example:

~~~text
Input: 5
Output: 5! = 120
~~~

## Docker design

The Docker image uses python:3.12-slim, copies only the application file, and runs as the unprivileged appuser account. The default input is 5; a value supplied to docker run replaces that default.

Build and run commands:

~~~powershell
docker build -t factorial-pranitha:latest .
docker run --rm factorial-pranitha:latest 6
~~~

Expected container output:

~~~text
6! = 720
~~~

## Jenkins pipeline

The Jenkinsfile contains four stages:

1. Checkout source retrieves the configured Git repository.
2. Run factorial with Python runs factorial.py with input 5.
3. Build Docker image builds a build-number tag and updates the latest tag.
4. Run container runs the image with input 6.

The pipeline uses bat and the Python launcher on Windows, and sh with python3 on Unix. The Jenkins agent must have Git, Python, Docker CLI, and permission to reach a running Docker Engine.

## Configure the Jenkins job

Create a Pipeline job and select Pipeline script from SCM:

- SCM: Git
- Repository URL: https://github.com/pranithabandiga-18/factorial-jenkins-docker.git
- Branch: */main
- Script path: Jenkinsfile

After saving, use Build Now and review Console Output for each stage.

## Evidence and current status

The Git push shown in the project setup completed and set main to track origin/main. The Jenkinsfile and application files are prepared in the repository.

A Jenkins build result is not included here because the Windows Jenkins service was not registered when checked. Add a screenshot of the successful Jenkins Console Output after Jenkins is installed, the service is running, and the job completes. This report does not claim a Jenkins build that has not been observed.
