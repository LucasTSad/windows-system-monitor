import psutil
import socket

FAMILY_MAP = {
    socket.AF_INET: "IPv4",
    socket.AF_INET6: "IPv6",
    getattr(psutil, "AF_LINK", -1): "MAC"
}

if hasattr(socket, "AF_LINK"):
    FAMILY_MAP[socket.AF_LINK] = "MAC"

def formatar_tamanho_bytes(bytes_value):
    for unit in ('B', 'KB', 'MB', 'GB'):
        if bytes_value < 1024:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024
    return f"{bytes_value:.2f} TB"

def formatar_tamanho_taxa(bytes_per_sec):
    for unit in ('B/s', 'KB/s', 'MB/s', 'GB/s'):
        if bytes_per_sec < 1024:
            return f"{bytes_per_sec:.2f} {unit}"
        bytes_per_sec /= 1024
    return f"{bytes_per_sec:.2f} TB/s"

def get_net_info():
    net_io_per_nic = psutil.net_io_counters(pernic=True)
    net_io_detailed = {
        nic: {"bytes_enviados": io.bytes_sent, "bytes_recebido": io.bytes_recv}
        for nic, io in net_io_per_nic.items()
    }
    
    net_if_stats = psutil.net_if_stats()
    net_stats = {
        net: {
            "isup": net_if_stats[net].isup,
            "vel_mbps": net_if_stats[net].speed
        }
        for net in net_if_stats
    }
    
    net_if_addrs = psutil.net_if_addrs()
    net_addrs = {}
    for net in net_if_addrs:
        net_addrs[net] = []
        for addr in net_if_addrs[net]:
            friendly_map = FAMILY_MAP.get(addr.family, f"Outro ({addr.family})")
            net_addrs[net].append({
                "tipo": friendly_map,
                "endereco": addr.address
            })
    
    return {
        "net_io": net_io_detailed, 
        "status_net": net_stats,
        "endereco_net": net_addrs
    }


class MonitorRede:
    def __init__(self):
        net_io_start = psutil.net_io_counters(pernic=True)
        self.last_sample = {
            nic: {"bytes_enviados": io.bytes_sent, "bytes_recebido": io.bytes_recv}
            for nic, io in net_io_start.items()
        }

    def medir_vel_atual(self, intervalo=1):
        current_data = get_net_info()
        current_sample = current_data["net_io"]
        status_map = current_data["status_net"]
        addrs_map = current_data["endereco_net"]

        interfaces_info = {}

        for nic, dados in current_sample.items():
            # Verifica se a interface está ativa/conectada
            is_up = status_map.get(nic, {}).get("isup", False)

            if not is_up:
                # Caso esteja desconectada, insere apenas o status
                interfaces_info[nic] = {
                    "status": "Desconectado"
                }
            else:
                # Caso esteja conectada, calcula e inclui todos os dados
                bytes_sent_total = dados["bytes_enviados"]
                bytes_recv_total = dados["bytes_recebido"]

                if nic in self.last_sample:
                    diff_recv = (bytes_recv_total - self.last_sample[nic]["bytes_recebido"]) / intervalo
                    diff_sent = (bytes_sent_total - self.last_sample[nic]["bytes_enviados"]) / intervalo
                else:
                    diff_recv = 0
                    diff_sent = 0

                enderecos = addrs_map.get(nic, [])

                interfaces_info[nic] = {
                    "status": "Conectado",
                    "velocidade_download": formatar_tamanho_taxa(diff_recv),
                    "velocidade_upload": formatar_tamanho_taxa(diff_sent),
                    "bytes_recebidos_total": formatar_tamanho_bytes(bytes_recv_total),
                    "bytes_enviados_total": formatar_tamanho_bytes(bytes_sent_total),
                    "enderecos": enderecos
                }

        self.last_sample = current_sample
        return interfaces_info