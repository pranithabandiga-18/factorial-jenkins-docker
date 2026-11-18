pipeline {
    agent any

    environment {
        IMAGE_NAME = 'factorial-app'
        IMAGE_TAG = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run program') {
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
        success { echo 'Factorial program ran and the Docker image was built successfully.' }
        failure { echo 'Pipeline failed. Review the stage output above.' }
    }
}
