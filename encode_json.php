<?php
$json = file_get_contents('credentials.json');
$encoded = base64_encode($json);
echo $encoded;