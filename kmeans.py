#!/usr/bin/env python


'''
Cluster a set of points into N groups that minimize intra-cluster distance.


- choose N random points as centroids
- cluster each point with its nearest centroid
- replace centroids with the center of each cluster
- repeat until clusters stabalize

https://en.wikipedia.org/wiki/K-means_clustering
'''


from collections import defaultdict
from random import randint, seed, sample


def cluster(points, n):
    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    # to start, choose some random centroids to cluster around
    centroids = sample(points, n)

    for i in range(100):
        clusters = defaultdict(list)
        error = 0

        for point in points:
            # bucket each point with the nearest centroid
            nearest_centroid = None
            nearest_distance = None

            for centroid in centroids:
                # find the nearest centroid
                dist = distance(point, centroid)
                if nearest_distance is None or dist < nearest_distance:
                    nearest_distance = dist
                    nearest_centroid = centroid

            clusters[nearest_centroid].append(point)
            error += nearest_distance

        # refine choice of centroids by finding center of each cluster
        centroids = []
        for centroid, clustered_points in clusters.items():
            x = sum([ p[0] for p in clustered_points ]) // len(clustered_points)
            y = sum([ p[1] for p in clustered_points ]) // len(clustered_points)
            centroids.append((x, y))

        # if centroids converge, we're done
        if set(centroids) == set(clusters.keys()):
            break

        # if initial centroid choice is bad and leads to convergence,
        # repopulate
        if len(centroids) < n:
            centroids += sample(points, 1)

    return clusters, error



# generate test data
seed_val = randint(0, 1000)
seed(seed_val)
print('seeded with ', seed_val)

CENTROID_COUNT = 3
CENTROID_RANGE = 1000
CLUSTER_SIZE = 300
CLUSTER_VARIANCE = 10

centroids = []
points = []
for i in range(CENTROID_COUNT):
    # pick centroid
    x = randint(0, CENTROID_RANGE)
    y = randint(0, CENTROID_RANGE)
    centroids.append((x, y))

    # generate points around that centroid
    for j in range(CLUSTER_SIZE):
        px = x + randint(-CLUSTER_VARIANCE, CLUSTER_VARIANCE)
        py = y + randint(-CLUSTER_VARIANCE, CLUSTER_VARIANCE)

        points.append((px, py))


# run clustering algorithm
print(sorted(centroids))
res, error = cluster(points, CENTROID_COUNT)
print(sorted(res))


# to improve accuracy, run a few times and use result with least error
for i in range(5):
    next_res, next_error = cluster(points, CENTROID_COUNT)
    if next_error < error:
        res = next_res
        error = next_error
print(sorted(res))
