
print "Hello World \n";

$i = 10;
$a = "hello";
$b = "world";

sub decr
{
	$i--;

	print "$i ";

	if ($i > 0)
	{
		goto &decr;
	}
}

print "\n";
decr();

