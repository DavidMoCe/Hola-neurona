import streamlit as st

st.image("neurona.jpg")

st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas"])

with tab1:
    st.header("Una neurona con una entrada y un peso")
    peso = st.slider("Peso", 0, 5)
    numero = st.number_input("Introduzca el valor de la entrada")
    resultado = numero * peso

    if st.button("Calcular"):
        st.write("La salida de la neurona es", resultado)

with tab2:
    w_0 = st.slider("Peso w_0", 0, 5)
    x_0 = st.number_input("Entrada x_0")
    
    w_1 = st.slider("Peso w_1", 0, 5)
    x_1 = st.number_input("Entrada x_1")

    resultado = x_0 * w_0 + x_1 * w_1
    if st.button("Calcular"):
        st.write("La salida de la neurona es", resultado)
with tab3:
    w_0 = st.slider("Peso w_0", 0, 5)
    x_0 = st.number_input("Entrada x_0")
    
    w_1 = st.slider("Peso w_1", 0, 5)
    x_1 = st.number_input("Entrada x_1")

    w_2 = st.slider("Peso w_2", 0, 5)
    x_2 = st.number_input("Entrada x_2")

    resultado = x_0 * w_0 + x_1 * w_1 + w_2 * x_2
    if st.button("Calcular"):
        st.write("La salida de la neurona es", resultado)