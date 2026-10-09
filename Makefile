# Exemple : make push m="Your commit name"
push:
	git add .
	git commit -m "$(m)"
	git push


uninstall_all: 
	pip freeze | xargs pip uninstall -y
