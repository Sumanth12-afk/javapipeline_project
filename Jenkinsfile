pipeline {
    agent any

    tools {
        maven 'Maven'
    }

    environment {
        SONARQUBE_URL = 'http://3.144.142.248:9000'
        SONARQUBE_TOKEN = 'your_sonarqube_token'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sumanth12-afk/javapipeline_project.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package' // Use Maven installed on the host machine
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    docker.image('b2fa856aa4dc').run('-p 9000:9000') // Start SonarQube Docker container
                    withSonarQubeEnv('SonarQube') {
                        sh 'mvn sonar:sonar'
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    docker.build('calculator:latest') // Build Docker image
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.image('calculator:latest').run() // Run Docker container
                }
            }
        }

        stage('Prometheus Monitoring') {
            steps {
                sh 'curl http://3.144.142.248:9090/metrics'
            }
        }
    }
}
