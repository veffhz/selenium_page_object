# selenium page object

#### project test automation with Selenium and Python

https://stepik.org/course/575

##### install requirements

```pip3 install -r requirements.txt```

##### install chrome driver:

```
wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

##### run tests:
```pytest -v --tb=line --language=en test_main_page.py```
```pytest -v --tb=line --language=en test_product_page.py```
