
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                
                    git 'https://github.com/aamador0202/flask-rest.git'
                    sh 'docker build -t flask-rest .'
                    sh 'docker login --username anthony0202 --password Fanggore-0202'
                    sh 'docker image tag flask-rest anthony0202/flask-rest:latest'
                    sh 'docker image push anthony0202/flask-rest:latest'
                    sh 'kubectl apply -f pv-volume.yml'
                    //sh 'kubectl apply -f pv-claim.yml'
                    
                    //sh 'docker run -d -p 8000:8000 --mount source=pers-vol,target=/app/local flask-rest'

              
            }

        }
    }
}

