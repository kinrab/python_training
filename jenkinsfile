pipeline 

{ agent any

 
    stage('Clone Repository') 
    {
      steps 
      {
              git branch: 'main', 
              url: 'https://github.com/kinrab/python_training.git'
      }
    }

    stage('Create Virtual Environment and install libraries') 
    {

        steps 
        {  
           bat '''        
                python -m venv venv  
                \venv\Scripts\activate
                pip install --upgrade pip
                pip install -r requirements.txt 
               '''        
        }

     }

    stage('Run tests') 
    {

        steps 
        {
            bat 'py.test TEST\test.phones.py'
        }

    }

 }


