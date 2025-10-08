<?php
header('Content-Type: application/json');

// Directorio donde están los reportes
$directorio = __DIR__ . "/reportes/";

// Si el directorio no existe, devolvemos un array vacío
if (!is_dir($directorio)) {
    echo json_encode([]);
    exit;
}

// Escanea los archivos en la carpeta y excluye "." y ".."
$archivos = array_values(array_diff(scandir($directorio), array('..', '.')));

// Devuelve los archivos en formato JSON
echo json_encode($archivos);
?>
