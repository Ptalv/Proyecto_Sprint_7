
import pandas as pd
import numpy as np

import plotly.express as px
import streamlit as st

# Cargar los datos
df = pd.read_csv(
    "https://raw.githubusercontent.com/jsaraujott/datos/refs/heads/main/iris.csv")
df["type"] = df["type"].astype(str)

# Titulo de nuestro reporte
st.header("Relacion de variables", divider="gray")
# Boton para decargar datasets
st.download_button(
    label="Descargar Datasets",
    data=df.to_csv(index=False),
    file_name="iris.csv"
)

# Seleccionador de variables
opciones_posibles = list(df.columns)[0:4]

v = st.multiselect(
    label="Seleccione maximo 2 variables",
    options=opciones_posibles,
    max_selections=2
)
# Boton para ejecutar el analisis
analisis_b = st.button(
    label="Analizar"
)

# Analisis de relacion
if analisis_b:
    try:

        col1, col2 = st.columns(2)

        with col1:
            hist_plot01 = px.histogram(
                df, x=v[0], title=f"Distribucion de {v[0]}", color="type")
            st.plotly_chart(hist_plot01, use_container_width=True)

            c1, c2, c3 = st.columns(3)

            with c1:
                prom1 = np.mean(df[v[0]])
                st.metric(
                    label="Media",
                    value="{}".format(round(prom1, 1))
                )

            with c2:
                med1 = np.median(df[v[0]])
                st.metric(
                    label="Mediana",
                    value="{}".format(round(med1, 1))
                )
            with c3:
                desv1 = np.std(df[v[0]])
                st.metric(
                    label="Desviacion",
                    value="{}".format(round(desv1, 1))
                )

        with col2:
            hist_plot02 = px.histogram(
                df, x=v[1], title=f"Distribucion de {v[1]}", color="type")
            st.plotly_chart(hist_plot02, use_container_width=True)

            c4, c5, c6 = st.columns(3)

            with c4:
                prom2 = np.mean(df[v[1]])
                st.metric(
                    label="Media",
                    value="{}".format(round(prom2, 1))
                )

            with c5:
                med2 = np.median(df[v[1]])
                st.metric(
                    label="Mediana",
                    value="{}".format(round(med2, 1))
                )
            with c6:
                desv2 = np.std(df[v[1]])
                st.metric(
                    label="Desviacion",
                    value="{}".format(round(desv2, 1))
                )

        disp_plot = px.scatter(
            df, x=v[0], y=v[1], color="type", title=f"Dispersion {v[1]} vs {v[0]}")
        st.plotly_chart(disp_plot, use_container_width=True)
        correl = np.corrcoef(df[v[0]], df[v[1]])
        st.metric(
            label="Correlacion de Pearson",
            value="{}%".format(round(correl[0, 1]*100, 1))
        )
    except:

        st.write("Faltan Variables Por Seleccionar")
