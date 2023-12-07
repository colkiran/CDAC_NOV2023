
sub fun
{
	print "@_ \n";
	
	$x = $_[0];
	$y = $_[1];
	
	$x = 100;
	$y = 300;
	
	print "\$x - $x, \$y - $y \n";
	print $x + $y, "\n";
	
	
}

$a = 10;
$b = 20;

print "Before :\$a - $a \t \$b - $b \n";

fun($a, $b);

print "After :\$a - $a \t \$b - $b \n";

# ==================================================
print "=" x 60, "\n";
print "=" x 60, "\n";

sub fun1
{
	print "@_ \n";
	
	$x = shift(@_);
	$y = shift(@_);
	
	$x = 100;
	$y = 300;
	
	print "\$x - $x, \$y - $y \n";
	print $x + $y, "\n";
	
	
}

$a = 10;
$b = 20;

print "Before :\$a - $a \t \$b - $b \n";

fun($a, $b);

print "After :\$a - $a \t \$b - $b \n";
