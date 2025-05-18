pipeline {
    agent any

    parameters {
        string(name: 'COUNTRIES', defaultValue: 'israel,usa,germany', description: 'Comma-separated list of countries')
    }

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
                script {
                    echo "Testing endpoints for countries: ${params.COUNTRIES}"
                    def countries = params.COUNTRIES.split(',')

                    for (country in countries) {
                        echo "🔍 Querying country: ${country}"
                        bat "curl.exe \"http://localhost:5000/newCasesPeak?country=${country.trim()}\""
                        bat "curl.exe \"http://localhost:5000/recoveredPeak?country=${country.trim()}\""
                        bat "curl.exe \"http://localhost:5000/deathsPeak?country=${country.trim()}\""
                    }
                }
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
