import psutil
from monitor.bytes_2_gb import bytes_converter

class MonitorMemoria:

    def __init__(self):
        mem_start = psutil.virtual_memory()
        swap_start = psutil.swap_memory()

        self.total_ram = bytes_converter(mem_start.total)
        self.total_swap = bytes_converter(swap_start.total)

    def get_memory_info(self):
    # Retorna a quantidade de memória virtual disponível, usada, livre, etc.
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()

        return {
            "memoria" : {
                "total_ram" : self.total_ram,
                "usada_ram" : bytes_converter(mem.used),
                "disponivel_ram" : bytes_converter(mem.available),
                "percentual_ram_uso" : mem.percent
            },
            "swap" : {
                "total_swap" : self.total_swap,
                "usada_swap" : bytes_converter(swap.used),
                "percentual_swap_uso" : swap.percent
            }
        }

# # MEMORIA ---------------------------------------------------------------------------------
# # Retorna a quantidade de memória virtual disponível, usada, livre, etc.
# memoria = psutil.virtual_memory()
# print("Memoria: ",memoria)
