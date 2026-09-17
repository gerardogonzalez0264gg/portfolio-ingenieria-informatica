package com.rrhh.api.empleado;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface HistorialSalarioRepository extends JpaRepository<HistorialSalario, Long> {

    List<HistorialSalario> findByEmpleadoIdOrderByFechaDesc(Long empleadoId);
}
