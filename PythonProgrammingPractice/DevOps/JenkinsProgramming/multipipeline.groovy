// TASK ONE
// Multiple selectable options (called boolean in Jenkins's website) -> Print options selected in pipeline in Jenkins
// Python script should print whether all options were selected or not
// EX: Three options: Python, C++, and Java -> User selects C++ and Java -> Jenkins program prints that the user selected C++ and Java
// (Python Script) -> Raises a customized exception that's called "All options aren't selected" and print some kind of error message
// EX2: Three options: Python, C++, and Java -> User selects everything -> Jenkins program prints that the user selected Python, C++, and Java
// (Python Script) -> DOESN'T raise exception and prints that everything is selected
// NOTE: python and jenkins scripts run separately
pipeline {
    agent any
    parameters {
        booleanParam(name: 'OPTION_PYTHON', defaultValue: false, description: 'Select Python')
        booleanParam(name: 'OPTION_CPP', defaultValue: false, description: 'Select C++')
        booleanParam(name: 'OPTION_JAVA', defaultValue: false, description: 'Select Java')
    }
    stages {
        stage('Check Options') {
            steps {
                script {
                    def options = []
                    def selectedOptions = []
                    if (params.OPTION_PYTHON) options.add('Python')
                    if (params.OPTION_CPP) options.add('C++')
                    if (params.OPTION_JAVA) options.add('Java')
                    selectedOptions = options
                    def optionsString = options.join(',')
                    def selectedOptionsString = selectedOptions.join(',')
                    bat "C:\\Users\\amrit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe C:\\Users\\amrit\\Desktop\\PythonProgramming\\JenkinsProgramming\\check_options.py \"${optionsString}\" \"${selectedOptionsString}\""
                }
            }
        }
    }
}


// TASK TWO
// Take 10 (string) boolean parameters (the "selectable" options) -> Takes a string parameter (which could contain a single letter, or multiple letters)
// -> Take another string parameter (which should contain a single-digit number) -> Checks whether each parameter contains the letter that the user entered
// -> Splits into two separate lists that contain or don't contain the letter(s) that the user entered (IF THERE IS MORE THAN ONE LETTER, program should check for words that have those letters consecutively (EX: Program gets letters "CA" -> should check for words with the letters CA consecutively))
// -> Program sorts second list based off of WHERE the letter(s) is placed in the elements (if one word has the letter(s) at the front of the word, is is placed ahead of a word that has the letter(s) at the end of the world (so it's given more "priority"))
// -> Prints both lists accordingly
// EX: User enters ["bike", "car", "helicopter", "plane", "rabbit" . . .] (10 parameters), then enters "a" (single letter parameter), then enters "2" (single-digit number)
// -> Program checks whether each parameter contains the letter a (what the user entered) -> Splits list into two separate lists that contains and doesn't contain the letter a
// (["bike", "helicopter" . . .], ["car", "plane", "rabbit" . . .]) -> Sorts second list based off of what letter is in the 2nd index of the first element (Since car is the first element, program checks what letter is in the 2nd index, which is the letter "r")
// -> Sorts second list based off of WHERE the letter "r" is placed (rabbit is placed 1st since the r is the first letter, and plane is at the end since it doesn't have an r)
// -> Prints 1st list as it was (without sorting), and prints 2nd list with the "r" sorting
pipeline {
    agent any
    parameters {
        string(name: 'WORDS', defaultValue: '', description: 'Comma-separated list of words')
        string(name: 'LETTERS', defaultValue: '', description: 'Letters to check for (single or multiple letters)')
        string(name: 'INDEX', defaultValue: '', description: 'Index to sort by (single-digit number)')
    }
    stages {
        stage('Process Strings') {
            steps {
                script {
                    def words = params.WORDS
                    def letters = params.LETTERS
                    def index = params.INDEX
                    def quotedWords = "\"${words}\""
                    env.words = quotedWords
                    env.letters = letters
                    env.index = index
                    bat "C:\\Users\\amrit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe C:\\Users\\amrit\\Desktop\\PythonProgramming\\JenkinsProgramming\\process_strings.py %words% %letters% %index%"
                }
            }
        }
    }
}
