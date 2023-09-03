#!/usr/bin/env python
# coding: utf-8

# In[16]:


# K- Means Clustering Mayank Joshi

import random

# Generate random data points for demonstration
data = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(20)]

# Number of clusters (K)
k = 3

# Initialize cluster centroids randomly
centroids = [random.choice(data) for _ in range(k)]

# Maximum number of iterations
max_iters = 100

# K-Means algorithm
for _ in range(max_iters):
    # Assign data points to clusters
    clusters = [[] for _ in range(k)]
    for point in data:
        distances = [((point[0] - c[0]) ** 2 + (point[1] - c[1]) ** 2) ** 0.5 for c in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    
    # Update cluster centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            new_centroid = (sum(p[0] for p in cluster) / len(cluster), sum(p[1] for p in cluster) / len(cluster))
            new_centroids.append(new_centroid)
        else:
            new_centroids.append(centroids[clusters.index(cluster)])
    
    # Check for convergence
    if new_centroids == centroids:
        break
    
    centroids = new_centroids

# Print clusters and their centroids
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")
    print(f"Centroid: {centroids[i]}")
    print()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




