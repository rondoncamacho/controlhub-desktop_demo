"""
ControlHUB - UI Design System (Demo)
Sistema de diseño con CustomTkinter (tema oscuro, colores, fuentes).
"""

import customtkinter as ctk


class DesignSystem:
    """Sistema de diseño centralizado para la aplicación."""
    
    @staticmethod
    def get_colors():
        """Retorna la paleta de colores completa."""
        return {
            "bg_primary": "#0a0a0f",
            "bg_secondary": "#14141e", 
            "bg_card": "#1e3a5f",
            "primary": "#0ea5e9",
            "success": "#10b981",
            "error": "#ef4444",
            "text_primary": "#ffffff",
            "text_secondary": "#cbd5e1",
            "button_colors": {
                "cmd": "#857f75",
                "reiniciar": "#dc2626",
                "notas": "#059669",
                "remoto": "#7c3aed"
            }
        }
    
    @staticmethod
    def get_fonts():
        """Retorna la configuración de fuentes."""
        SANS = ("Segoe UI", "Arial", "sans-serif")
        return {
            "TITLE": (SANS, 22, "bold"),
            "BUTTON": (SANS, 14, "bold"),
            "SMALL": (SANS, 10)
        }


if __name__ == "__main__":
    # Aplicar tema
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    colors = DesignSystem.get_colors()
    
    # Ventana de prueba
    root = ctk.CTk()
    root.title("SFX-ControlHUB Demo - UI")
    root.geometry("400x250")
    root.configure(fg_color=colors["bg_primary"])
    
    # Frame principal
    card = ctk.CTkFrame(root, fg_color=colors["bg_card"], corner_radius=10)
    card.pack(expand=True, padx=20, pady=20, fill="both")
    
    # Título
    ctk.CTkLabel(
        card,
        text="SFX-ControlHUB",
        font=DesignSystem.get_fonts()["TITLE"],
        text_color=colors["text_primary"]
    ).pack(pady=20)
    
    # Botones de ejemplo
    ctk.CTkButton(
        card,
        text="REINICIAR",
        font=DesignSystem.get_fonts()["BUTTON"],
        fg_color=colors["button_colors"]["reiniciar"],
        corner_radius=8,
        width=120
    ).pack(pady=5)
    
    ctk.CTkButton(
        card,
        text="+INFO",
        font=DesignSystem.get_fonts()["BUTTON"],
        fg_color=colors["primary"],
        corner_radius=8,
        width=120
    ).pack(pady=5)
    
    # Estado
    ctk.CTkLabel(
        card,
        text="🟢 ONLINE",
        font=DesignSystem.get_fonts()["SMALL"],
        text_color=colors["success"]
    ).pack(pady=10)
    
    root.mainloop()
