<?php
// Ruta al script Bash
$scriptPath = "/var/www/html/scripts/script1.sh";

// Ejecuta el script Bash
$output = shell_exec("bash $scriptPath");

// Si deseas imprimir la salida del script Bash, puedes hacerlo aquí
echo "<pre>$output</pre>";
?>
