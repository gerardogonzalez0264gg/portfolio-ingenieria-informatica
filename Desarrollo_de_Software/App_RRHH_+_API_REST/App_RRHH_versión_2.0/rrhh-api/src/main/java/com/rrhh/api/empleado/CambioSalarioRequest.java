package com.rrhh.api.empleado;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Positive;

public class CambioSalarioRequest {

    @Positive(message = "El nuevo salario debe ser positivo")
    private Double nuevoSalario;

    @NotBlank(message = "Debes indicar el motivo del cambio")
    private String motivo;

    public Double getNuevoSalario() {
        return nuevoSalario;
    }

    public void setNuevoSalario(Double nuevoSalario) {
        this.nuevoSalario = nuevoSalario;
    }

    public String getMotivo() {
        return motivo;
    }

    public void setMotivo(String motivo) {
        this.motivo = motivo;
    }
}
