#-------------------------------------------------------------------------
# AUTHOR: Chanrady Ho
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: 2 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
instance = []
for i in range(len(db)):
    # Age conversion
    if db[i][0] == "Young":
        instance.append(1)
    elif db[i][0] == "Presbyopic":
        instance.append(2)
    else:
        instance.append(3)
    # Spectacle prescription conversion
    if db[i][1] == "Myope":
        instance.append(1)
    else:
        instance.append(2)
    # Astigmatism conversion
    if db[i][2] == "Yes":
        instance.append(1)
    else:
        instance.append(2)
    # Tear Production Rate conversion
    if db[i][3] == "Reduced":
        instance.append(1)
    else:
        instance.append(2)
    X.append(instance)
    instance = []
print(X)

#transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
for i in range(len(db)):
    # Age conversion
    if db[i][4] == "Yes":
        Y.append(1)
    else:
        Y.append(2)
print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy', )
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()