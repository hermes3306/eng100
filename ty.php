<?php

while (true) {
	$Day0		= "2020-12-05";
	$Day0       = strtotime($Day0);
	$DayN       = strtotime(date("Y-m-d"));
	$N      = ($DayN - $Day0)/60/60/24;

	$fname = "/home/pi/code/eng100/" . $N . ".txt";
	$handle = fopen($fname, "r");
	if ($handle) {
    	while (($line = fgets($handle)) !== false) {
			echo $line;
			sleep(3);
    	}
    	fclose($handle);
	} else {
    	// error opening the file.
	} 
	echo "*";
	sleep(10);
	system('clear');
}

?>

