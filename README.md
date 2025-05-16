# Dapr in Action: From Core Concepts to AI Agents

### Presentation: [Slides](https://github.com/pyladiesams/dapr-in-action-may2025/blob/main/workshop/dapr_in_actions.pdf)

## Workshop description

Welcome to the workshop on building AI Agents with Dapr!

[Dapr](https://github.com/dapr/dapr) is a powerful open-source runtime that simplifies building distributed applications. During this session, you'll get up to speed on Dapr's fundamentals and gain practical experience creating AI agents using [dapr-agents](https://github.com/dapr/dapr-agents).

This workshop is split in two parts: 

1. guided workshop on building introductory agents 
2. self-paced advanced workshop

## Introductory Workshop Requirements 

First clone the repo:

```bash
git clone https://github.com/pyladiesams/dapr-in-action-may2025
cd dapr-in-action-may2025
```

### Using a notebook

* Python 3.10 (recommended) or higher
* Jupyter notebook or jupyter-lab

or

* Google Colab

### Setting up dependencies when using Jupyter notebook

* Python 3.10 (recommended) or higher
* pip package manager or [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Usage

### with uv

Run the following code:

```
uv venv
source .venv/bin/activate
uv sync
```

### without uv

Set up a virtual environment using virtualenv:

* pip install virtualenv
* Install environment: python3 -m venv venv
* Activate environment: source venv/bin/activate
* Install dependencies in environment: pip install -r requirements.txt
       
### API Keys

API keys can abe accessed via this [privatebin](https://privatebin.net/?ec00cd7f2c464e55#8xMHSFNHyTrGe8f1DhyB62qCmb9RwrPoFExV5pWKXZEs). The password will be shared during the workshop. 

The keys will only be available during the workshop. If you want to follow the workshop after, please generate HuggingFace and Currents API key yourself first at https://huggingface.co/ and https://currentsapi.services/en.

If you are using Google Colab, instructions on how the set the secrets is provided in the notebook.

If you are using Jupyter notebook locally, please update `helper_secrets.py` file in `workshop/introductory_workshop`:

```env
HUGGINGFACE_API_KEY=your_api_key_here
CURRENTS_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual HuggingFace and Currents API key.

### Starting the notebook

If you are using Jupyter notebooks, navigate to `workshop/introductory_workshop` and run `jupyter notebook`.

If you are using Google Colab, navigate to https://colab.research.google.com/ and import the notebooks in `workshop/introductory_workshop`. 

## [Optional] Self-paced Advanced Workshop

If you'd like to also follow the advanced version of this workshop, we need to install a few more dependencies:

* [Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/)
* [Docker Desktop](https://docs.docker.com/desktop/)

Since we'll be using the Dapr CLI the advanced section of the workshop can't be run in a notebook. Refer to the READMEs in each subdirectory on instructions how to run the code in the terminal.

You are all set and ready to begin!

## Video record
Re-watch [this YouTube stream](https://youtube.com/live/SqGmmLGmrXQ)

## Credits
This workshop was set up by @pyladiesams, Dana Arsovska ([Git](https://github.com/Dzvezdana), [LinkedIn](https://www.linkedin.com/in/dana-arsovska/)) and Marc Duiker ([web site](https://marcduiker.dev/)).
