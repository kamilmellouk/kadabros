import pandas as pd
import gzip
import json
import pyarrow.ipc as ipc
import pyarrow.feather as feather
import os 
import matplotlib.pyplot as plt
import seaborn as sns


# Function to load gzipped TSV data into a pandas dataframe
def load_tsv_gz_file(filepath):
    with gzip.open(filepath, 'rt') as f:
        df = pd.read_csv(f, delimiter='\t')
    return df

def load_and_filter_jsonl_gz_file_by_chunks(filepath, chunk_size=10000, exclude_fields=None):
    '''
    Spefcify the chunk size and the fiels to exclude or not if needed. 
    Return the video matedatas of video include in the global variable category
    '''
    if exclude_fields is None:
        exclude_fields = ['title', 'description']
    dataframe_chunks = []
    
    with gzip.open(filepath, 'rt', encoding='utf-8') as f:
        records = []
        for line in f:
            # Exclude unwanted fields here
            record = {k: v for k, v in json.loads(line).items() if k not in exclude_fields}
            records.append(record)
            
            if len(records) == chunk_size:
                df_chunk = pd.DataFrame(records)
                df_filtered = df_chunk[df_chunk['categories'] == CATEGORY].drop(columns=exclude_fields, errors='ignore')
                dataframe_chunks.append(df_filtered)
                records = []
        
        # Make sure to process the last chunk
        if records:
            df_chunk = pd.DataFrame(records)
            df_filtered = df_chunk[df_chunk['categories'] == CATEGORY].drop(columns=exclude_fields, errors='ignore')
            dataframe_chunks.append(df_filtered)
    
    return pd.concat(dataframe_chunks, ignore_index=True)

def read_and_filter_feather(path):
    # Open the feather file using pyarrow.ipc's RecordBatchFileReader
    reader = ipc.RecordBatchFileReader(path)

    # Initialize an empty list to store the filtered DataFrames
    filtered_dfs = []
    # Loop over all batches
    num_batches = reader.num_record_batches
    for i in range(num_batches):
        # Get the ith batch
        batch = reader.get_batch(i)
        
        # Convert the batch to a pandas DataFrame
        df = batch.to_pandas()
        
        # Filter the DataFrame by category
        filtered_df = df[df['categories'] == CATEGORY]
        
        # If the filtered DataFrame is not empty, add it to the list
        if not filtered_df.empty:
            filtered_dfs.append(filtered_df)

    # Once the loop is complete, concatenate all the filtered DataFrames
    final_df = pd.concat(filtered_dfs, ignore_index=True)
    return final_df

def plot_topN_tag(tag_col, N):
    # Step 1: Split the `tags` column into individual tags and explode the DataFrame.
    tags_exploded = tag_col.str.split(',').explode()

    # Step 2: Count the occurrences of each tag.
    tags_count = tags_exploded.value_counts()

    # Step 3: Sort the results and plot the top 10 tags.
    top_tags = tags_count.head(N)
    top_tags.plot(kind='bar')
    plt.title(f'Top {N} Tags')
    plt.xlabel('Tags')
    plt.ylabel('Count')
    plt.show()
