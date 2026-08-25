import psutil
from monitor.bytes_2_gb import bytes_converter

def get_memory_info():
    # Retorna a quantidade de memória virtual disponível, usada, livre, etc.
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()    
    return {
        "memoria" : {
            "total_ram" : bytes_converter(mem.total),
            "usada_ram" : bytes_converter(mem.used),
            "disponivel_ram" : bytes_converter(mem.available),
            "percentual_ram_uso" : mem.percent
        },
        "swap" : {
            "total_swap" : bytes_converter(swap.total),
            "usada_swap" : bytes_converter(swap.used),
        }
    }

# # MEMORIA ---------------------------------------------------------------------------------
# # Retorna a quantidade de memória virtual disponível, usada, livre, etc.
# memoria = psutil.virtual_memory()
# print("Memoria: ",memoria)
