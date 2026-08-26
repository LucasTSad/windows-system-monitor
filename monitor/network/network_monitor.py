import psutil
import time
import socket

# Filtro de familia de endereços
FAMILY_MAP = {
    socket.AF_INET : "inet",
    socket.AF_INET6 : "inet6",
    getattr(psutil, "AF_LINK", -1): "MAC"
}

if hasattr(socket, "AF_LINK"):
    FAMILY_MAP[socket.AF_LINK] = "MAC"

def get_net_info():
    # Coleta I/O bruto
    net_io_per_nic = psutil.net_io_counters(pernic=True)
    net_io_detailed = {nic: {"bytes_enviados": io.bytes_sent, "bytes_recebido": io.bytes_recv} for nic, io in net_io_per_nic.items()}
    
    # Coleta Status (isup)
    net_if_stats = psutil.net_if_stats()
    net_stats = {net: {"isup": net_if_stats[net].isup, "vel_mbps": net_if_stats[net].speed} for net in net_if_stats}
    
    # Coleta Endereços com nomes amigáveis (Sua lógica original preservada e traduzida)
    net_if_addrs = psutil.net_if_addrs()
    net_addrs = {}
    for net in net_if_addrs:
        net_addrs[net] = []
        for addr in net_if_addrs[net]:
            friendly_map = FAMILY_MAP.get(addr.family, f"Desconhecido ({addr.family})")
            net_addrs[net].append({
                "familia": friendly_map,
                "endereco": addr.address
            })
    
    return {
        "net_io": net_io_detailed, 
        "status_net": net_stats,
        "endereco_net": net_addrs
    }

def formatar_tamanho(bytes_per_sec):
    for unit in ('B/s', 'KB/s', 'MB/s', 'GB/s'):
        if bytes_per_sec < 1024:
            return f"{bytes_per_sec:.2f} {unit}"
        bytes_per_sec /= 1024
    return f"{bytes_per_sec:.2f} TB/s"

class MonitorRede:
    def __init__(self):

        net_io_start = psutil.net_io_counters(pernic=True)
        self.last_sample = {
            nic: {"bytes_enviados": io.bytes_sent, "bytes_recebido": io.bytes_recv}
            for nic, io in net_io_start.items()
        }

    def medir_vel_atual(self, intervalo = 1 ):

        current_data = get_net_info()
        current_sample = current_data["net_io"]
        active_nic = {nic for nic, status in current_data["status_net"].items() if status["isup"]}

        fluxo_real = {}
        for nic, dados in current_sample.items():
            if nic in self.last_sample and nic in active_nic:

                diff_recv = (dados["bytes_recebido"] - self.last_sample[nic]["bytes_recebido"]) / intervalo
                diff_sent = (dados["bytes_enviados"] - self.last_sample[nic]["bytes_enviados"]) / intervalo
                addrs =  current_data["endereco_net"].get(nic, [])

                fluxo_real[nic] = {
                    "download_vel": formatar_tamanho(diff_recv),
                    "upload_vel": formatar_tamanho(diff_sent),
                    "endereco": addrs
                }

        self.last_sample = current_sample
        return fluxo_real    


# # NETWORK ---------------------------------------------------------------------------------
# # Retorna as statisticas de I/O da rede
# # Caso pernic for True retorna todas as redes instaladas
# # Caso False retorna apenas a ativa
# rede = psutil.net_io_counters(pernic=False, nowrap=True)
# print("Rede: ",rede)

# # Retorna os tipos de IP usado
# # inet - IPv4 e IPv6
# # inet4 - IPv4
# # inet6 - IPv6
# # tcp - TCP
# # tcp4 - prioriza TCP ao invez de IPv4
# # tcp6 - prioriza TCP ao invez de IPv6
# # udp - UDP
# # udp4 - prioriza UDP ao invez de IPv4
# # udp6 - prioriza UDP ao invez de IPv6
# # unix - Unix sockets
# # all - todos os tipos de IP
# # rede_ip = psutil.net_connections(kind='inet4')
# # print("Rede IP: ",rede_ip)

# # Retorna o endereço associado a cada NIC
# # rede_endereco = psutil.net_if_addrs()
# # print("Rede Endereço: ",rede_endereco)

# # Retorna as estatisticas de cada NIC
# rede_estatisticas = psutil.net_if_stats()
# print("Rede Estatisticas: ",rede_estatisticas)
