
print "hello world \n";

$i = 10;
$a = "hello";
$b = "world";
#decr:
sub decr
{
	$i--;
	print "$i "; 
	
	if ($i > 0)
	{
		#goto decr;
		#goto $a.$b;
		goto decr;
	}
}
print "\n";
decr();