# 🚗 Sistema de Estacionamiento v1.0

Sistema integral de gestión de estacionamientos diseñado para optimizar el control de ingresos, asignación de espacios y procesos de facturación automática.

## 📋 Tabla de Contenidos
- [Objetivo](#-objetivo)
- [Características Principales](#-características-principales)
- [Flujo de Funcionamiento](#-flujo-de-funcionamiento)
- [Guía de Instalación](#-guía-de-instalación)
- [Estructura del Código](#-estructura-del-código)

---

## 🎯 Objetivo
Desarrollar una herramienta eficiente que permita a los administradores de playas de estacionamiento:
1.  **Digitalizar** el registro de vehículos.
2.  **Optimizar** el uso del espacio físico mediante un mapa en tiempo real.
3.  **Automatizar** el cálculo de tarifas para evitar errores humanos en el cobro.

---

## ✨ Características Principales

### ⚙️ Gestión de Tarifas
- Configuración por tipo de vehículo: **Auto**, **Moto**, **Camioneta**.
- Cálculo basado en horas (con redondeo comercial).
- Flexibilidad para definir precios base por categoría.

### 📥 Control de Ingreso (Check-in)
- Registro de patente y tipo de vehículo.
- **Asignación Inteligente:** El sistema busca automáticamente la primera cochera disponible.
- Marca de tiempo precisa mediante el servidor.

### 🗺️ Visualización de Disponibilidad
- Panel visual del estado de las cocheras (**Libre** vs **Ocupado**).
- Identificación inmediata de qué vehículo ocupa cada lugar.

### 💳 Salida y Cobro (Check-out)
- Cálculo automático de estadía.
- Generación de resumen de cobro (Ticket de salida).
- Liberación automática del espacio tras el pago.
