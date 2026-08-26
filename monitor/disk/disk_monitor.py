import psutil

from monitor.bytes_2_gb import bytes_converter

class MonitorDisco:

    def __init__(self):
        # Retorna todos os discos
        all_disks = psutil.disk_partitions(all=True)
        # Lista de todos os discos
        self.all_disk_sum = self._disk_info_builder(all_disks)
        # Retorna os disicos ustilizaveis
        self.usable_disks = [disk for disk in all_disks if 'cdrom' not in disk.opts and disk.fstype != '']
        # Lista de todos os discos fisicos validas/ativas
        self.usable_disks_sum = self._disk_info_builder(self.usable_disks)

        self.total_gb_cache = {}
        for disk in self.usable_disks:
            try:
                # No Windows/Linux, usar o mountpoint para buscar o uso é o padrão mais seguro
                usage = psutil.disk_usage(disk.mountpoint)
                self.total_gb_cache[disk.device] = bytes_converter(usage.total)
            except OSError:
                self.total_gb_cache[disk.device] = None

    def _disk_info_builder(self,disks):
        disk_lib = {}
        for disk in disks:
                disk_lib[disk.device] = {
                    "ponto_montagem": disk.mountpoint,
                    "sistema_arquivos": disk.fstype if disk.fstype != '' else "N/A",
                    "opcoes": disk.opts
                }

        return disk_lib

    def get_disk_info(self):
       
        sum_uso = {}

        for disk in self.usable_disks:
            try:
                # disk.device contém a letra no Windows (ex: 'C:\\') ou o caminho no Linux (ex: '/')
                usage = psutil.disk_usage(disk.device)

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
                # Evita que o script quebre caso algum disco precise de permissão de administrador
                sum_uso[disk.device] = {
                    "total_gb": self.total_gb_cache.get(disk.device),
                    "used_gb": None,
                    "free_gb": None,
                    "percentual": None,
                    "status": status_erro
                }

        return {
            "discos" : {
                "todos_discos" : self.all_disk_sum,
                "discos_usáveis" : self.usable_disks_sum,
            },
            "uso_disco" : sum_uso
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