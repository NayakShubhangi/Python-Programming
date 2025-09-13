pipeline{
    agent any
    stages{
        stage("Execute Python"){
            steps{
                script{
                    bat "C:\\Users\\amrit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe ${env.workspace}/github_integration.py"
                }
            }
        }
    }
}