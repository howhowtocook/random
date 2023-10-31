########################################################################
#Call required libraries
from sklearn import datasets
import numpy as np            # Data manipulation
import pandas as pd           # Dataframe manipulatio
import matplotlib.pyplot as plt              # For graphics
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture #For GMM clustering
from sklearn import metrics
from sklearn.decomposition import PCA
from scipy.spatial import ConvexHull


# load data
iris = datasets.load_iris() 
data = pd.DataFrame(iris.data)
pca=PCA().fit(data) # 降维后的数据只用于最后画图
print('方差累计贡献率为{}'.format(np.cumsum(pca.explained_variance_ratio_))) #取前两个
data_pca = pca.fit_transform(data)
y = iris.target


#Scaling of data
data_scaled = data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
#K means Clustering
ncluster = np.unique(y).shape[0]
Kmeans = KMeans(ncluster)
Kmeans.fit(data_scaled)
data.insert(0,'kmeans',pd.DataFrame(Kmeans.predict(data_scaled)))
# Agglomerative Clustering
agg = AgglomerativeClustering(ncluster, affinity = 'euclidean', linkage = 'ward')
data.insert(0,'agglomerative',pd.DataFrame(agg.fit_predict(data_scaled)))

#Guassian Mixture 
ModellingGuassian = GaussianMixture(n_components=ncluster,init_params='kmeans')
data.insert(0,'Guassian',pd.DataFrame(Guassian.fit_predict(data_scaled)))

#orignal
data.insert(0,'label',pd.DataFrame(y))


#Plot the clusters 
def ScatterWithBoundries(thecol,subplot):
    ax = fig.add_subplot(2,2,subplot)
    colors = ['red', 'black', 'blue', 'green', 'orange', 'pink']    
    scatter = plt.scatter(data_pca[:,0], data_pca[:,1], c=data[thecol], s=2, cmap='rainbow')    
    plt.title(thecol)        
    for i in np.unique(data[thecol]):    
        points = np.array(data_pca[:,:2][data[thecol] == i])        
        hull = ConvexHull(points)    
            for simplex in hull.simplices:            
            	plt.plot(points[simplex, 0], points[simplex, 1], 'k-', color=colors[i], linewidth=1.5)
            	
fig = plt.figure()
ScatterWithBoundries('label',1)
ScatterWithBoundries('Guassian',2)
ScatterWithBoundries('agglomerative',3)
ScatterWithBoundries('kmeans',4)
plt.show()
