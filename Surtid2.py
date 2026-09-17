import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Surtid2",
    page_icon="🛒",
    layout="wide"
)

if "Productos" not in st.session_state:
    st.session_state["Productos"] = [
        {
            "ID": 1,
            "Producto": "Coca Cola",
            "Categoria": "Bebida",
            "Cantidad": 10
        },

        {
            "ID": 2,
            "Producto": "Jabon para manos",
            "Categoria": "Higiene",
            "Cantidad": 7
        },

        {
            "ID": 3,
            "Producto": "Producto adulto",
            "Categoria": "Otros",
            "Cantidad": 4
        },

        {
            "ID": 4,
            "Producto": "Comida para Gatos",
            "Categoria": "Alimentos",
            "Cantidad" : 5, 



        },

        {
            "ID": 5, 
            "Producto": "Papiel Higienico",
            "Categoria" : "Higiene",
            "Cantidad" : 9,

        },

    ]


    st.sidebar.title("Surtid2:)")

    opcion = st.sidebar.selectbox(
        "Seleccione la opciòn que mas le parezca: "

        [
            "Inicio",
            "Productos",
            "Agregar Producto",
            "Eliminar Producto",
            "Buscar Producto",
            "Ventas", 
            "Inventario",


        ]
    )


# Inicio de la Creacion de los botones q si no me pierdo pq soy gilililipollololololalalalas 
    
if opcion == "Inicio":
    st.title("Bienvenido a tu final perra judia")

    st.write(" " \
    "Sistema facil para almacenar a la guarra de tu madre" \
    "Inventario y ventas de la perra de Otman")


# Inicio con la creacion de como iran distribuido las funciones en este caso de lo que queremos moestrar 🦭
# Comenzando por las columnas 

col1,col2,col3 = st.columns(3)

total_Productos = len(st.session_state.Productos)
total_Cantidad = sum( 
    total_Productos["Cantidad"]
    for total_Productos in st.session_state.Productos)

valor_Inventario = sum(
    Productos["Precio"] * Productos["Cantidad"]
    for Productos in st.session_state.Productos

)


with col1: 
    st.metric("Productos de la puta de otman", total_Productos)


with col2:
    st.metric("Productos de la guarra de otman", total_Cantidad)

with col3:
    st.metric("Coste del Inventario"
              f"{valor_Inventario:.2f}")  # The fuck? q cojones hizo aqui esta ia de mrd
    
    st.subheader("Productos Disponibles")

    df = pd.DataFrame(st.session_state.Productos)

st.dataframe(
    df,
    use_container_width = True,
    hide_index = True, 
)



# Revisar luego pq tengo dudas con esta parte Parte de Productos

if opcion == "Productos": 

    st.title("Productos")


df = pd.DataFrame(st.session_state["Productos"])

st.dataframe(
    df,
    width = "stretch",
    hide_index= True,

)

# Parte de la Agregacion de Prodcutos 🦭

if opcion == "Agregar Productos":
    st.title("Agregar Producto")

    nombre = st.text_input("Nombre del Producto")
    categoria = st.selectbox(

    "Categoria",
    [
        "Bebidas",
        "Comida",
        "Lacteos",
        "Limpieza",
        "Panaderia"
        "Otros",

    ]        

    )

    precio = st.number_input(
        "Precio",
        min_value= 0.01,
        step = 0.1,

 )
    

    stock = st.number_input(
        "Cantidad en stock",
        min_value=0.1,
        step = 1,
    )

    # Ahora vamos con el boton 

    if st.button("Agregar Producto"):

        if nombre.strip() == "":
            st.error("Debes escribir el nombre del Producto")

        else:

            nuevo_id = 1

            if len(st.session_state.Productos) > 0: 

                nuevo_id = max(
                    Productos["ID"]
                    for Productos in st.session_state.Productos
                ) + 1


            nuevo_producto = {
                "ID": nuevo_id,
                "Producto": nombre,
                "Categoria": categoria,
                "Precio": precio, 
                "Stock": stock,
            }

            st.session_state.Productos.append(nuevo_producto)

            st.success("Producto agregado correctamente")



# Aqui iriamos con la creacion de editar el producto 







