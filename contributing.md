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



# Code architecture


<iframe frameborder="0" style="width:100%;height:683px;" src="https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Omniscience%20Architecture.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1QQipHURIAomjYmFVKvQWa0p_awLovM0n%26export%3Ddownload"></iframe>