import pandas as pd
import gzip
import json
import pyarrow.ipc as ipc


# Function to load gzipped TSV data into a pandas dataframe
def load_and_filter_jsonl_gz_file_by_chunks(filepath,
                                            categ,
                                            chunk_size=10000,
                                            exclude_fields=None):
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
            record = {k: v for k, v in json.loads(line).items()
                      if k not in exclude_fields}
            records.append(record)

            if len(records) == chunk_size:
                df_chunk = pd.DataFrame(records)
                df_filtered = df_chunk[df_chunk['categories'] == categ]\
                    .drop(columns=exclude_fields, errors='ignore')
                dataframe_chunks.append(df_filtered)
                records = []

        # Make sure to process the last chunk
        if records:
            df_chunk = pd.DataFrame(records)
            df_filtered = df_chunk[df_chunk['categories'] == categ]\
                .drop(columns=exclude_fields, errors='ignore')
            dataframe_chunks.append(df_filtered)

    return pd.concat(dataframe_chunks, ignore_index=True)


def read_and_filter_feather(path, category):
    # Open the feather file using pyarrow.ipc's RecordBatchFileReader
    reader = ipc.RecordBatchFileReader(path)

    filtered_dfs = []

    num_batches = reader.num_record_batches
    for i in range(num_batches):
        batch = reader.get_batch(i)
        df = batch.to_pandas()
        filtered_df = df[df['categories'] == category]

        if not filtered_df.empty:
            filtered_dfs.append(filtered_df)

    final_df = pd.concat(filtered_dfs, ignore_index=True)
    return final_df
