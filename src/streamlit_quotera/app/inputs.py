import streamlit as st
from typing import Tuple, Any, Dict
from io import StringIO


def input_text(readme: Dict[Any, Any]) -> Tuple[str, Any]:
    """User decides whether to upload a txt file or paste text.

    Parameters
    ----------
    readme : Dict
        Dictionary containing tooltips to guide user's choices.

    Returns
    -------
    Tuple[str, Any]
        Text file & corresponding button.
    """
    load_options = dict()
    load_options["load_text"] = st.checkbox(
        "Load a text dataset", False, help=readme["tooltips"]["upload_choice"]
    )
    if load_options["load_text"]:
        file = st.file_uploader(
            "Upload a txt file", type="txt", help=readme["tooltips"]["text_upload"]
        )

        if file:
            stringio = StringIO(file.getvalue().decode("utf-8"))
            text = stringio.read()
        else:
            st.stop()

    else:
        text = st.text_area("Please paste your text :", height=50)

    button = st.button("Paraphrase")

    return text, button
