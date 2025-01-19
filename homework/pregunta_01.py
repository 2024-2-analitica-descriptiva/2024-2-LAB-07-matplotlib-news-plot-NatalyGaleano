"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Crear carpeta 'files/plots' si no existe
    output_dir = os.path.abspath("./files/plots")  # Ruta absoluta
    if not os.path.exists(output_dir):
        print(f"Creando la carpeta: {output_dir}")
        os.makedirs(output_dir)

# Se agrega la figura vacia 
    plt.figure()
    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue", #Azul de tablut
        "Radio": "lightgrey",
        }
    
    #Se agrega diccionario para que la linea que predomina quede por encima de las otras lineas
    zorder = { 
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }
    # cambio de grosor de la linea

    linewidths = {

        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    # Se lee el archivo
    df = pd.read_csv("files/input/news.csv", index_col=0)
# Se itera por cada columna del dataframe y se le pone la etiqueta con el nombre de la columna. 
    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col],
        )
     # Se agrega el titulo 
    
    plt.title("How people get their news", fontsize=16)
    # ELiminar linea superior derecha de la grafica y la izquierda, para darle mas orden 

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    # organizar los valores de la parte izq. 
    plt.gca().axes.get_yaxis().set_visible(False)

    #vamos a organizar la linea izq como porcentje con el ciclo for. 

    for col in df.columns:
        first_year= df.index[0]
        plt.scatter(
            x=first_year,#primer año
            y=df[col][first_year],# de la columna por cada año
            color=colors[col],
            zorder=zorder[col],
        )

    #vamos  poner la fuente de noticias como el valor en % al inicio  

        plt.text (
            first_year -0.2,
            df[col][first_year],
            col+" " + str(df[col][first_year]) +"%",
            ha="right",
            va="center",
            color=colors[col],
        )
        
    
        





    #Vamos a hacer lo mismo al lado derecho
        last_year = df.index[-1]
        plt.scatter(
            x=last_year,#primer año
            y=df[col][last_year],# de la columna por cada año
            color=colors[col],
            zorder=zorder[col],
        )
#vamos a poner la fuente con el valor % al final 
        plt.text (
            last_year + 0.2,
            df[col][last_year],
            col+" " + str(df[col][last_year]) +"%",
            ha="left",
            va="center",
            color=colors[col],
        )
    


    #--------------------
    # Se agrega una leyenda para poder identificar a que hace parte cada color. 
    # plt.legend(loc="upper right")_ Dado que esto muestra una grafica que no resalta bien cual es la fuente que
    #  viene creciendo para ver noticias vamos a eliminarla y 
    #  vamos a organizar la información de tal forma que 
    # los colores nos ayuden a resltar cual es la funte 
    # que ha venido creciendo. 
    # Se usa para ir mostrando como va quedando la gráfica
# Para identificar los colores se hace primero que el for
 #----------------------------------

# Agregar todos los años.

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha="center",

    )
    #Finalmente se guarda como PNG

    
    output_path = os.path.join(output_dir, "news.png")

    try:
        plt.tight_layout()
        plt.savefig(output_path)
        print(f"Gráfico guardado en: {output_path}")
    except Exception as e:
        print(f"Error al guardar el gráfico: {e}")

    return 

print(pregunta_01())
    
    





    