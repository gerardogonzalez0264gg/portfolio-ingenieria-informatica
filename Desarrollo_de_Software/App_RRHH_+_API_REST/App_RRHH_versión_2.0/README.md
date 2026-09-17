# App RRHH - Versión 2.0

Esta versión corresponde a una evolución de la **App RRHH V1.0**, incorporando mejoras principalmente en seguridad, validaciones, gestión de salarios y organización del backend.

## 🔄 Cambios respecto a la V1.0

La **V1.0** contaba principalmente con las funciones básicas de un sistema CRUD para gestionar empleados.

En la **V2.0** se agregaron y mejoraron diferentes funcionalidades:

| V1.0 | V2.0 |
|---|---|
| CRUD básico de empleados | Se mantiene el CRUD de empleados |
| Sin validaciones completas | Se agregan validaciones de datos |
| Sin gestión de cambios salariales | Se incorpora cambio de salario |
| Sin historial de salarios | Se agrega historial de cambios salariales |
| Sin sistema de usuarios | Se incorporan usuarios y autenticación |
| Sin protección de contraseñas | Se agrega protección de contraseñas |
| Manejo de errores básico | Se incorpora un manejador de errores |
| Backend con estructura básica | Se agrega una capa de servicios |
| Sin Spring Security | Se incorpora Spring Security |

## 🔐 Seguridad

La V2.0 incorpora herramientas de seguridad mediante **Spring Security**, además de funcionalidades relacionadas con usuarios, inicio de sesión y protección de contraseñas.

La autenticación está implementada en el backend, pero actualmente **no se utiliza para restringir el acceso inicial al frontend**.

## ✅ Validaciones

Se agregaron validaciones para controlar los datos ingresados, como:

- Nombre y apellido obligatorios.
- Salario con valor positivo.
- Validación de los datos enviados a la API.

## 💰 Gestión de salarios

La V2.0 incorpora la posibilidad de modificar el salario de un empleado y registrar los cambios realizados mediante un **historial de salarios**.

## 🏗️ Organización del backend

El backend fue mejorado mediante la incorporación de una **capa de servicios**, separando mejor las responsabilidades:

```text
Controller
    ↓
Service
    ↓
Repository
    ↓
Database
