FLASK_APP = app

.PHONY: run
run:
		flask --app $(FLASK_APP) run