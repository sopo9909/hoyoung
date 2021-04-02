<<<<<<< HEAD
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.tree import export_graphviz
import pydot
from IPython.core.display import Image
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
iris = load_iris()
X = iris.data[:,2:]
iris.target[:5]
np.unique(iris.target,return_counts=True)
y=iris.target
tree = DecisionTreeClassifier(max_depth =2)
tree.fit(X,y)
dot_data=export_graphviz(tree,out_file=None,feature_names=iris.feature_names[2:],class_names=iris.target_names,rounded =True,filled =True,impurity=True)
import pydotplus
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris.png")
Image("iris.png")
# graph = pydot.graph_from_dot_file("iris.dot")[0]
# iris_png = graph.create_png()
# Image(iris_png)
X1 = iris.data[:,:-2]
iris.target[:5]
np.unique(iris.target,return_counts=True)
y1=iris.target
tree = DecisionTreeClassifier(max_depth =4)
tree.fit(X1,y1)
dot_data=export_graphviz(tree,out_file=None,feature_names=iris.feature_names[:-2],class_names=iris.target_names,rounded =True,filled =True,impurity=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris1.png")
Image("iris1.png")
=======
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.tree import export_graphviz
import pydot
from IPython.core.display import Image
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
iris = load_iris()
X = iris.data[:,2:]
iris.target[:5]
np.unique(iris.target,return_counts=True)
y=iris.target
tree = DecisionTreeClassifier(max_depth =2)
tree.fit(X,y)
dot_data=export_graphviz(tree,out_file=None,feature_names=iris.feature_names[2:],class_names=iris.target_names,rounded =True,filled =True,impurity=True)
import pydotplus
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris.png")
Image("iris.png")
# graph = pydot.graph_from_dot_file("iris.dot")[0]
# iris_png = graph.create_png()
# Image(iris_png)
X1 = iris.data[:,:-2]
iris.target[:5]
np.unique(iris.target,return_counts=True)
y1=iris.target
tree = DecisionTreeClassifier(max_depth =4)
tree.fit(X1,y1)
dot_data=export_graphviz(tree,out_file=None,feature_names=iris.feature_names[:-2],class_names=iris.target_names,rounded =True,filled =True,impurity=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris1.png")
Image("iris1.png")
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
