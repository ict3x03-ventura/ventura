pipeline {
    agent any
    stages {
        stage('OWASP DependencyCheck'){
            steps {
                dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP'
            }
            post {
                success { 
                    dependencyCheckPublisher pattern: '**/dependency-check-report.xml'}
            }
        }
    }
}
