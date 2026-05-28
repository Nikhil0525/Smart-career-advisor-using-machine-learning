import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, Normalizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, Flatten, Dropout, MaxPooling1D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow as tf

# Step 1: Load and preprocess the dataset
dataset = pd.read_csv("roo_data.csv")

# Step 2: Simplify job roles into categories
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

# Step 3: Separate features and labels
data = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Step 4: Encode categorical features
labelencoder = LabelEncoder()

for i in range(13, 27):  # Assuming categorical features are in these columns
    data[:, i] = labelencoder.fit_transform(data[:, i])

# Convert all data to float32
data = data.astype(np.float32)

# Step 5: Normalize numerical features
normalizer = Normalizer()
data[:, :13] = normalizer.fit_transform(data[:, :13])

# Step 6: Encode the labels
labelencoder = LabelEncoder()
labels = labelencoder.fit_transform(labels)
labels = to_categorical(labels)  # One-hot encode the labels for CNN

# Step 7: Reshape data for CNN
data = np.expand_dims(data, axis=2)  # Adding a channel dimension

# Step 8: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Step 9: Build the CNN model
model = Sequential()

# Adding Convolutional layers
model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv1D(filters=128, kernel_size=2, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv1D(filters=256, kernel_size=2, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.2))

model.add(Flatten())

# Adding Dense layers
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(labels.shape[1], activation='softmax'))  # Output layer for multi-class classification

# Step 10: Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 11: Train the model with early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=32, callbacks=[early_stopping])

# Step 12: Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc * 100:.2f}%")

# Step 13: Save the model
model.save('cnn_model.h5')
