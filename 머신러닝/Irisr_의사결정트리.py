<<<<<<< HEAD
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.tree import export_graphviz
import pydot
from IPython.core.display import Image
import os
from sklearn.model_selection import train_test_split
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
iris = load_iris()
X = iris.data
iris.target[:5]
np.unique(iris.target,return_counts=True)
y=iris.target
X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=123)
tree = DecisionTreeClassifier(max_depth =2)
tree.fit(X_train,y_train)
dot_data=export_graphviz(tree,out_file=None,feature_names=iris.feature_names,class_names=iris.target_names,rounded =True,filled =True,impurity=True)
import pydotplus
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris2.png")
Image("iris2.png")
=======
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.tree import export_graphviz
import pydot
from IPython.core.display import Image
import os
from sklearn.model_selection import train_test_split
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
iris = load_iris()
X = iris.data
iris.target[:5]
np.unique(iris.target,return_counts=True)
y=iris.target
X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=123)
tree = DecisionTreeClassifier(max_depth =2)
tree.fit(X_train,y_train)
dot_data=export_graphviz(tree,out_file=None,feature_names=iris.feature_names,class_names=iris.target_names,rounded =True,filled =True,impurity=True)
import pydotplus
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris2.png")
Image("iris2.png")
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
