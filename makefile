venvs: ms1venv ms2venv fbvenv
rmvenvs: rmvenvms1 rmvenvms2 rmvenvfb

ms1venv:
	poetry install -C micro1
ms2venv:
	poetry install -C micro2
fbvenv:
	poetry install -C fallback

rmvenvms1:
	poetry env remove python -C micro1
rmvenvms2:
	poetry env remove python -C micro2
rmvenvfb:
	poetry env remove python -C fallback
