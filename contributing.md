Feel free to create a Pull request or to open an issue!


# Installation
Create a virtual env (python 3.8)


```shell
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
```

You're all set!


# Code quality
We use black as a formatter, flake8 to lint, and pyright and mypy to check the typing.
If you use VSCode, your VSCode will use our .vscode config containing the required parameters to develop on this project.

If you want to contribute on this project, you can ask the .envvariables file to us.


# Tests

To execute :
```
source djenv/bin/activate
./manage.py test
```

To update the serialization:
```
python manage.py test --snapshot-update
git commit -m "update snapshot" --no-verify
```
