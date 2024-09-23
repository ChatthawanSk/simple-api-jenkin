pipeline {
    agent any

    environment {
        VM2_SSH = "now@192.168.56.101" // Replace with your VM2 user and IP address
        VM3_SSS = "now@192.168.56.103"
    }

    stages {
        stage('Clone Simple API on VM2') {
            steps {
                script {
                    // Clone the simple-api repository directly on VM2
                    sh """
                        ssh ${VM2_SSH} 'git clone --branch main https://github.com/yourusername/simple-api.git /path/to/simple-api'
                    """
                }
            }
        }

        stage('Run Unit Tests on VM2') {
            steps {
                script {
                    // Run unit tests on VM2
                    sh """
                        ssh ${VM2_SSH} 'cd /path/to/simple-api && pip install -r requirements.txt && pytest tests/'
                    """
                }
            }
        }

        stage('Build Docker Image on VM2') {
            steps {
                script {
                    // Build Docker image for simple-api on VM2
                    sh """
                        ssh ${VM2_SSH} 'cd /path/to/simple-api && docker build -t myregistry/simple-api:latest .'
                    """
                }
            }
        }

        stage('Create Docker Container on VM2') {
            steps {
                script {
                    // Run the Docker container for testing on VM2
                    sh """
                        ssh ${VM2_SSH} 'docker run -d --name simple-api-container -p 5000:5000 myregistry/simple-api:latest'
                    """
                }
            }
        }

        stage('Clone Simple API Robot on VM2') {
            steps {
                script {
                    // Clone the simple-api-robot repository directly on VM2
                    sh """
                        ssh ${VM2_SSH} 'git clone --branch main https://github.com/yourusername/simple-api-robot.git /path/to/simple-api-robot'
                    """
                }
            }
        }

        stage('Run Robot Tests on VM2') {
            steps {
                script {
                    // Run Robot Framework tests on VM2
                    sh """
                        ssh ${VM2_SSH} 'cd /path/to/simple-api-robot && pip install -r requirements.txt && robot test.robot'
                    """
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    // Push the built image to the Docker registry from VM2
                    sh """
                        ssh ${VM2_SSH} 'docker push myregistry/simple-api:latest'
                    """
                }
            }
        }

        stage('Clean Up on VM2') {
            steps {
                script {
                    // Stop and remove the container on VM2
                    sh """
                        ssh ${VM2_SSH} 'docker stop simple-api-container || true && docker rm simple-api-container || true'
                    """
                }
            }
        }
    }

    post {
        always {
            // Cleanup workspace
            cleanWs()
        }
    }
}