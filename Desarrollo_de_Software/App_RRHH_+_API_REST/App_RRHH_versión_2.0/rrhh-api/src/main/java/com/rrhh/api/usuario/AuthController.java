package com.rrhh.api.usuario;

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = "*")
public class AuthController {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @PostMapping("/registro")
    public ResponseEntity<?> registrar(@Valid @RequestBody Usuario datos) {

        if (usuarioRepository.findByUsername(datos.getUsername()).isPresent()) {
            return ResponseEntity.status(HttpStatus.CONFLICT)
                    .body(Map.of("error", "Ese nombre de usuario ya existe"));
        }

        String hashDeLaClave = passwordEncoder.encode(datos.getPassword());
        datos.setPassword(hashDeLaClave);

        Usuario guardado = usuarioRepository.save(datos);

        guardado.setPassword(null);
        return ResponseEntity.status(HttpStatus.CREATED).body(guardado);
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@Valid @RequestBody LoginRequest login) {

        Optional<Usuario> posibleUsuario = usuarioRepository.findByUsername(login.getUsername());

        if (posibleUsuario.isEmpty()) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Usuario o contraseña incorrectos"));
        }

        Usuario usuario = posibleUsuario.get();

        boolean claveCorrecta = passwordEncoder.matches(login.getPassword(), usuario.getPassword());

        if (!claveCorrecta) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Usuario o contraseña incorrectos"));
        }

        usuario.setPassword(null);
        return ResponseEntity.ok(usuario);
    }
}
