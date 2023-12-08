
$st = "red rose this is blue rose a sample yellow rose";

$cntr = 0;
$stp = 2;

while ($st =~ m/(\w+)\s\brose/g)
{
	$cntr++;
	if ($cntr == $stp)
	{
		print "The second rose is $1 color \n"; 
	}
}

print "There are $cntr roses \n";
