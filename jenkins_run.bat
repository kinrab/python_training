
echo "Start..."

git branch: 'main', url: 'https://github.com/kinrab/python_training.git'

python -m venv venv

xcopy  D:\REPO_PYTHON\Python_Training\.venv C:\xxl\venv /E /I /H /Y
                
echo "End of work."