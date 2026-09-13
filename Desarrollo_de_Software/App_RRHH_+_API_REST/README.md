# Aplicación de Gestión de Recursos Humanos

Aplicación web desarrollada para la gestión de empleados mediante una arquitectura separada entre frontend y backend.

## Descripción

La aplicación permite gestionar información de empleados a través de una interfaz web conectada a una API REST.

El proyecto está dividido en dos componentes principales:

- `rrhh-frontend`: interfaz web desarrollada con React.
- `rrhh-api`: API REST desarrollada con Spring Boot para gestionar los datos de los empleados.

## Tecnologías utilizadas

### Frontend

- React
- JavaScript
- Vite
- HTML
- CSS

### Backend

- Java
- Spring Boot
- Spring Data JPA
- Maven
- H2 Database

## Funcionalidades

- Registrar empleados.
- Consultar empleados.
- Actualizar información de empleados.
- Eliminar empleados.
- Comunicación entre frontend y backend mediante una API REST.

## Estructura del proyecto

```text
App_RRHH_+_API_REST/
├── rrhh-api/
│   ├── pom.xml
│   └── src/
│
└── rrhh-frontend/
    ├── package.json
    ├── public/
    └── src/
