ENV=env

$(ENV):
	virtualenv $(ENV)
	$(ENV)/bin/pip install -r requirements.txt

npm_dev:
	make -C app/static dev

npm_prod:
	make -C app/static prod

dev: $(ENV) npm_dev

prod: $(ENV) npm_prod



npm_clean:
	make -C app/static clean

$(ENV)_clean:
	rm -Rf $(ENV)


clean: npm_clean $(ENV)_clean


re: clean default