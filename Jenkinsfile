pipeline {
    agent any

    tools {
        maven 'Maven'
    }

    environment {
        SONARQUBE_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'your_sonarqube_token'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/your-java-app.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'mvn sonar:sonar'
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    docker.build('your-java-app:latest')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.run('your-java-app:latest')
                }
            }
        }

        stage('Prometheus Monitoring') {
            steps {
                sh 'curl http://localhost:9090/metrics'
            }
        }
    }
}
