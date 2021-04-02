<<<<<<< HEAD
import json
from flask import Flask, request, make_response
from slacker import Slacker
from inspect import Parameter
from numpy.lib.function_base import vectorize
import pandas as pd
from pandas.core.arrays import sparse
from scipy.sparse.construct import random
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score,roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression #Logistic(Regression)Classifier
from sklearn.svm import SVC #Support Vector Machine
from sklearn.naive_bayes import GaussianNB #Naive Bayesian
from sklearn.neighbors import KNeighborsClassifier #K Nearest Neighbor
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.ensemble import GradientBoostingClassifier #Gradient Boosing
from sklearn.neural_network import MLPClassifier #Neural Network
from sklearn import model_selection
from sklearn.tree import export_graphviz
import re
from numpy.core.fromnumeric import reshape
from numpy.lib.function_base import append
from sklearn.ensemble import RandomForestClassifier
from IPython.core.display import Image
from sklearn.model_selection import train_test_split
import datetime
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from numpy.lib.function_base import gradient
from IPython.core.display import Image
import numpy as np
from sklearn.preprocessing import StandardScaler
import pydotplus
from sklearn.utils.validation import check_random_state
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
from numpy.lib.function_base import gradient
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
=======
import json
from flask import Flask, request, make_response
from slacker import Slacker
from inspect import Parameter
from numpy.lib.function_base import vectorize
import pandas as pd
from pandas.core.arrays import sparse
from scipy.sparse.construct import random
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score,roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression #Logistic(Regression)Classifier
from sklearn.svm import SVC #Support Vector Machine
from sklearn.naive_bayes import GaussianNB #Naive Bayesian
from sklearn.neighbors import KNeighborsClassifier #K Nearest Neighbor
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.ensemble import GradientBoostingClassifier #Gradient Boosing
from sklearn.neural_network import MLPClassifier #Neural Network
from sklearn import model_selection
from sklearn.tree import export_graphviz
import re
from numpy.core.fromnumeric import reshape
from numpy.lib.function_base import append
from sklearn.ensemble import RandomForestClassifier
from IPython.core.display import Image
from sklearn.model_selection import train_test_split
import datetime
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from numpy.lib.function_base import gradient
from IPython.core.display import Image
import numpy as np
from sklearn.preprocessing import StandardScaler
import pydotplus
from sklearn.utils.validation import check_random_state
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
from numpy.lib.function_base import gradient
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
