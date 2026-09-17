package com.rrhh.api.empleado;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
public class HistorialSalario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "empleado_id", nullable = false)
    private Empleado empleado;

    private Double salarioAnterior;
    private Double salarioNuevo;
    private String motivo;
    private LocalDateTime fecha;

    public HistorialSalario() {
    }

    public HistorialSalario(Empleado empleado, Double salarioAnterior, Double salarioNuevo, String motivo) {
        this.empleado = empleado;
        this.salarioAnterior = salarioAnterior;
        this.salarioNuevo = salarioNuevo;
        this.motivo = motivo;
        this.fecha = LocalDateTime.now();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Empleado getEmpleado() {
        return empleado;
    }

    public void setEmpleado(Empleado empleado) {
        this.empleado = empleado;
    }

    public Double getSalarioAnterior() {
        return salarioAnterior;
    }

    public void setSalarioAnterior(Double salarioAnterior) {
        this.salarioAnterior = salarioAnterior;
    }

    public Double getSalarioNuevo() {
        return salarioNuevo;
    }

    public void setSalarioNuevo(Double salarioNuevo) {
        this.salarioNuevo = salarioNuevo;
    }

    public String getMotivo() {
        return motivo;
    }

    public void setMotivo(String motivo) {
        this.motivo = motivo;
    }

    public LocalDateTime getFecha() {
        return fecha;
    }

    public void setFecha(LocalDateTime fecha) {
        this.fecha = fecha;
    }
}
