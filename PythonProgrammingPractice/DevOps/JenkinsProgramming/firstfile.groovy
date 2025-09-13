pipeline {
    // Agent is a tool that gives us all of the configurations to execute in a particular OS or cloud
    agent any
    stages{
        stage('testing'){
            steps{
                script{
                    println "Testing . . ."
                }
            }
        }
    }
}