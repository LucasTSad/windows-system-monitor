import psutil
from monitor.bytes_2_gb import bytes_converter

class MonitorMemoria:

    def __init__(self):
        mem_start = psutil.virtual_memory()
        swap_start = psutil.swap_memory()

        self.total_ram = bytes_converter(mem_start.total)
        self.total_swap = bytes_converter(swap_start.total)


    ## Retorna as informações de memória RAM do sistema;
    ## e confere se está ativo
    def _get_ram_checker(self):
        ram = psutil.virtual_memory()
        ram_info = {}
        if ram.total == 0:
            ram_info = "N/A"
        else:
            ram_info = {
                "total_ram" : self.total_ram,
                "usada_ram" : bytes_converter(ram.used),
                "disponivel_ram" : bytes_converter(ram.available),
                "percentual_ram_uso" : ram.percent
            }

        return ram_info

    ## Retorna as informações de memória swap do sistema;
    ## e confere se está ativo
    def _get_swap_checker(self):
        swap = psutil.swap_memory()
        swap_info = {}
        if swap.total == 0:
            swap_info = "N/A"
        else:
            swap_info = {
                "total_swap" : self.total_swap,
                "usada_swap" : bytes_converter(swap.used),
                "percentual_swap_uso" : swap.percent
            }

        return swap_info

    ## Retorna as informações de memória RAM e swap do sistema;
    def get_memory_info(self):
        ram_info = self._get_ram_checker()
        swap_info = self._get_swap_checker()

        return {
            "memoria" : ram_info,
            "swap" : swap_info
        }

# # MEMORIA ---------------------------------------------------------------------------------
# # Retorna a quantidade de memória virtual disponível, usada, livre, etc.
# memoria = psutil.virtual_memory()
# print("Memoria: ",memoria)
