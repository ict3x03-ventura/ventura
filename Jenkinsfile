pipeline {
    agent {
        docker { image 'ubuntu:latest' }
    }
    stages {
        stage('OWASP DependencyCheck'){
            steps {
                dependencyCheck additionalArguments: '--formal HTML --format XML', odcInstallation: 'OWASP'
            }
        }
 
        stage('Deploy') {
            steps {
                sh 'git clone https://github.com/ict3x03-ventura/ventura'
                sh 'pwd'
                sh 'ls -la'
                sh 'sudo ifconfig'
            }
        }
    }
}
