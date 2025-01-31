#English to Chinese Translation Project
Overview

This project enables the translation of English text into Chinese using a pretrained machine translation model. The model leverages the power of natural language processing (NLP) to convert input text from English to Chinese accurately and efficiently. This is achieved through a user-friendly interface for easy interaction with the translation engine.
Features

    English to Chinese Translation: A pretrained model is used for seamless translation.
    Local Processing: The model runs locally on your machine without requiring an internet connection once the model is downloaded.
    Efficient: Optimized for CPU usage, with the possibility of utilizing GPU support for faster translations.

Requirements

    Python 3.x
    PyTorch (For model loading and inference)
    Hugging Face Transformers library (For pretrained models)
    Flask (For creating a web-based interface, if applicable)

Installation

    Clone the repository:

git clone https://github.com/MikhaAnnaJohnson/EnglishToChineseTranslation.git

Download pretrained model: The pretrained MarianMT model for English-to-Chinese translation will be automatically loaded when running the code.

You can  run a Flask web application for real-time translation via a browser:

CPU Usage

This project processes translation tasks using the CPU by default. The pretrained model performs tokenization, inference, and decoding tasks locally on your machine. While the translation process will be slower on a CPU, it is entirely functional without the need for GPU support.

Acknowledgments

Hugging Face Transformers
PyTorch
MarianMT
