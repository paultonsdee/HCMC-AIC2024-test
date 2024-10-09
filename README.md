<p align="center">
  <img src="./app/static/images/contest_banner.png" width="1080">
</p>
<h1 align="center">HCMC-AIC2024</h1>

<p align="center">
  <em>Joining forces with innovators and AI enthusiasts, this project is a dynamic collaboration aimed at crafting a cutting-edge event-retrieval system, proudly participating in the Ho Chi Minh AI Challenge 2024.</em>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [🎯 Features](#-features)
- [🤖Tech Stack](#-technologies-used)
- [🚀 Usage](#-getting-started)
- [👣 Workflow](#-workflow)
- [👀 Demo](#-demo)
- [🧑‍💻 Contributors](#-Contributors)
</details>

## 📍 Overview
Welcome! This project is a collaborative endeavor to develop an advanced event-retrieval system. As a participant in the esteemed Ho Chi Minh AI Challenge 2024, our team, **AIO_TOP10**, is dedicated to harnessing the power of artificial intelligence to create a robust and efficient event-retrieval solution.


More details about the challenge refers to this [link.](https://aichallenge.hochiminhcity.gov.vn/)


## 🎯 Features


## 🤖 Tech Stack

### Server building

- Back-end: FastAPI. 
- Front-end: ...
- Deploy: Docker.

### Core technology

- Keyframe-extraction: TransNetV2, K-Means. 
- LLM: Gemini, Groq, SambaNova, etc. 
- Embedding: CLIP. 


## 🚀 Usage

### App Directory
```
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── v1
│   │   ├── components
│   │   │   ├── embedding
│   │   │   ├── kfe               # key frames extraction
│   │   │   ├── llms              # query-rewrite
│   │   │   └── translation
│   │   ├── core
│   │   ├── routes
│   │   ├── services
│   │   └── utils
│   ├── db
│   │   ├── features
│   │   ├── media-info
│   │   ├── objects
│   └── test
│       └── unit
├── bash
├── notebooks
└── recommender
    └── app
        └── api
```

### Running the app

1. **Clone the repository**



2. **Setup Environment**



**Download dataset from Kaggle**

We store our dataset on Kaggle. Please, download it from [here](https://www.kaggle.com/datasets/pyetsvu/aic2024-extracted-data) and compress it in `db` directory, `/backend/db`.
Additionally, we have 2 other appoaches to download. You can read the detail from [here](backend/db/README.md).


3. **Run the application**



## 👣 Workflow

### API

Back-end port: 8000

- `GET` - http://localhost:8000/ : Get a random quote, check basic connection to db, 
- `POST` - http://localhost:8000/search : Search by text (At the moment). 
- `GET` - http://localhost:8000/search/{image_idx} : Get image by image_idx.

_Note:_ Detail about how to get response after running the app successfully is in [notebook](notebooks/dev_search_text_api.ipynb)



## 👀 Demo



## 🧑‍💻 Contributors

<!-- <a href="https://github.com/MinLee0210">
    <img src="https://avatars.githubusercontent.com/u/57653278?v=4">
</a> -->