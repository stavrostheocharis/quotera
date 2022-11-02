<div align="center">

![Quotera](src/streamlit_quotera/references/logo_2.png)

[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue.svg)](#supported-python-versions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-informational.svg)](https://github.com/artefactory-global/streamlit_prophet/blob/main/LICENSE)

Deploy a [Streamlit](https://streamlit.io/) app, or a [FastAPI](https://fastapi.tiangolo.com/) API to paraphrase text

</div>
## Requirements
### Python version
* Main supported version : <strong>3.9</strong> <br>
* Other supported versions : <strong>3.7</strong> & <strong>3.8</strong>

To use the scripts on your computer, please make sure you have one of these versions installed.

### Install environment & dependencies

In order to run the needed scripts you need to have python installed and run the command below.
```
python3 -m venv /path/to/new/virtual/environment
```

To activate your `venv` run `source "env_name"/bin/activate`.

To install dependencies run the command:

```bash
pip install -r requirements.txt
```

### How to use it

As stated there are 2 ways using the Streamlit app, or the API.

Once installed the dependencies
- run the following command from CLI to open the app in the default web browser:

    ```
    python quotera_streamlit_cli.py 
    ```
- run the following command from CLI to open the API in the default web browser:

    ```
    python quotera_cli.py serve
    ```

## How to contribute?

We welcome any suggestions, problem reports, and contributions!
For any changes you would like to make to this project, we invite you to submit an [issue]("https://github.com/stavrostheocharis/quotera/issues").

For more information, see [`CONTRIBUTING`](https://github.com/stavrostheocharis/quotera/blob/main/CONTRIBUTING.md) instructions.

If you wish to containerize the app, see [`DOCKER`](https://github.com/stavrostheocharis/quotera/blob/main/DOCKER.md) instructions.