pipeline {
    agent any
    parameters {
        file(name: 'TEXT_FILE', description: 'Upload your .txt file')
    }
    stages {
        stage('Process Text File') {
            steps {
                script {
                    def uploadedFile = "${WORKSPACE}/params.TEXT_FILE"
                    bat "C:\\Users\\amrit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe\" \"C:\\Users\\amrit\\Desktop\\PythonProgramming\\JenkinsProgramming\\read_txt.py ${uploadedFile}"
                    def result = readFile(uploadedFile)
                    println "Result: ${result}"
                }
            }
        }
    }
}


// ERROR IS RETURNED