pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SalomiParasara/my-webapp.git'
                    credentialsId: 'GITHUB_TOKEN'
            }
        }
    

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest tests/ --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-python-app:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // stop & remove old container if exists
                sh 'docker rm -f my-python-container || true'
                sh 'docker run -d -p 5000:5000 --name my-python-container my-python-app:latest'
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline completed. Visit http://localhost:5000 to see your app running."
        }
    }
}
