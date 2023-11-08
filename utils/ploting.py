import matplotlib.pyplot as plt

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