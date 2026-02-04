pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/kinrab/python_training.git'
            }
        }

        stage('XCOPY') {
            steps {
                bat '''
                xcopy  D:\\REPO_PYTHON\\Python_Training\\.venv C:\\Users\\Никита\\.jenkins\\workspace\\NewTestRun /E /I /H /Y
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
