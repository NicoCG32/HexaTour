# Changelog

Todas las entradas notables de este proyecto se documentan en este archivo.

El formato esta basado en [Keep a Changelog](https://keepachangelog.com/es/),
y el proyecto sigue [Versionado Semantico](https://semver.org/lang/es/).

## [1.0.0] - 2026-07-18

Entrega de curso y cierre del repositorio como producto final.

### Agregado
- `README.md` reescrito como guia de ejecucion reproducible (web sin
  hardware, carga de firmware y pruebas), con nota de estado del proyecto.
- `test/validate_data.py`: validador de coherencia de los datos del portal
  (campos obligatorios de cada POI y conteos por categoria), sin dependencias
  externas.
- `LICENSE` (MIT).
- `.gitignore` con reglas para Python, Node, Arduino/ESP32, IDEs y secretos.

### Eliminado
- Archivos de gobernanza de comunidad OSS (`CODE_OF_CONDUCT.md`,
  `CONTRIBUTING.md`, `SECURITY.md` y `.github/`), propios de proyectos con
  desarrollo y contribuidores externos activos; no aplican a un proyecto
  academico cerrado.
