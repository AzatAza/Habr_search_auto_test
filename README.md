# Test search Habr
Selenium/Python

```
The Task
1. Open https://habr.com/
2. Fill in the search field
3. Check result
```

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

Start the test from a folder which contains test file(you also can --headless option)
```
Ex: cd ../test_search_habr/test
pytest test_search_input.py
Or using in headless mode:
pytest test_search_input.py --headless true
```

If you want to get Allure report
```
pytest test_search_input.py --alluredir=allure-results/
allure serve allure-results/
```

pre-commit https://pre-commit.com
```
pre-commit run --all-files
```

Test site
```
https://habr.com/
```


