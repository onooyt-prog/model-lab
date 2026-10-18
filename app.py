from styling import apply_styles
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title='model-lab',
    layout = 'wide'
)
apply_styles()

st.title('model-lab 🔥')
st.write('Train, compare, and experiment with machine-learning models.')


wine = load_wine(as_frame = True)
X = wine.data
y = wine.target
class_names = list(wine.target_names)

st.sidebar.header('Experimental settings')

model_name = st.sidebar.selectbox(
    'Chose a model',
    [
        'Random Forest',
        'Logistic Regression',
        'K-Nearest Neighbours',
        'Decision Tree'
    ],
)

test_size = st.sidebar.slider(
    'Test data (%)',
    min_value = 10,
    max_value = 40,
    value = 25,
    step = 5,
)


random_seed = st.sidebar.slider(
    'Random Seed',
    min_value = 1,
    max_value = 100,
    value = 42,
)

st.sidebar.subheader('Model parameters')


if model_name == "Random Forest":
    n_estimators = st.sidebar.slider(
        "Number of trees", 10, 300, 100, 10
    )
    max_depth = st.sidebar.slider(
        "Maximum depth (0 = unlimited)", 0, 20, 0
    )

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth or None,
        random_state=random_seed,
    )

elif model_name == "Logistic Regression":
    C = st.sidebar.select_slider(
        "Regularization strength (C)",
        options=[0.01, 0.1, 1.0, 10.0, 100.0],
        value=1.0,
    )

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(C=C, max_iter=2000),
    )

elif model_name == "K-Nearest Neighbours":
    n_neighbors = st.sidebar.slider(
        "Number of neighbors (K)", 1, 20, 5
    )

    model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=n_neighbors),
    )

else:
    max_depth = st.sidebar.slider(
        "Maximum depth (0 = unlimited)", 0, 20, 0
    )

    model = DecisionTreeClassifier(
        max_depth=max_depth or None,
        random_state=random_seed,
    )

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=random_seed, stratify=y)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

precision = precision_score(y_test, predictions, average='weighted', zero_division=0)
#la recall si f1 mereu z_d=0!!!
recall = recall_score(y_test, predictions, average='weighted', zero_division=0)

f1 = f1_score(y_test, predictions, average='weighted', zero_division=0)

st.subheader('Dataset overview')

col1, col2, col3 = st.columns(3)
col1.metric('Samples', len(X))
col2.metric('Features', X.shape[1])
col3.metric('Classes', len(class_names))

with st.expander('Explore the dataset'):
    st.write('Each row represents a wine sample. The target is its wine class.')
    st.dataframe(X.assign(
        wine_class=[class_names[i] for i in y]
    ), use_container_width = True)

st.subheader(f"Results - {model_name}")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", f"{accuracy:.1%}")
col2.metric("Precision", f"{precision:.1%}")
col3.metric("Recall", f"{recall:.1%}")
col4.metric("Weighted F1", f"{f1:.1%}")

left, right = st.columns(2)

with left:
    st.subheader('Confusion matrix')
    matrix = confusion_matrix(y_test, predictions)
    fig, ax = plt.subplots(figsize=(5, 4))
    image = ax.imshow(matrix, cmap = 'Blues')
    fig.colorbar(image, ax=ax)

    ax.set(
        xticks=range(len(class_names)),
        yticks=range(len(class_names)),
        xticklabels=class_names,
        yticklabels=class_names,
        xlabel="Predicted class",
        ylabel="Actual class",
    )
    plt.setp(ax.get_xticklabels(), rotation=25, ha="right")

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            ax.text(col, row, matrix[row, col], ha="center", va="center")

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.subheader("Model information")
    st.write(f"**Algorithm:** {model_name}")
    st.write(f"**Training samples:** {len(X_train)}")
    st.write(f"**Test samples:** {len(X_test)}")
    st.write(f"**Random seed:** {random_seed}")

    st.info(
        "Change the settings in the sidebar to retrain the model "
        "and see how its performance changes."
    )

st.subheader("Test predictions")

results = pd.DataFrame({
    "actual_class": [class_names[i] for i in y_test],
    "predicted_class": [class_names[i] for i in predictions],
    "correct": y_test.to_numpy() == predictions,
})

st.dataframe(results.head(10), use_container_width=True)

st.download_button(
    "Download all predictions as CSV",
    data=results.to_csv(index=False).encode("utf-8"),
    file_name="model_predictions.csv",
    mime="text/csv",
)

st.caption(
    "model-lab • Built with Python, Streamlit, and scikit-learn"
)