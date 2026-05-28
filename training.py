import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, Normalizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_curve, accuracy_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess the dataset
dataset = pd.read_csv("dataset.csv")

# Simplify job roles into categories
def simplify_job_roles(dataset):
    job_role_mapping = {
        'Network Admin': ['Network Security Administrator', 'Network Engineer', 'Network Security Engineer'],
        'Business Analyst': ['Business Systems Analyst', 'Business Intelligence Analyst', 'CRM Business Analyst'],
        'Database Developer': ['Database Manager', 'Database Administrator'],
        'IT Admin': ['Information Security Analyst', 'Information Technology Auditor', 'Information Technology Manager'],
        'Software Engineer': ['Software Systems Engineer', 'Software Developer', 'Software Quality Assurance (QA) / Testing'],
        'Technical Engineer': ['CRM Technical Developer', 'Technical Support', 'Technical Services/Help Desk/Tech Support'],
        'Data Architect': ['Solutions Architect'],
        'UX Designer': ['Design & UX'],
        'Administrator': ['Portal Administrator', 'Systems Security Administrator'],
        'Applications Developer': ['Mobile Applications Developer']
    }

    for new_role, old_roles in job_role_mapping.items():
        dataset['Suggested Job Role'].replace(old_roles, new_role, inplace=True)

simplify_job_roles(dataset)

# Separate features and labels
data = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Convert categorical columns to numeric if necessary
for i in range(data.shape[1]):
    if data[:, i].dtype == 'object':
        labelencoder = LabelEncoder()
        data[:, i] = labelencoder.fit_transform(data[:, i])

# Normalize numerical features
normalizer = Normalizer()
data = normalizer.fit_transform(data)

# Encode the labels
labelencoder = LabelEncoder()
labels = labelencoder.fit_transform(labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the model
joblib.dump(clf, 'filename3.pkl')

# Evaluate the model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Generate and save graphs
# 1. Feature Importance Graph
feature_importances = clf.feature_importances_
features = [f'Feature {i}' for i in range(len(feature_importances))]
plt.figure(figsize=(12, 6))
sns.barplot(x=feature_importances, y=features, palette='viridis')
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.savefig('feature_importance.png')
plt.show()

# 2. Dataset Distribution Graph
plt.figure(figsize=(10, 6))
sns.countplot(x=dataset['Suggested Job Role'])
plt.xticks(rotation=90)
plt.xlabel('Job Role')
plt.ylabel('Count')
plt.title('Dataset Distribution by Job Role')
plt.savefig('dataset_distribution.png')
plt.show()

# 3. Pie Chart of Class Distribution in Test Set
class_labels = labelencoder.inverse_transform(np.unique(labels))
class_counts = np.bincount(y_test)
plt.figure(figsize=(8, 8))
plt.pie(class_counts, labels=class_labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title('Class Distribution in Test Set')
plt.savefig('class_distribution_pie_chart.png')
plt.show()

# 4. Fake Confusion Matrix
def generate_fake_data(num_classes=3):
    conf_matrix = np.zeros((num_classes, num_classes), dtype=int)
    np.fill_diagonal(conf_matrix, [1000, 800, 900])  # High correct predictions
    conf_matrix[0, 1] = conf_matrix[1, 2] = conf_matrix[2, 0] = 50  # Few misclassifications
    return conf_matrix

conf_matrix = generate_fake_data()
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 1', 'Class 2', 'Class 3'], yticklabels=['Class 1', 'Class 2', 'Class 3'])
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Fake Confusion Matrix')
plt.savefig('fake_confusion_matrix.png')
plt.show()

# 5. Fake Precision-Recall Curve
recall = np.linspace(0, 1, 100)
precision = np.linspace(0.9, 1, 100)  # High precision
plt.figure(figsize=(10, 7))
plt.plot(recall, precision, marker='.')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Fake Precision-Recall Curve')
plt.savefig('fake_precision_recall_curve.png')
plt.show()

# 6. Fake Accuracy Image
accuracy = 0.95  # High accuracy value
plt.figure(figsize=(6, 4))
plt.bar(['Accuracy'], [accuracy], color='blue')
plt.ylim([0, 1])
plt.ylabel('Accuracy')
plt.title('Fake Model Accuracy')
plt.savefig('fake_accuracy.png')
plt.show()
