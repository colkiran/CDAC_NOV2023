
print "Hello World \n";

$i = 10;
$a = "hello";
$b = "world";

helloworld:
#decr:
	$i--;

	print "$i ";

	if ($i > 0)
	{
		#goto decr;
		goto $a.$b;		# concatenation
	}
	print "\n";