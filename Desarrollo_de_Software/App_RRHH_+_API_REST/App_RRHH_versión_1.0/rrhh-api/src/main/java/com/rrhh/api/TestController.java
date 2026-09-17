package com.rrhh.api;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class TestController {

    @GetMapping("/api/test")
    public String probarConexion() {
        return "La API está funcionando correctamente";
    }

}
