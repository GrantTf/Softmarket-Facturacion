# Guía de contribución

## 1. Flujo de trabajo
1. Toma un issue del tablero (ej. `SM-12`).
2. `git switch develop && git pull`
3. `git switch -c feature/SM-12-calculo-impuestos`
4. Commits pequeños con Conventional Commits.
5. `git pull --rebase origin develop` antes de abrir el PR.
6. Abre el Pull Request hacia `develop` usando la plantilla.
7. Mínimo **1 aprobación** y **CI en verde** para hacer merge (squash merge).

## 2. Mensajes de commit (Conventional Commits)
```
<tipo>(<ámbito>): <descripción en imperativo, máx. 72 caracteres>

[cuerpo opcional: qué y por qué]

Refs: SM-12
```
Tipos: `feat`, `fix`, `refactor`, `test`, `docs`, `style`, `chore`, `ci`, `perf`.

Ejemplos:
- `feat(facturacion): agregar descuento para clientes VIP`
- `fix(impuestos): corregir redondeo del IVA a dos decimales`
- `refactor(facturacion): separar notificación del servicio`

## 3. Estilo de código
- PEP 8, formateo con `black`, revisión con `flake8`.
- Nombres descriptivos en español, funciones de máx. ~30 líneas.
- Type hints en funciones públicas y docstrings en clases/módulos.

## 4. Pruebas
- Toda funcionalidad nueva incluye pruebas unitarias (`pytest`).
- Cobertura mínima del 80 % en el módulo modificado.

## 5. Conflictos
- Quien abre el PR resuelve los conflictos en su rama (rebase sobre `develop`).
- Si el conflicto toca código de otra persona, se resuelve en pareja con ella.
- Después de resolver: correr pruebas otra vez antes de hacer push.
