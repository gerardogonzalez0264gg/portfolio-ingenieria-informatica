# App RRHH - Versión 2.0

Esta versión corresponde a una evolución de la **App RRHH V1.0**, incorporando mejoras principalmente en seguridad, validaciones, gestión de salarios y organización del backend.

## 🔄 Cambios respecto a la V1.0

La V1.0 contaba principalmente con las funciones básicas de un sistema CRUD para gestionar empleados.

En la V2.0 se agregaron y mejoraron diferentes funcionalidades:

| V1.0 | V2.0 |
|---|---|
| CRUD básico de empleados | Se mantiene y mejora el CRUD de empleados |
| Validaciones básicas | Se incorporan nuevas validaciones de datos |
| Sin gestión de cambios salariales | Se incorpora cambio de salario |
| Sin historial de salarios | Se agrega historial de cambios salariales |
| Sin sistema de usuarios | Se incorpora sistema de usuarios |
| Sin autenticación | Se implementa funcionalidad de inicio de sesión |
| Sin protección de contraseñas | Se incorpora protección de contraseñas |
| Sin Spring Security | Se incorpora Spring Security |
| Manejo de errores básico | Se incorpora un manejador de errores |
| Estructura básica del backend | Se incorpora una capa de servicios |

## 🔐 Seguridad y autenticación

En comparación con la V1.0, la V2.0 incorpora funcionalidades de seguridad y autenticación mediante **Spring Security**.

Se agregaron:

- Sistema de usuarios.
- Funcionalidad de inicio de sesión.
- Protección de contraseñas.
- Configuración de Spring Security.

Estas funcionalidades están **implementadas en el backend**, pero actualmente el inicio de sesión **no está integrado al acceso inicial del frontend**. Es decir, la aplicación cuenta con el sistema de autenticación, pero este todavía no se utiliza para restringir la entrada a la aplicación.

## ✅ Validaciones

Se incorporaron validaciones para controlar los datos ingresados, entre ellas:

- Nombre y apellido obligatorios.
- Salario con valor positivo.
- Validación de los datos enviados a la API.

## 💰 Gestión de salarios

La V2.0 incorpora la posibilidad de modificar el salario de un empleado y registrar los cambios realizados mediante un **historial de salarios**.

## 🏗️ Organización del backend

El backend fue mejorado mediante la incorporación de una **capa de servicios**, separando mejor las responsabilidades de la aplicación:

```text
Controller
    ↓
Service
    ↓
Repository
    ↓
Database
