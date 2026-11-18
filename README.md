# Factorial CI project

This project calculates the factorial of a non-negative integer. The same command-line program can run with Python or inside Docker. A Jenkins pipeline checks out the repository, runs the program, builds an image, and runs a container.

## Project files

- factorial.py contains the factorial function and command-line interface.
- Dockerfile packages the program in a small Python image and runs it as a non-root user.
- Jenkinsfile defines the checkout, Python run, image build, and container run stages.
- .dockerignore keeps Git and local Python files out of the Docker build context.
- .gitignore excludes local Python cache and environment files from Git.
- PROJECT_REPORT.md explains the design and records how to complete the Jenkins run evidence.

## Run with Python

From this directory:

~~~powershell
py -3 factorial.py 5
~~~

Expected output:

~~~text
5! = 120
~~~

The calculation starts at 1 and multiplies by every integer from 2 to the requested number. This also gives the defined results 0! = 1 and 1! = 1. Negative input is rejected.

## Build and run with Docker

~~~powershell
docker build -t factorial-pranitha:latest .
docker run --rm factorial-pranitha:latest 6
~~~

Expected output from the container:

~~~text
6! = 720
~~~

Omit the final number to use the image's default input of 5.

## Jenkins pipeline

The Jenkinsfile supports Windows and Unix agents. The agent needs Git, Python, Docker CLI, and access to a running Docker Engine. For a Windows Jenkins service, make sure the service account can run py -3 and reach Docker Desktop's engine.

Create a Pipeline job with these settings:

1. Select New Item, enter factorial-pipeline, choose Pipeline, then select OK.
2. Under Pipeline, choose Pipeline script from SCM and set SCM to Git.
3. Repository URL: https://github.com/pranithabandiga-18/factorial-jenkins-docker.git
4. Branch specifier: */main
5. Script path: Jenkinsfile

Save the job, then select Build Now. Open Console Output to view the checkout, program output, Docker build, and container output. The image is created on the Jenkins agent and is not published to Docker Hub by this pipeline.

## Push later changes to GitHub

Run these commands in the project folder after editing files:

~~~powershell
git add factorial.py Dockerfile .dockerignore .gitignore Jenkinsfile README.md PROJECT_REPORT.md
git commit -m "Update factorial CI project"
git push origin main
~~~

## Report and evidence

PROJECT_REPORT.md is written for this project. Add your own screenshot of the successful Jenkins Console Output after the service is installed and a build completes. Do not report a successful Jenkins build until that output is available.
