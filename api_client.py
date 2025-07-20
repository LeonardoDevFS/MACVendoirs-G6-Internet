import requests
import config # Importa nosso arquivo de configuração

def get_vendor_info(mac_address):
    """
    Busca informações do fabricante para um dado endereço MAC.
    Retorna uma tupla: (sucesso, mensagem_ou_dado)
    """
    headers = {
        "Authorization": f"Bearer {config.API_TOKEN}"
    }
    
    try:
        url = config.API_URL.format(mac_address)
        response = requests.get(url, headers=headers, timeout=10) # <-- A CORREÇÃO É AQUI
        
        if response.status_code == 200:
            data = response.json()
            vendor = data.get("data", {}).get("organization_name", "Fabricante não encontrado")
            return (True, vendor)
        elif response.status_code == 404:
            return (False, "Endereço MAC não encontrado na base de dados.")
        else:
            return (False, f"Erro na API. Código: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return (False, "Falha na conexão com a API.")