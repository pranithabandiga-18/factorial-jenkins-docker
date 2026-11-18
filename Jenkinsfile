pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = 'factorial-pranitha'
        IMAGE_TAG = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout source') {
            steps {
                checkout scm
            }
        }

        stage('Run factorial with Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 factorial.py 5'
                    } else {
                        bat 'py -3 factorial.py 5'
                    }
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                        sh 'docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest'
                    } else {
                        bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
                        bat 'docker tag %IMAGE_NAME%:%IMAGE_TAG% %IMAGE_NAME%:latest'
                    }
                }
            }
        }

        stage('Run container') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} 6'
                    } else {
                        bat 'docker run --rm %IMAGE_NAME%:%IMAGE_TAG% 6'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Factorial ran successfully and the Docker image was built and run.'
        }
        failure {
            echo 'The pipeline failed. Review the console output for the failing stage.'
        }
    }
}
