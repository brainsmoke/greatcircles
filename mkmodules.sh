#!/bin/sh

DIR="$(dirname -- $0)"

MOD_DIR="$DIR/pcb/modules.pretty"
BIN_DIR="$DIR/tools/svgconvert"
mkdir -p "$MOD_DIR"

#for i in "$DIR/svg/*.svg"
for i in "$DIR/svg/v3.6.svg"
do
FILENAME="$(basename -- "$i")"

echo "$i"
echo
"$BIN_DIR/list_pcbs.py" < "$i" | while read layer; do

"$BIN_DIR/svgtokicadmod.py" --layer "${layer}" < "$i" > "$MOD_DIR/${FILENAME%.svg}-${layer}.kicad_mod"

done

done
