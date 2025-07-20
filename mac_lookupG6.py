# mac_lookupG6.py
# Ponto de entrada principal da aplicação. Executa este arquivo para iniciar.

import tkinter as tk
from gui import MacLookupApp # Importa a classe da nossa interface

if __name__ == "__main__":
    # Cria a janela principal
    root_window = tk.Tk()
    
    # Cria uma instância da nossa aplicação, passando a janela
    app = MacLookupApp(root_window)
    
    # Inicia o loop da interface, que a mantém aberta
    root_window.mainloop()