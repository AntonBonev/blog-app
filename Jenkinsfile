pipeline {
  agent {
    kubernetes {
      label 'kaniko-agent'
      defaultContainer 'kaniko'
    }
  }

  environment {
    IMAGE_NAME = "antonbonev/blog"
    IMAGE_TAG = "${BUILD_NUMBER}"
    DOCKER_REGISTRY = "docker.io"
  }

  stages {
    stage('Clone repository') {
      steps {
        checkout scm
      }
    }

    stage('Build and Push with Kaniko') {
      steps {
        sh '''
          /kaniko/executor \
            --context `pwd` \
            --dockerfile `pwd`/Dockerfile \
            --destination=$DOCKER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG \
            --cleanup
        '''
      }
    }

    stage('Trigger Manifest Update') {
      steps {
        echo "Triggering updateManifest job with tag $IMAGE_TAG"
        build job: 'updatemanifest', parameters: [
          string(name: 'DOCKERTAG', value: IMAGE_TAG)
        ]
      }
    }
  }
}
