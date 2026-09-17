package com.rrhh.api.empleado;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.NoSuchElementException;

@Service
public class EmpleadoService {

    @Autowired
    private EmpleadoRepository empleadoRepository;

    @Autowired
    private HistorialSalarioRepository historialRepository;

    @Transactional
    public Empleado cambiarSalario(Long empleadoId, Double nuevoSalario, String motivo) {

        Empleado empleado = empleadoRepository.findById(empleadoId)
                .orElseThrow(() -> new NoSuchElementException("Empleado no encontrado"));

        Double salarioAnterior = empleado.getSalario();

        if (nuevoSalario == null || nuevoSalario <= 0) {
            throw new IllegalArgumentException("El nuevo salario debe ser un número positivo");
        }

        empleado.setSalario(nuevoSalario);
        empleadoRepository.save(empleado);

        HistorialSalario registro = new HistorialSalario(empleado, salarioAnterior, nuevoSalario, motivo);
        historialRepository.save(registro);

        return empleado;
    }

    public List<HistorialSalario> obtenerHistorial(Long empleadoId) {
        return historialRepository.findByEmpleadoIdOrderByFechaDesc(empleadoId);
    }
}
