import seaborn as sns
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm
from typing import List


def analyze(all_sents: List[List[str]]):
    model = SentenceTransformer('all-mpnet-base-v2')
    repeats = [len(sents) - len(set(sents)) for sents in all_sents]
    print("Repeats:", repeats)
    embs = [model.encode(list(set(sents))) for sents in all_sents]

    cosine_sims = [[np.dot(np.mean(emb_a, axis=0), np.mean(emb_b, axis=0)) /
                    (norm(np.mean(emb_a, axis=0)) * norm(np.mean(emb_b, axis=0))) for emb_a in embs] for emb_b in embs]

    # print(cosine_sims)
    # for i in range(len(emb)):
    #     for j in range(i + 1, len(emb)):
    #         c1_mean = np.mean(emb[i], axis=0)
    #         c2_mean = np.mean(emb[j], axis=0)
    #         print(len(c1_mean), len(emb[i]))
    #         print(len(c2_mean), len(emb[j]))
    #         cosine = np.dot(c1_mean, c2_mean) / (norm(c1_mean) * norm(c2_mean))
    #         print(i, "-", j, cosine)

    flat_emb = np.concatenate(embs, axis=0)

    pca = PCA(n_components=2)
    pca.fit(flat_emb)
    emb_pca = pca.transform(flat_emb)
    labels = []
    for i in range(len(all_sents)):
        labels += [i for _ in range(len(set(all_sents[i])))]
    plt.figure(figsize=(10,7))
    sns.scatterplot(x=emb_pca[:, 0], y=emb_pca[:,1], hue=labels, palette=['purple', 'blue', 'red'])
    plt.show()

    return cosine_sims, repeats
