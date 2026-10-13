# SoftMarket · Módulo de Facturación

Repositorio de ejemplo de la propuesta de buenas prácticas para SoftMarket S.A.
(Buenas Prácticas de Desarrollo de Software, CUC).

## Estructura

```
src/facturacion/
  modelos.py      # entidades (Cliente, Item, Factura)
  descuentos.py   # políticas de descuento (OCP)
  impuestos.py    # IVA por país (SRP/OCP)
  puertos.py      # interfaces Repositorio y Notificador (ISP/DIP)
  servicio.py     # ServicioFacturacion: orquesta el proceso
tests/            # pruebas unitarias con pytest
legacy/           # código original, solo como referencia del diagnóstico
```

## Ramas

| Rama | Uso |
|---|---|
| `main` | Código en producción. Solo recibe merges desde `release/*` y `hotfix/*`. Cada merge lleva tag `vX.Y.Z`. |
| `develop` | Integración de la siguiente versión. |
| `feature/SM-<id>-<descripcion>` | Una funcionalidad o refactor; sale de `develop` y vuelve por Pull Request. |
| `release/X.Y.0` | Estabilización antes de publicar. |
| `hotfix/X.Y.Z-<descripcion>` | Corrección urgente desde `main`. |

## Cómo correr

```bash
pip install pytest flake8 black
PYTHONPATH=src pytest -q
```

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de hacer tu primer commit.
