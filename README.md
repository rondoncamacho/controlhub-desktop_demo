# ControlHUB - Demo

Panel de administración y gestión remota de equipos informáticos desarrollado en Python (CustomTkinter) para entornos críticos. **Herramienta interna utilizada en operaciones de emergencia.**

---

![Vista del Dashboard](https://github.com/rondoncamacho/controlhub-desktop_demo/blob/main/screenshots/Dashboard.png)

## 🚀 Funcionalidades

- Monitoreo de estado de equipos en tiempo real.
- Ejecución remota de comandos (CMD).
- Gestión de archivos vía SMB.
- Acceso remoto (VNC).
- Gestión de MySQL y backups.

---

## 🛠️ Tecnologías

- Python 3.10+
- CustomTkinter (UI moderna)
- WMI (Administración remota Windows)
- ThreadPoolExecutor (Monitoreo paralelo)
- MySQL (Gestión de bases de datos)
- PsExec / VNC (Control remoto)
- SMB (Transferencia de archivos)

---

## 💡 Retos Técnicos Superados

- **Monitoreo en tiempo real:** Implementación de ThreadPoolExecutor para escanear +50 equipos en paralelo.
- **Seguridad:** Manejo de credenciales vía variables de entorno y keyring.
- **Interfaz crítica:** Diseño UX enfocado en tiempos de respuesta rápidos para operadores.

---

## 📸 Panel de Control de Equipos

![Control de Equipos](https://github.com/rondoncamacho/controlhub-desktop_demo/blob/main/screenshots/Controldeequipos.png)

---

## 🔒 Nota de Seguridad

Este repositorio es una **demo pública**. No contiene:
- IPs reales
- Nombres de equipos reales
- Credenciales
- Datos operativos del 911

El código completo y la información de infraestructura son confidenciales y no están disponibles públicamente.

---

## 📬 Contacto

**Ing. Luis Rondón**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rondoncamacho/)
