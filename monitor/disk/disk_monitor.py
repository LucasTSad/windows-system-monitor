import psutil

from monitor.bytes_2_gb import bytes_converter

def disk_info_builder(disks):
    disk_lib = {}
    for disk in disks:
            disk_lib[disk.device] = {
                "ponto_montagem": disk.mountpoint,
                "sistema_arquivos": disk.fstype if disk.fstype != '' else "N/A",
                "opcoes": disk.opts
            }

    return disk_lib

def get_disk_info():
    # Retorna todos os discos
    all_disks = psutil.disk_partitions(all=True)
    # Lista de todos os discos
    all_disk_resumo = disk_info_builder( all_disks)
    # Retorna os disicos fisicos
    usable_disks = [disk for disk in all_disks if 'cdrom' not in disk.opts and disk.fstype != '']
    # Lista de todos os discos fisicos validas/ativas
    usable_disks_resumo = disk_info_builder(usable_disks)

    # Retorna o uso do disco para cada disco fisico
    resumo_uso = {}
    for disk in usable_disks:
        try:
            # disk.device contém a letra no Windows (ex: 'C:\\') ou o caminho no Linux (ex: '/')
            usage = psutil.disk_usage(disk.device)
            
            resumo_uso[disk.device] = {
                "total_gb": bytes_converter(usage.total),
                "used_gb": bytes_converter(usage.used),
                "free_gb": bytes_converter(usage.free),
                "percentual": usage.percent,
                "status": "Online"
            }
        except OSError as e:
            # Define o status dinamicamente checando a classe da exceção 'e'
            status_erro = "Erro de Permissao" if isinstance(e, PermissionError) else "Unidade Indisponivel"
            # Evita que o script quebre caso algum disco precise de permissão de administrador
            resumo_uso[disk.device] = {
                "total_gb": None,
                "used_gb": None,
                "free_gb": None,
                "percentual": None,
                "status": status_erro
            }

    return {
        "discos" : {
            "todos_discos" : all_disk_resumo,
            "discos_usáveis" : usable_disks_resumo,
        },
        "uso_disco" : resumo_uso
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