import streamlit as st
import pandas as pd
from ucimlrepo import fetch_ucirepo

def fetch_dataset(uci_id):
    dataset_namespace = fetch_ucirepo(id=uci_id)
    X = dataset_namespace.data.features
    y = dataset_namespace.data.targets
    # st.subheader("Features")
    # st.dataframe(X)
    # st.subheader("Target")
    # st.dataframe(y)
    return X,y



def display_dataframe():
    df_books = pd.read_csv("../resourceFiles/datasets/diabetes_binary_5050split_health_indicators_BRFSS2015.csv")
    st.title("View Tabular Data")
    st.dataframe(df_books)

if __name__ == "__main__":
    # st.title("Analyse Tabular Data")
    # fetch_dataset(uci_id=891)
    display_dataframe()