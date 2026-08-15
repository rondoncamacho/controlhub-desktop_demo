"""
ControlHUB - WMI Connector (Demo)
Parte de una herramienta interna utilizada en operaciones de emergencia.
Este fragmento muestra la conexión WMI remota para obtener uptime.
"""

import os
import logging
import pythoncom
import win32com.client
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def wmi_connect_demo(ip, username, password):
    """Establece conexión WMI con un equipo remoto."""
    pythoncom.CoInitialize()
    try:
        locator = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        return locator.ConnectServer(ip, "root\\cimv2", username, password)
    except Exception as e:
        pythoncom.CoUninitialize()
        logger.error(f"Error WMI en {ip}: {e}")
        raise


def get_uptime_demo(ip, username, password):
    """Obtiene el uptime de un equipo remoto vía WMI."""
    try:
        svc = wmi_connect_demo(ip, username, password)
        os_q = svc.ExecQuery("SELECT LastBootUpTime FROM Win32_OperatingSystem")
        for os_obj in os_q:
            raw = str(os_obj.LastBootUpTime).split(".")[0]
            boot = datetime.strptime(raw, "%Y%m%d%H%M%S")
            delta = datetime.now() - boot
            return f"Uptime: {delta.days}d {delta.seconds // 3600}h"
    except Exception as e:
        logger.error(f"Error obteniendo uptime de {ip}: {e}")
        return f"Uptime: Error ({e})"
    finally:
        pythoncom.CoUninitialize()


if __name__ == "__main__":
    # Variables de entorno para credenciales (usa 192.0.2.10 como IP de ejemplo)
    host = os.getenv("WMI_HOST", "192.0.2.10")
    user = os.getenv("WMI_USER", "demo_user")
    pwd = os.getenv("WMI_PASSWORD", "demo_password")
    
    print(f"🔍 Conectando a {host}...")
    result = get_uptime_demo(host, user, pwd)
    print(result)
