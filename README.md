# Factorial Program with Jenkins and Docker

A command-line Python program that calculates the factorial of a non-negative integer. The Jenkins pipeline runs the program, builds a Docker image, and runs a container from that image.

## Requirements

- Python 3.8 or newer for running locally
- Git to publish the source
- Docker Engine (and a Jenkins agent with Docker access) for image building
- Jenkins with Pipeline support and a Git installation

## Run locally

```bash
python factorial.py 5
```

Expected output:

```text
5! = 120
```

The input must be a non-negative whole number. `0!` is `1`. For example, `python factorial.py -1` reports an input error.

## Build and run the Docker image

From this directory:

```bash
docker build -t factorial-app:latest .
docker run --rm factorial-app:latest 6
```

The image uses `python:3.12-slim`, copies in the one-file application, and sets the program as its entry point. The default input is `5`, so `docker run --rm factorial-app:latest` prints `5! = 120`; a number passed after the image name replaces that default.

## Publish to GitHub with Git

1. On GitHub, create a new empty repository named `factorial-jenkins-docker`. Do not initialize it with a README, license, or `.gitignore` because this folder already contains them.
2. Open a terminal in this project directory and run:

   ```bash
   git init -b main
   git add .
   git commit -m "Add factorial app with Jenkins and Docker"
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/factorial-jenkins-docker.git
   git push -u origin main
   ```

Replace `YOUR_GITHUB_USERNAME` with your GitHub username. GitHub may prompt you to authenticate; use a configured credential manager or a personal access token when Git asks for credentials. Do not put a token in the remote URL or commit it to this project.

If this folder is already a Git repository, skip `git init -b main`; add the remote only if one is not already configured (`git remote -v`).

## Configure the Jenkins job

1. Ensure the Jenkins controller/agent that will run this pipeline has Git, Python 3, and Docker installed. The Jenkins agent must be allowed to run Docker commands (typically through a Docker socket or an appropriately configured agent). The Jenkinsfile uses the Unix `sh` step, so run it on a Linux agent.
2. In Jenkins, select **New Item**, enter a job name such as `factorial-pipeline`, choose **Pipeline**, then select **OK**.
3. Under **Pipeline**, choose **Pipeline script from SCM**. Set **SCM** to **Git**, enter the GitHub repository URL, and configure credentials if it is private. Set the branch to `*/main` and **Script Path** to `Jenkinsfile`.
4. Save and select **Build Now**. The stages check out the repository, run `python3 factorial.py 5`, build a build-number-tagged image and a `latest` tag, then run the image with input `6`.
5. Open the build's **Console Output** to see each command and its result. The image is created on the Jenkins Docker host; it is not automatically uploaded to Docker Hub.

### Optional: publish the image to Docker Hub

The provided pipeline builds and runs the image locally. To publish it, first create a Docker Hub repository and add a Jenkins credential of type **Username with password** (use a Docker Hub access token as the password). Then adapt the image name to `YOUR_DOCKERHUB_USERNAME/factorial-app` and add a credentials-bound login, `docker push` stage, and logout. Keep the credential ID in Jenkins and never hard-code the token in the Jenkinsfile. Publishing is omitted by default so the pipeline works without registry credentials.

## How the factorial works

For a non-negative integer `n`, the factorial is the product of all positive integers up to `n`: `n! = n × (n−1) × ... × 1`. The special case `0! = 1` is part of the mathematical definition. Python's `math.factorial` performs the calculation using arbitrary-precision integers. The command-line parser converts the argument to an integer and rejects text or decimal input; the application also rejects negative integers.

## Project files

- `factorial.py` — command-line program and input validation
- `Dockerfile` — reproducible container image definition
- `Jenkinsfile` — checkout, execution, image build, and container run stages
- `.dockerignore` — excludes Git metadata and Python cache files from image build context
