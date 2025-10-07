install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py 

train:
	python train.py


eval:
	echo "## Model Metrics" > report.md
	cat ./Results/metrics.txt >> report.md
	echo '\n## Confusion Matrix Plot' >> report.md
	echo '![Confusion Matrix](./Results/model_results.png)' >> report.md
	
	

package-artifacts:
	mkdir -p output
	cp -r Results output/
	cp report.md output/


update-branch:
	git config --global user.name $(USER_NAME)
	git config --global user.email $(USER_EMAIL)
	git remote set-url origin https://$(GITHUB_CONNECTION_USERNAME):$(GITHUB_TOKEN)@github.com/arid1182/CICD-for-Machine-Learning.git
	git config --global credential.helper store
	echo "https://$(GITHUB_CONNECTION_USERNAME):$(GITHUB_TOKEN)@github.com" > ~/.git-credentials
	git fetch origin update --update-head-ok
	git checkout -B update origin/update 2>/dev/null || git checkout -B update 
	git add -A
	git commit -am "Update with new results:$(build.BuildId)" || echo "No Changes to Commit "
	git push origin update --force-with-lease


hf-login: 
	hf auth login --token $(HF) --add-to-git-credential

push-hub: 
	hf upload tcse11itjr/Drug-Classifications ./App --repo-type=space --commit-message="Sync App files"
	hf upload tcse11itjr/Drug-Classifications ./Model /Model --repo-type=space --commit-message="Sync Model"
	hf upload tcse11itjr/Drug-Classifications ./Results /Metrics --repo-type=space --commit-message="Sync Model"

deploy: hf-login push-hub

all: install format train eval deploy