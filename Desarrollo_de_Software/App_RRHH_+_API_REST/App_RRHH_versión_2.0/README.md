# App RRHH - Versión 2.0

Aplicación web para la gestión de empleados desarrollada como proyecto de estudio.

Esta versión corresponde a una mejora de la **App RRHH V1.0**, incorporando nuevas funcionalidades relacionadas con seguridad, validaciones, gestión de salarios y organización del backend.

## 🚀 Funcionalidades

- Crear empleados.
- Consultar empleados.
- Actualizar información de empleados.
- Eliminar empleados.
- Validación de datos de los empleados.
- Validación del salario.
- Cambio de salario.
- Registro del historial de cambios de salario.
- Sistema de usuarios y autenticación.
- Protección de contraseñas.
- Manejo de errores.
- Separación de responsabilidades mediante una capa de servicios.

> La autenticación se encuentra implementada en el backend, pero actualmente no está integrada como requisito para acceder a la aplicación desde el frontend.

## 🛠️ Tecnologías utilizadas

### Backend
- Java
- Spring Boot
- Spring Data JPA
- Spring Security
- Maven
- Base de datos

### Frontend
- React
- Vite
- JavaScript
- CSS
- HTML

## 📁 Estructura del proyecto

```text
App_RRHH_versión_2.0/
│
├── rrhh-api/
│   └── Backend desarrollado con Spring Boot
│
└── rrhh-frontend/
    └── Frontend desarrollado con React + Vite
