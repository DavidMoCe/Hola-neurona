# ¡Hola Neurona! 🌟🤖

## 🌍 Choose Your Language / Elige tu idioma:
- [English](#english-)
- [Español](#español-)

---

## Project URL 🌐

You can access the project at the following URL:  
[**Neuron Simulator URL**](https://simuladorneurona-david.streamlit.app/)

## English 🇬🇧






---

## Español 🇪🇸

Este es un proyecto interactivo utilizando **Streamlit** que simula el comportamiento de una neurona con diferentes configuraciones de entradas y pesos. A través de una interfaz web, puedes ver cómo cambia la salida de la neurona al ajustar los valores de entrada y peso.🚀

## Requisitos 📦

Para ejecutar este proyecto, necesitas tener instalado **Python 3** y las siguientes bibliotecas:

- `streamlit`

Puedes instalar las dependencias ejecutando el siguiente comando:

```bash
pip install streamlit
```

## Instrucciones para ejecutar 🖥️
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```
2. Ejecuta el archivo de Streamlit con el siguiente comando:
   ```bash
   streamlit run app.py
   ```
   Reemplaza `app.py` con el nombre del archivo donde guardaste el código si es diferente.
3. Se abrirá una página en tu navegador donde podrás interactuar con la aplicación. 🌐

## Descripción de la Aplicación 🧠
La aplicación tiene tres pestañas, cada una con un modelo de neurona diferente:

### 1. Una neurona con una entrada y un peso 🔢⚖️
- Permite ingresar un valor para la entrada y un peso.
- La salida de la neurona se calcula multiplicando la entrada por el peso.
- Puedes ajustar el peso y el valor de entrada usando controles deslizantes y un campo numérico.
- Un botón de "Calcular" mostrará la salida.

### 2. Una neurona con dos entradas y dos pesos 2️⃣➕2️⃣
- Aquí puedes ingresar dos valores de entrada y dos pesos.
- La salida se calcula como la suma de las entradas multiplicadas por sus respectivos pesos: `x_0 * w_0 + x_1 * w_1`.
- Similar al primer modelo, ajusta los valores con deslizadores y campos de entrada.

### 3. Una neurona con tres entradas, tres pesos y un bias de 10 🔢⚖️+🔟
- En este modelo, puedes ingresar tres valores de entrada y tres pesos.
- La salida se calcula como: `x_0 * w_0 + x_1 * w_1 + x_2 * w_2 + 10`.
- Un valor de bias fijo de 10 se añade al resultado.

## Licencia 📄
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.



