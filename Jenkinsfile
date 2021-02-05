pipeline {
  agent any
  stages {
    stage('Checkout Scm') {
      steps {
        git(credentialsId: 'Repo-Cred', url: 'https://github.com/aamador0202/flask-rest.git')
      }
    }

    stage('Shell script 0') {
      steps {
        sh '''#Building docker image, logging onto dockerhub and pushing lastest image
#docker build -t flask-rest . ;
#docker login --username anthony0202 --password Fanggore-0202 ;
#docker image tag flask-rest anthony0202/flask-rest:latest ;
#docker image push anthony0202/flask-rest:latest ;
'''
      }
    }

    stage('Shell script 1') {
      steps {
        sh '''#Creating namespaces for prod, dev and qa

kubectl apply -f prod-ns.yml ;
kubectl apply -f dev-ns.yml ;
kubectl apply -f qa-ns.yml ;

#Creating context for prod and switching to prod namespace
kubectl config set-context prod --namespace=prod-namespace \\
--cluster=minikube --user=minikube ;
kubectl config use-context prod ;
kubectl apply -f pv-volume-prod.yml ;
kubectl apply -f pv-claim.yml
kubectl apply -f prod-pod.yml
kubectl apply -f prod-service.yml
kubectl apply -f prod-secret.yml
kubectl apply -f prod-ingress.yml

#Creating context for dev and switching to dev namespace
kubectl config set-context dev --namespace=dev-namespace \\
--cluster=minikube --user=minikube ;
kubectl config use-context dev ;
kubectl apply -f pv-volume-dev.yml ;
kubectl apply -f pv-claim.yml
kubectl apply -f dev-pod.yml
kubectl apply -f dev-service.yml
kubectl apply -f dev-secret.yml
kubectl apply -f dev-ingress.yml

#Creating context for qa and switching to qa namespace
kubectl config set-context qa --namespace=qa-namespace \\
--cluster=minikube --user=minikube ;
kubectl config use-context qa ;
kubectl apply -f pv-volume-qa.yml ;
kubectl apply -f pv-claim.yml
kubectl apply -f qa-pod.yml
kubectl apply -f qa-service.yml
kubectl apply -f qa-secret.yml
kubectl apply -f qa-ingress.yml


'''
      }
    }

  }
  triggers {
    pollSCM('* * * * *')
  }
}
