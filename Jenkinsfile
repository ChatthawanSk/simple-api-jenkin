pipeline {
    agent any

    environment {
        VM2_SSH_CREDENTIALS = '94659338-5609-4f43-a35a-f09b297758e7' // Your SSH credentials ID in Jenkins
        VM2_HOST = '192.168.1.43' // Replace with your VM2 user and IP address
    }

    stages {
        stage('Clone Simple API on VM2') {
            steps {
                script {
                    sshagent([VM2_SSH_CREDENTIALS]) {
                        // Remove existing directory before cloning
                        sh """
                            ssh -o StrictHostKeyChecking=no now@${VM2_HOST} 'rm -rf /path/to/simple-api || true'
                            ssh -o StrictHostKeyChecking=no now@${VM2_HOST} 'git clone --branch main https://github.com/ChatthawanSk/simple-api-jenkin.git /path/to/simple-api'
                        """
                    }
                }
            }
        }

        stage('Run Unit Tests on VM2') {
            steps {
                script {
                    // Run unit tests on VM2
                    sshagent([VM2_SSH_CREDENTIALS]) {
                        sh """
                            ssh -o StrictHostKeyChecking=no now@${VM2_HOST} 'cd /path/to/simple-api && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && pytest test/'
                        """
                    }
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