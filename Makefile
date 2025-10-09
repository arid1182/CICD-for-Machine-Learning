trigger: none
pr: none

resources:
  pipelines:
  - pipeline: 'ci-trigger'
    source: 'hf-CML'
    trigger:
      branches:
        include:
          - main

stages:
- stage: Deploy
  displayName: 'Deploying Application'
  jobs:
  - job: deploy
    displayName: 'Deploying App'
    pool:
      vmImage: 'ubuntu-latest'
    steps:
    - checkout: none
      displayName: 'Skip ADO Checkout'
    
    - script: |
        echo "CD Pipeline triggered by CI pipeline completion"
        echo "Build ID: $(resources.pipeline.ci-trigger.runID)"
        echo "Build Branch: $(resources.pipeline.ci-trigger.sourceBranch)"
        echo "Deploying Application from Github 'update' branch"
      displayName: 'Log Trigger Informations'
    
    - task: Bash@3
      displayName: 'Checkout from Github Account Branch'
      inputs:
        targetType: 'inline'
        script: |
          make github-checkout
      env:
        GITHUB_TOKEN: $(GITHUB_TOKEN)

    - script: |
        pip install -U "huggingface_hub[cli]"
      displayName: 'Install Hugging Face CLI'
    
    - script: |
        make deploy HF=$(HF)
      displayName: 'Deploy to Hugging Face'
      env:
        HF: $(HF)