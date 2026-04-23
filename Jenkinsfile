pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/vinaychennupati984-dev/Virtual-HIL.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t virtual-hil .'
            }
        }
    }

    post {
        success {
            echo 'Build Successful ✅'
        }
        failure {
            echo 'Build Failed ❌'
        }
    }
}