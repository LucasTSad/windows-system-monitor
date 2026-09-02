import psutil

from monitor.bytes_2_gb import bytes_converter

class MonitorDisco:

    def __init__(self):
        self.usable_disks = []
        self.all_disk_sum = {}
        self.usable_disks_sum = {}
        self.total_gb_cache = {}

    ## Retorna todos os discos e os utilizaveis
    def _get_current_disk(self):
        # Retorna todos os discos
        all_disks = psutil.disk_partitions(all=True)
        # Retorna os disicos ustilizaveis
        usable_disks = [disk for disk in all_disks if 'cdrom' not in disk.opts and disk.fstype != '']
        return all_disks, usable_disks


    ## Retorna um unico disco e trata erros caso Não tenha permissão de acesso;
    ## não está conectado ou simplesmente indisponivel
    def _get_single_disk_usage(self, disk):
        sum_uso = {}
        try:
            usage = psutil.disk_usage(disk.mountpoint)

            if disk.device not in self.total_gb_cache or self.total_gb_cache[disk.device] is None:

                self.total_gb_cache[disk.device] = bytes_converter(usage.total)

            sum_uso[disk.device] = {
                    "total_gb": self.total_gb_cache.get(disk.device),
                    "used_gb": bytes_converter(usage.used),
                    "free_gb": bytes_converter(usage.free),
                    "percentual": usage.percent,
                    "status": "Online"
                    }
        except OSError as e:
            # Define o status dinamicamente checando a classe da exceção 'e'
            status_erro = "Erro de Permissao" if isinstance(e, PermissionError) else "Unidade Indisponivel"
            self.total_gb_cache[disk.device] = None
            # Evita que o script quebre caso algum disco precise de permissão de administrador
            sum_uso[disk.device] = {
                "total_gb": self.total_gb_cache.get(disk.device),
                "used_gb": None,
                "free_gb": None,
                "percentual": None,
                "status": status_erro
            }
        
        return sum_uso


    ## Cuida do conjunto de discos e sincorniza o cache
    def _get_disk_usage(self):

        current_disks = {disk.device for disk in self.usable_disks}
        cache_disks = set(self.total_gb_cache.keys())
        removed_disks = cache_disks - current_disks

        # Remove os discos que não estão mais presentes
        for disk in removed_disks:
            del self.total_gb_cache[disk]

        disks = {}
        for disk in self.usable_disks:
            disk_usage = self._get_single_disk_usage(disk)
            disks.update(disk_usage)

            
        return disks


    ## Retorna as informações do disco
    def _disk_info_builder(self,disks):
        disk_lib = {}
        for disk in disks:
                disk_lib[disk.device] = {
                    "ponto_montagem": disk.mountpoint,
                    "sistema_arquivos": disk.fstype if disk.fstype != '' else "N/A",
                    "opcoes": disk.opts
                }

        return disk_lib


    ## Retorna as informações do disco
    def get_disk_info(self):

        all_disks, usable_disks = self._get_current_disk()
        self.usable_disks = usable_disks

        self.all_disk_sum = self._disk_info_builder(all_disks)
        self.usable_disks_sum = self._disk_info_builder(usable_disks)
       
        return {
            "discos" : {
                "todos_discos" : self.all_disk_sum,
                "discos_usáveis" : self.usable_disks_sum,
            },
            "uso_disco" : self._get_disk_usage()
        }

# # DISK ---------------------------------------------------------------------------------
# # Caso Falso tenta distinguir entre discos físicos e lógicos e tenta retornar apenas os Fisicos
# # Caso True retorna todos os discos

# disco = psutil.disk_partitions(all=True)
# print("Disco: ",disco)

# # Retorna o uso do Disco
# disco_uso = psutil.disk_usage('/')
# print("Disco Uso: ",disco_uso)

# # Retorna o IO do Disco
# # Quando perdisk é True, retorna a mesma informação para cada disco fisico
# # Caso nowrap for True, retorna o valor acumulado desde a inicialização do sistema
# disco_io = psutil.disk_io_counters(perdisk=True, nowrap=True)
# print("Disco IO: ",disco_io)