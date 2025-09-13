// pipeline{
//     agent any
//     stages{
//         stage('Python Script Integration'){
//             steps{
//                 script{
//                     bat 'C:\\Users\\amrit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe C:\\Users\\amrit\\Desktop\\PythonProgramming\\JenkinsProgramming\\something.py'
//                 }
//             }
//         }
//     }
// }

// TASK ONE
// Jenkins program akes two string parameters named "number1" and "number2"
// Write python script
// -> Inside of the python script
// -> Convert to int
// -> Find the greater number out of the two variables
// -> print it
// NOTE: To accept Jenkins parameters inside of a pythons script, need to use command line arguments
pipeline {
    agent any
    parameters {
        string(name: 'number1', defaultValue: '0', description: 'First Number')
        string(name: 'number2', defaultValue: '0', description: 'Second Number')
    }
    stages {
        stage('Compare numbers') {
            steps {
                script {
                    def number1 = params.number1
                    def number2 = params.number2
                    bat "C:\\Users\\amrit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe C:\\Users\\amrit\\Desktop\\PythonProgramming\\JenkinsProgramming\\compare_numbers.py %number1% %number2%"
                }
            }
        }
    }
}

// TASK TWO
// Take a parameter that's called "choice" in Jenkins configuration (on the website)
// Choice dropdown should have some programming language names in it (EX: Python, Java, C, ect...)
// Whatever is selected should be printed, but in a python script
pipeline {
    agent any
    parameters {
        choice(name: 'choice', choices: ['Python', 'Java', 'C', 'JavaScript'], description: 'Select a programming language')
    }
    stages {
        stage('Print Choice') {
            steps {
                script {
                    bat "C:\\Users\\amrit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe C:\\Users\\amrit\\Desktop\\PythonProgramming\\JenkinsProgramming\\print_choice.py %choice%"
                }
            }
        }
    }
}