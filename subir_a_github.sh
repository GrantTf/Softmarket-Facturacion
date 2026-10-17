#!/usr/bin/env bash
# Sube el repositorio de ejemplo con TODAS sus ramas y tags a GitHub.
# Uso:  1) Crea en GitHub un repositorio VACÍO (sin README) llamado softmarket-facturacion
#       2) Descomprime softmarket-facturacion.zip y entra a la carpeta
#       3) bash subir_a_github.sh https://github.com/TU_USUARIO/softmarket-facturacion.git
set -e
URL="$1"
[ -z "$URL" ] && { echo "Falta la URL del repositorio"; exit 1; }
git remote remove origin 2>/dev/null || true
git remote add origin "$URL"
git push -u origin --all
git push origin --tags
echo "Listo. En GitHub ve a Settings > Branches y protege 'main' y 'develop'."
