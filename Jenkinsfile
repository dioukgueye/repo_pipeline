node {
    stage('Clone') {
        git branch: 'main', url: 'https://github.com/dioukgueye/repo_pipeline.git'
    }
    stage('Build') {
        bat label: '', script: 'javac Main.java'
    }
    stage('Run') {
        bat label: '', script: 'java Main'
    }
}
