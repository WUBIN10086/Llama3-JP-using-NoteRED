# Llama3-JP-using-NoteRED

Make a web service using Llama3 -8B for Japanese conversation.
Model supported by [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) 

This repo just a sample for using docker to create the composed continers.

The flow like as follows:

1. create a llama api
2. test your api (can skip)
3. create a requirements list
4. make dockerfile for llama continer.
5. make docker-compose.yaml
6. open the NoteRED webpage
7. edit your service
   

## How to use this repo:

### 1. Download the Llama model by yourself.

run this for Linux:
```
sudo wget https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF/resolve/main/Llama-3-ELYZA-JP-8B-q4_k_m.gguf
```

or download by yourself:

```
https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF/blob/main/Llama-3-ELYZA-JP-8B-q4_k_m.gguf
```

### 2. Download this repo

using:

```
git clone https://github.com/WUBIN10086/Llama3-JP-using-NoteRED.git
```

and add your downloaded model file (in step 2) to the repo floder, the structure should like:

```
web_llama
├── API-python
│   ├── llama_api.py
│   └── test_llama_fastapi.py
├── Llama-3-ELYZA-JP-8B-q4_k_m.gguf
├── requirements.txt
└── docker-compose.yml
```

!!! Dont forget add the model (Llama-3-ELYZA-JP-8B-q4_k_m.gguf).

### 3. create the docker continers

run this command:

```
docker-compose up --build
```

### 4. Open NoteRED in browser

```
127.0.0.1:1880
```

Import the content in the `NoteRED.txt`
