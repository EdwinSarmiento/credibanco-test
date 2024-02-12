pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/EdwinSarmiento/credibanco-test.git'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest web.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t web-python .'
            }
        }
    }
}