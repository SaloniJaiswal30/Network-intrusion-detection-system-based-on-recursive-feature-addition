# Network-intrusion-detection-system-based-on-recursive-feature-addition
It’s a project in which unknown attack is detected. Detection using machine learning techniques are time consuming therefore efficient feature selection algorithm is used to make the classification process fast.
### Technology Used
Python
### Description
- Dataset Used: 100 malwar_files(zip) and hundred clean_files(zip) has been used as dataset. Features has been extracted out of it and used as an dataset using feature_extraction.py
- Ranked the datset features using CFS(Correlation feature selection) and selected good features.(ranking_n_subset.py)
- Selected beat subset using Recursive feature addition(recursive_feature_addition.py)
- classification using SVM(recursive_feature_addition.py)
