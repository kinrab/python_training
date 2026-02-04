pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/kinrab/python_training.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate && pip install --upgrade pip && pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                // Используем call, чтобы подцепить окружение для запуска теста
                bat 'venv\\Scripts\\activate && pytest TEST/test.phones.py'
            }
        }
    }
}
