SHELL=/bin/bash

install-env:
	conda create -n ph python=3.7
	source activate ph && pip install -r requirements.txt
	conda install ipykernel
	source activate ph && python -m ipykernel install --user --name ph --display-name "philipshue"

uninstall-env:
	conda remove --name ph --all
