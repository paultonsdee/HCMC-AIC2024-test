import pandas as pd
import numpy as np

def recommend_cold_start(df:pd.DataFrame, video_idx:str, m_clusters:int, m_videos:int=4) -> list[str]: 
    row = df[df['Video name'].str.endswith(f"{video_idx}")]
    selected_label = row.label.values[0]

    # Picking from m remains clusters
    while True: 
        rand_clusters = np.random.choice(9, m_clusters, replace=False)
        if not np.isin(selected_label, rand_clusters): 
            break

    
    recommend_list = []

    for cluster in rand_clusters: 
        selected_docs = df[df['label'] == cluster]
        n_docs = len(selected_docs)
        rand_idx = np.random.randint(0, n_docs, m_videos)
        for doc in selected_docs.iloc[rand_idx, 0]:   # Only select the first row as Video name
            recommend_idx = doc.split('/')[-1]
            recommend_list.append(recommend_idx)

    
    return recommend_list