pipeline {
    agent any
    environment {
        IMAGE_NAME = "chennupativinaychandra/virtual-hil"
        TAG = "${BUILD_NUMBER}"  // Use build number, not 'latest'
    }
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // FAIL pipeline if tests fail
                bat 'pytest --junitxml=test-reports.xml -v'
            }
        }
        stage('Build Docker Image') {
            // Only run if previous stages PASS
            when { expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' } }
            steps {
                bat 'docker build -t %IMAGE_NAME%:%TAG% .'
                bat 'docker tag %IMAGE_NAME%:%TAG% %IMAGE_NAME%:latest'
            }
        }
        stage('Push to Docker Hub') {
            when { expression { currentBuild.result == 'SUCCESS' } }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    bat 'docker push %IMAGE_NAME%:%TAG%'
                    bat 'docker push %IMAGE_NAME%:latest'
                }
            }
        }
    }
    post {
        always {
            // Archive test results for Jenkins dashboard
            junit 'test-reports.xml'
        }
        success {
            echo "Virtual HIL image ready: ${IMAGE_NAME}:${TAG}"
        }
        failure {
            echo 'Pipeline failed - check pytest results above'
        }
    }
}