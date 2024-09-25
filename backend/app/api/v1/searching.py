"""Algorihtms that related to search."""

def search_by_text(query: str, top_k: int, vector_store) -> dict:
    """
    Searches for images related to a given text query using a vector store.

    Args:
        query (str): The text query to search for.
        top_k (int): The number of top results to return.
        vector_store: The vector store object to use for searching.

    Returns:
        dict: A dictionary containing the search results:
            - scores (list): A list of similarity scores for each retrieved image.
            - idx_image (list): A list of indices corresponding to the retrieved images.
            - infos_query (list): A list of filenames (without path) associated with the query.
            - image_paths (list): A list of filenames (without path) associated with the retrieved images.
    """
    scores, idx_image, infos_query, image_paths = vector_store.text_search(query, top_k)

    infos_query = [info.split('/')[-1] for info in infos_query]
    image_paths = [image_path.split('/')[-1] for image_path in image_paths]

    return {
        'scores': scores.tolist(),
        'idx_image': idx_image.tolist(),
        'infos_query': infos_query, 
        'image_paths': image_paths
    }


def search_by_image(): 
    ...

def search_by_image_online(): 
    ...