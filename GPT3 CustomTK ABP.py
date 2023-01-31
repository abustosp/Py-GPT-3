
import openai
import customtkinter as ctk
from PIL import Image
import os

# Inicializar OpenAI
openai.api_key = "YOUR API KEY"

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Crear la clase App
class App(ctk.CTk):

    # Inicializar la clase
    def __init__(self):
        
        # Inicializar la clase padre
        super().__init__()

        # Crear la ventana principal
        #self = ctk.CTk()
        self.title("Chatbot GPT-3 OpenAI por Agustín Bustos")
        self.geometry("550x600")
        
        #Agregar el icono de la ventana principal
        self.iconbitmap("ABP.ico")

        #definir el layout de 3 columnas por 4 filas
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1 , weight=1 , minsize=350)
        self.grid_rowconfigure(0 , weight=1)
        self.grid_rowconfigure(1 , weight=1 , minsize=200)
        self.grid_rowconfigure(2 , weight=1)
        self.grid_rowconfigure(3 , weight=1 , minsize=150)
        self.grid_rowconfigure(4 , weight=1)

        #hacer que la columna 0 tenga un tamaño fijo de 40 y no se pueda cambiar
        self.grid_columnconfigure(0 , minsize=40 , weight=0)


        #Agregar un cuadro con el logo
        self.logo = ctk.CTkImage(Image.open("ABP blanco sin fondo.png") , size=(40 , 40))
        self.logo_imagen = ctk.CTkLabel(self, text="", image=self.logo)
        self.logo_imagen.grid(row=0, column=0, pady=5 , padx=(10,10))

        # Crear la etiqueta para el usuario
        label_user = ctk.CTkLabel(self, text="Consulta:", width=10 , anchor="nw")

        # Crear la entrada para el usuario
        #entry_user = ctk.Entry(self, width=50)
        entry_user = ctk.CTkTextbox(self, height=20 , wrap=ctk.WORD)

        # Crear la etiqueta para el chatbot
        label_bot = ctk.CTkLabel(self, text="GPT-3:" , anchor="nw" , width=10 )
        label_bot.grid(row=1, column=0, pady=5 , padx=(20,20) , sticky="nw")

        # Crear la entrada de tipo ctk.text para el chatbot y que se autoajuste al tamaño de la ventana
        entry_bot = ctk.CTkTextbox(self , height=20 , wrap=ctk.WORD )

        # Crear la entrada para el chatbot
        entry_bot.grid(row=1, column=1, pady=5 , padx=(10,10) , sticky="nsew")
        label_user.grid(row=3, column=0, pady=5 , padx=(20,20) , sticky="nw" )
        entry_user.grid(row=3, column=1, pady=5 , padx=(10,10) , sticky="nsew")

        # Función para el botón de enviar
        def send_message():
            # Obtener el texto de entry_user
            user_input = entry_user.get("1.0", "end")
            # Obtener la entrada del usuario
            #user_input = entry_user.get()
            # Limpiar la entrada del usuario
            entry_user.delete("0.0", ctk.END)
            # Generar la respuesta del chatbot
            response = openai.Completion.create(engine="text-davinci-003", prompt=user_input, max_tokens=2048 , temperature=0.4)
            # Mostrar la respuesta del chatbot
            entry_bot.insert(ctk.END, f"Usuario: \n{user_input}\n")
            entry_bot.insert(ctk.END,  f"Chatbot: {response['choices'][0]['text']}\n\n\n")
            # Almacenar la pregunta y respuesta en un archivo de texto
            with open("chatbot_log.txt", "a") as f:
                f.write(f"Usuario: \n{user_input}\n")
                f.write(f"Chatbot: {response['choices'][0]['text']}\n\n\n")

        # Crear el botón de enviar
        button_send = ctk.CTkButton(self, text="Consultar", command=send_message)
        button_send.grid(row=4 , column=1 , pady=10 , padx=(10,10))

        # Crear el botón Importar archivo chatbot_log.txt y asignar el texto en entry_bot.insert, se tiene que seleccionar el archivo chatbot_log.txt en el explorador de archivos
        def importar():
            #borrar el contenido de entry_bot
            entry_bot.delete("0.0", ctk.END)
            file = ctk.filedialog.askopenfilename(initialdir=os.getcwd(), title="Seleccionar archivo", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
            with open(file, "r") as f:
                entry_bot.insert(ctk.END, f.read())

        # Crear el botón de importar (de color rojo)
        button_import = ctk.CTkButton(self, text="Importar", command=importar , fg_color="#62f56e" , hover_color='#2d7332' , text_color='#353535' )
        button_import.grid(row=0 , column=1 , pady=10 , padx=(10,10))


# Inicia el bucle principal de la ventana
if __name__ == "__main__":
    app = App()
    app.mainloop()