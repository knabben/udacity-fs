run:
	vagrant up --provision-with=shell,ansible

install:
	pip install ansible
	vagrant provision --provision-with=shell,ansible

update:
	vagrant provision --provision-with=ansible

drop:
	vagrant destroy -f

deploy:
	vagrant provision --provision-with=deploy

install_production:
	ssh -p 22 ubuntu@52.206.145.58 < install.sh
	ansible-playbook playbooks/prod/install.yml -i ansible.cfg

deploy_production:
	ansible-playbook playbooks/prod/deploy.yml -i ansible.cfg
