import { useEffect, useState } from "react";
import { API_URL } from "./api";
import "./App.css";

const empleadoVacio = { nombre: "", apellido: "", cargo: "", salario: "" };

function App() {
  const [empleados, setEmpleados] = useState([]);
  const [formulario, setFormulario] = useState(empleadoVacio);
  const [editandoId, setEditandoId] = useState(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    cargarEmpleados();
  }, []);

  function cargarEmpleados() {
    setCargando(true);
    fetch(API_URL)
      .then((res) => {
        if (!res.ok) throw new Error("No se pudo conectar con la API");
        return res.json();
      })
      .then((datos) => {
        setEmpleados(datos);
        setError("");
      })
      .catch((err) => setError(err.message))
      .finally(() => setCargando(false));
  }

  function manejarCambio(evento) {
    const { name, value } = evento.target;
    setFormulario({ ...formulario, [name]: value });
  }

  function manejarEnvio(evento) {
    evento.preventDefault();

    const empleadoAEnviar = {
      ...formulario,
      salario: parseFloat(formulario.salario) || 0,
    };

    const esEdicion = editandoId !== null;
    const url = esEdicion ? `${API_URL}/${editandoId}` : API_URL;
    const metodo = esEdicion ? "PUT" : "POST";

    fetch(url, {
      method: metodo,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(empleadoAEnviar),
    })
      .then((res) => {
        if (!res.ok) throw new Error("No se pudo guardar el empleado");
        return res.json();
      })
      .then(() => {
        setFormulario(empleadoVacio);
        setEditandoId(null);
        cargarEmpleados();
      })
      .catch((err) => setError(err.message));
  }

  function manejarEditar(empleado) {
    setFormulario({
      nombre: empleado.nombre,
      apellido: empleado.apellido,
      cargo: empleado.cargo,
      salario: empleado.salario,
    });
    setEditandoId(empleado.id);
  }

  function manejarBorrar(id) {
    if (!confirm("¿Seguro que quieres borrar este empleado?")) return;

    fetch(`${API_URL}/${id}`, { method: "DELETE" })
      .then((res) => {
        if (!res.ok) throw new Error("No se pudo borrar el empleado");
        cargarEmpleados();
      })
      .catch((err) => setError(err.message));
  }

  function cancelarEdicion() {
    setFormulario(empleadoVacio);
    setEditandoId(null);
  }

  return (
    <div className="contenedor">
      <h1>Sistema de RRHH</h1>

      {error && <div className="error">⚠ {error}</div>}

      <form onSubmit={manejarEnvio} className="formulario">
        <h2>{editandoId ? "Editar empleado" : "Agregar empleado"}</h2>
        <input
          name="nombre"
          placeholder="Nombre"
          value={formulario.nombre}
          onChange={manejarCambio}
          required
        />
        <input
          name="apellido"
          placeholder="Apellido"
          value={formulario.apellido}
          onChange={manejarCambio}
          required
        />
        <input
          name="cargo"
          placeholder="Cargo"
          value={formulario.cargo}
          onChange={manejarCambio}
          required
        />
        <input
          name="salario"
          type="number"
          placeholder="Salario"
          value={formulario.salario}
          onChange={manejarCambio}
          required
        />
        <div className="botones-formulario">
          <button type="submit">{editandoId ? "Guardar cambios" : "Agregar"}</button>
          {editandoId && (
            <button type="button" onClick={cancelarEdicion} className="secundario">
              Cancelar
            </button>
          )}
        </div>
      </form>

      <h2>Empleados</h2>
      {cargando ? (
        <p>Cargando...</p>
      ) : empleados.length === 0 ? (
        <p>No hay empleados registrados todavía.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>Cargo</th>
              <th>Salario</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {empleados.map((emp) => (
              <tr key={emp.id}>
                <td>{emp.nombre}</td>
                <td>{emp.apellido}</td>
                <td>{emp.cargo}</td>
                <td>${emp.salario}</td>
                <td className="acciones">
                  <button onClick={() => manejarEditar(emp)}>Editar</button>
                  <button onClick={() => manejarBorrar(emp.id)} className="peligro">
                    Borrar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
