pipeline {
    agent any

    environment {
        PROJECT_DIR = "unstructured_to_structured"
        VENV = "venv"
    }

    stages {

        stage('Checkout from GitHub') {
            steps {
                git branch: 'main',
      url: 
   'https://github.com/navinaveen-b/unstructured-to-structured.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Data Processing Pipeline') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    python src/main.py
                '''
            }
        }

        stage('Archive Processed Data') {
            steps {
                archiveArtifacts artifacts: 'data/processed/**/*', fingerprint: true
            }
        }

    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check console output."
        }
    }
}

