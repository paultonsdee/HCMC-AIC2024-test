# Instruction to setup DB


## Download dataset manually (HIGHLY RECOMMEND)

We store our dataset on Kaggle. Please, download it from [here](https://www.kaggle.com/datasets/pyetsvu/aic2024-extracted-data) and compress it in `db` directory, `/backend/db`


## Download dataset via shell

We support 2 versions of downloading dataset via command shell, via Google Drive and Kaggle. 

1. Google Drive: This version got a problem that Google may prevent too many download request for a large file. 
2. Kaggle: This version require `kaggle.json`, which is Kaggle's beta API, you can interact with Competitions and Datasets to download data, make submissions, and more via the command line. You can get it from [here](https://www.kaggle.com/settings),`https://www.kaggle.com/settings` , and store it in this directory.