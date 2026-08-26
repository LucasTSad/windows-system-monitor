import psutil
import json
import subprocess
import time

from monitor.cpu.cpu_monitor import MonitorCPU
from monitor.memory.memory_monitor import MonitorMemoria
from monitor.disk.disk_monitor import MonitorDisco
from monitor.network.network_monitor import MonitorRede

def start_monitor():
    monitor_rede = MonitorRede()
    monitor_cpu = MonitorCPU()
    monitor_mem = MonitorMemoria()
    monitor_disk = MonitorDisco()

    comando_limpar = ["cls"] if subprocess.os.name == 'nt' else ["clear"]
    intervalo_seg = 1

    try:
        while True:
            # Coleta os dados brutos das suas classes
            dados_cpu = monitor_cpu.get_cpu_info()         
            dados_mem = monitor_mem.get_memory_info()       
            dados_disk = monitor_disk.get_disk_info()       
            dados_rede = monitor_rede.medir_vel_atual(intervalo=intervalo_seg)

            # Trata as frequências para o JSON não quebrar se vier None
            freq_atual = dados_cpu['frequencia_cpu_mhz']['atual']
            freq_formatada = f"{int(freq_atual)} MHz" if freq_atual else "N/A"

            # Monta o JSON final exatamente com o layout e chaves que você pediu
            snapshot_enxuto = {
                "TIMESTAMP": time.strftime("%d/%m/%Y %H:%M:%S"),
                "CPU": {
                    "Uso": f"{dados_cpu['uso_total_percentual']}%",
                    "Frequência": freq_formatada,
                    "Frequência Mínima": f"{int(dados_cpu['frequencia_cpu_mhz']['min'])} MHz",
                    "Frequência Máxima": f"{int(dados_cpu['frequencia_cpu_mhz']['max'])} MHz"
                },
                "MEMÓRIA": {
                    "Uso_RAM": f"{dados_mem['memoria']['percentual_ram_uso']}%",
                    "Consumo_RAM": f"{dados_mem['memoria']['usada_ram']} / {dados_mem['memoria']['total_ram']}",
                    "Uso_Swap": f"{dados_mem['swap'].get('percentual_swap_uso', 0)}%",
                    "Consumo_Swap": f"{dados_mem['swap']['usada_swap']} / {dados_mem['swap']['total_swap']}"
                },
                "DISCO": {
                    # Varre dinamicamente todos os discos usáveis mapeados
                    dispositivo: f"Uso: {dados['percentual']}%"
                    for dispositivo, dados in dados_disk['uso_disco'].items()
                },
                "REDE": {
                    # Varre dinamicamente as placas de rede ativas com tráfego
                    nome_placa: {
                        "Download": velocidades['download_vel'],
                        "Upload": velocidades['upload_vel']
                    }
                    for nome_placa, velocidades in dados_rede.items()
                } if dados_rede else "Nenhuma interface ativa com tráfego."
            }

            # Limpa o terminal antes de exibir o novo segundo
            subprocess.run(comando_limpar, shell=True)

            print(json.dumps(snapshot_enxuto, indent=4, ensure_ascii=False))

            time.sleep(intervalo_seg)

    except KeyboardInterrupt:
        print("\n[!] Monitoramento encerrado pelo usuário.")

if __name__ == "__main__":
    start_monitor()

# SENSORES ---------------------------------------------------------------------------------
# Retorna o status da bateria do sensor
sensor = psutil.sensors_battery()
print("Sensor: ",sensor)

# BOOT TIME ---------------------------------------------------------------------------------
# Retorna o tempo de boot do sistema
boot_time = psutil.boot_time()
print("Boot Time: ",boot_time)

# USERS ---------------------------------------------------------------------------------
# Retorna os usuários logados no sistema
usuarios = psutil.users()
print("Usuários: ",usuarios)

# PROCESSOS ---------------------------------------------------------------------------------
# Retorna os processos ativos no sistema
# for proc in psutil.process_iter(['pid', 'name', 'username']):
#     print(proc.info)

# Retorna quais PIDs existem no sistema
# pids = psutil.pid_exists(7464) # troque o PID para o que deseja verificar
# print("PID x existe: ",pids)

# Retorna qual processo pode ser terminado
procs = psutil.Process().children()
gone, alive = psutil.wait_procs(procs, timeout=3)
print(gone)
print(alive)