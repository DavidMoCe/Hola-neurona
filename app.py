import streamlit as st

st.image("neurona.jpg")

st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas"])

with tab1:
    st.header("Una neurona con una entrada y un peso")
    peso = st.slider("Peso", 0.0, 5.0, step=0.5, key="peso_tab1")
    numero = st.number_input("Introduzca el valor de la entrada", key="numero_tab1")
    resultado = numero * peso

    if st.button("Calcular", key="boton_0"):
        st.write("La salida de la neurona es", resultado)

with tab2:
    w_0 = st.slider("Peso w_0", 0.0, 5.0, step=0.5, key="w0_tab2")
    x_0 = st.number_input("Entrada x_0", key="x0_tab2")
    
    w_1 = st.slider("Peso w_1", 0.0, 5.0, step=0.5, key="w1_tab2")
    x_1 = st.number_input("Entrada x_1", key="x1_tab2")

    resultado = x_0 * w_0 + x_1 * w_1
    if st.button("Calcular", key="boton_1"):
        st.write("La salida de la neurona es", resultado)
with tab3:
    w_0 = st.slider("Peso w_0", 0.0, 5.0, step=0.5, key="w0_tab3")
    x_0 = st.number_input("Entrada x_0", key="x0_tab3")
    
    w_1 = st.slider("Peso w_1", 0.0, 5.0, step=0.5, key="w1_tab3")
    x_1 = st.number_input("Entrada x_1", key="x1_tab3")

    w_2 = st.slider("Peso w_2", 0.0, 5.0, step=0.5, key="w2_tab3")
    x_2 = st.number_input("Entrada x_2", key="x2_tab3")

    resultado = x_0 * w_0 + x_1 * w_1 + w_2 * x_2
    if st.button("Calcular", key="boton_2"):
        st.write("La salida de la neurona es", resultado)
