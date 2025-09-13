pipeline{
    agent any
    parameters{
        string(name: 'language', defaultValue: 'English', description: 'Enter your preferred language:')
    }
    stages{
        stage('Language'){
            steps{
                script{
                    if(params.language){
                        println "Your entered language is ${params.language}"
                    }
                    else{
                        println "No language entered"
                        println "Language = ${params.language}"
                    }
                }
            }
        }
    }
}