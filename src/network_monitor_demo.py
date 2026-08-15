"""
ControlHUB - Network Monitor (Demo)
Monitoreo paralelo de múltiples hosts usando ThreadPoolExecutor.
"""

import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ping_host(ip, timeout=0.3):
    """Verifica estado de un host via ping (Windows)."""
    cmd = ['ping', '-n', '1', '-w', '300', ip]
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout
        )
        return ip, result.returncode == 0
    except subprocess.TimeoutExpired:
        logger.warning(f"Timeout en {ip}")
        return ip, False
    except Exception as e:
        logger.error(f"Error en {ip}: {e}")
        return ip, False


def monitor_network_demo(ip_list):
    """Escanea múltiples IPs en paralelo usando ThreadPoolExecutor."""
    results = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(ping_host, ip): ip for ip in ip_list}
        for future in as_completed(futures):
            ip, status = future.result()
            results[ip] = "✅ ACTIVO" if status else "❌ INACTIVO"
            logger.info(f"{ip}: {'ACTIVO' if status else 'INACTIVO'}")
    return results


if __name__ == "__main__":
    # IPs de ejemplo (reservadas para documentación)
    ips = ["192.0.2.1", "192.0.2.2", "192.0.2.3", "8.8.8.8"]
    
    print("🔍 Escaneando hosts...")
    for ip, status in monitor_network_demo(ips).items():
        print(f"{ip}: {status}")
