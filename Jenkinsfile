pipeline {
    agent any

    environment {
        VM2_SSH = "now@192.168.1.43" // Replace with your VM2 user and IP address
        VM3_SSH = "now@192.168.1.103"
    }

    stages {
        stage('Clone Simple API on VM2') {
            steps {
                script {
                    // Remove existing directory before cloning
                    sh """
                        ssh -o StrictHostKeyChecking=no now@192.168.1.43 'rm -rf /path/to/simple-api/* /path/to/simple-api/.* 2>/dev/null || true'
                        ssh -o StrictHostKeyChecking=no ${VM2_SSH} 'git clone --branch main https://github.com/ChatthawanSk/simple-api-jenkin.git /path/to/simple-api'
                    """
                }
            }
        }

        stage('Run Unit Tests on VM2') {
            steps {
                script {
                    // Run unit tests on VM2
                    sh """
                        ssh ${VM2_SSH} 'cd /path/to/simple-api && pip install -r requirements.txt && pytest test/'
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