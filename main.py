import tkinter as tk
from tkinter import filedialog, scrolledtext

def open_file():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Todos los archivos", "*.*"), ("Archivos de texto", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)  # Limpiar el área de texto
                text_area.insert(tk.INSERT, content)  # Insertar contenido
        except Exception as e:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.INSERT, f"Error al abrir el archivo:\n{e}")

# Crear ventana principal
root = tk.Tk()
root.title("Explorador de Archivos")
root.geometry("600x400")
root.iconbitmap("compilador.ico")


# Botón para abrir archivo
btn_open = tk.Button(root, text="Abrir Archivo", command=open_file)
btn_open.pack(pady=10)

# Área de texto con scroll
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Ejecutar la aplicación
root.mainloop()


import sysconfig; print(sysconfig.get_path("scripts"))
import site; print(site.USER_BASE + "\\Scripts")