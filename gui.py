import tkinter as tk
from tkinter import ttk, messagebox
import threading
from api_client import get_vendor_info # Importa nossa função de busca

class MacLookupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscar Fabricante G6")
        # MUDANÇA: Janela significativamente menor
        self.root.geometry("300x165") 
        self.root.resizable(False, False)

        self._setup_styles()
        self._create_widgets()

    def _setup_styles(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 9)) # MUDANÇA: Fonte um pouco menor nos rótulos
        style.configure("TButton", font=("Segoe UI", 9, "bold")) # MUDANÇA: Fonte um pouco menor no botão
        style.configure("TEntry", font=("Segoe UI", 9))
        style.configure("TCheckbutton", font=("Segoe UI", 8)) # MUDANÇA: Fonte um pouco menor no checkbox

    def _create_widgets(self):
        # MUDANÇA: Menos preenchimento interno
        main_frame = ttk.Frame(self.root, padding="8 8 8 8")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # MUDANÇA: Menos espaço vertical
        ttk.Label(main_frame, text="Endereço MAC:").pack(pady=(0, 4))
        
        # MUDANÇA: Campo de entrada mais curto
        self.mac_entry = ttk.Entry(main_frame, width=30)
        self.mac_entry.pack()

        self.search_button = ttk.Button(main_frame, text="Buscar Fabricante", command=self._start_lookup_thread)
        # MUDANÇA: Menos espaço vertical
        self.search_button.pack(pady=8)

        # MUDANÇA: wraplength ajustado para a nova largura
        self.result_label = ttk.Label(main_frame, text="Aguardando MAC...", font=("Segoe UI", 9, "italic"), wraplength=280)
        self.result_label.pack()

        self.is_topmost = tk.BooleanVar()

        pin_checkbox = ttk.Checkbutton(
            main_frame,
            text="Fixar no topo",
            variable=self.is_topmost,
            command=self._toggle_topmost,
            style="TCheckbutton"
        )
        # MUDANÇA: Menos espaço vertical
        pin_checkbox.pack(pady=(10, 0))

    def _toggle_topmost(self):
        is_pinned = self.is_topmost.get()
        self.root.attributes('-topmost', is_pinned)

    def _start_lookup_thread(self):
        mac_address = self.mac_entry.get().strip()
        if not mac_address:
            messagebox.showwarning("Aviso", "Por favor, insira um endereço MAC.")
            return

        self.search_button.config(state=tk.DISABLED)
        self.result_label.config(text="Buscando...")
        
        thread = threading.Thread(target=self._perform_lookup, args=(mac_address,))
        thread.daemon = True
        thread.start()

    def _perform_lookup(self, mac_address):
        success, message = get_vendor_info(mac_address)
        
        if success:
            self.result_label.config(text=f"Fabricante: {message}")
        else:
            self.result_label.config(text=f"Resultado: {message}")
            
        self.search_button.config(state=tk.NORMAL)