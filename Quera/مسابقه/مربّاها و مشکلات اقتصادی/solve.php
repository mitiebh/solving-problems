<?php
$handle = fopen ("php://stdin","r");

$line1 = fgets($handle);
$line1 = explode(' ' , $line1);
$line2 = fgets($handle);
$line2 = explode(' ', $line2);

$jars = $line1[0];
$capacity = intval($line1[1]);

$sum = array_sum($line2);
$total_jars_used = intval(ceil(($sum/$capacity)));
$remaining = $jars - $total_jars_used;
echo $remaining;
