pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t covid-flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Running Flask container...'
                bat 'docker rm -f covid-service || exit 0'
                bat 'docker run -d -p 5000:5000 --name covid-service covid-flask-app'
                sleep time: 5, unit: 'SECONDS'
            }
        }

        stage('Test API Endpoints') {
            steps {
                echo 'Testing endpoints...'
                bat 'curl.exe http://localhost:5000/status'
                bat 'curl.exe "http://localhost:5000/newCasesPeak?country=israel"'
                bat 'curl.exe "http://localhost:5000/recoveredPeak?country=israel"'
                bat 'curl.exe "http://localhost:5000/deathsPeak?country=israel"'
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Stopping and removing container...'
                bat 'docker stop covid-service'
                bat 'docker rm covid-service'
            }
        }
    }
}
