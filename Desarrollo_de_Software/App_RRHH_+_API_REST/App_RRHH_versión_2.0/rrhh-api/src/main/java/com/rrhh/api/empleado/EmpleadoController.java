package com.rrhh.api.empleado;

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;

@RestController
@RequestMapping("/api/empleados")
@CrossOrigin(origins = "*")
public class EmpleadoController {

    @Autowired
    private EmpleadoRepository empleadoRepository;

    @Autowired
    private EmpleadoService empleadoService;

    @GetMapping
    public List<Empleado> listarTodos() {
        return empleadoRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Empleado> obtenerPorId(@PathVariable Long id) {
        return empleadoRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Empleado> crear(@Valid @RequestBody Empleado nuevoEmpleado) {
        Empleado guardado = empleadoRepository.save(nuevoEmpleado);
        return ResponseEntity.status(HttpStatus.CREATED).body(guardado);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Empleado> actualizar(@PathVariable Long id, @Valid @RequestBody Empleado datos) {
        return empleadoRepository.findById(id)
                .map(empleadoExistente -> {
                    empleadoExistente.setNombre(datos.getNombre());
                    empleadoExistente.setApellido(datos.getApellido());
                    empleadoExistente.setCargo(datos.getCargo());
                    empleadoExistente.setSalario(datos.getSalario());
                    Empleado actualizado = empleadoRepository.save(empleadoExistente);
                    return ResponseEntity.ok(actualizado);
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminar(@PathVariable Long id) {
        if (!empleadoRepository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        empleadoRepository.deleteById(id);
        return ResponseEntity.noContent().build();
    }

    @PatchMapping("/{id}/salario")
    public ResponseEntity<?> cambiarSalario(@PathVariable Long id,
                                             @Valid @RequestBody CambioSalarioRequest datos) {
        try {
            Empleado actualizado = empleadoService.cambiarSalario(
                    id, datos.getNuevoSalario(), datos.getMotivo());
            return ResponseEntity.ok(actualizado);
        } catch (NoSuchElementException e) {
            return ResponseEntity.notFound().build();
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/historial-salarios")
    public List<HistorialSalario> verHistorialSalarios(@PathVariable Long id) {
        return empleadoService.obtenerHistorial(id);
    }
}
