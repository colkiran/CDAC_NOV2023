
sub fun
{
	print "@_ \n";
	
	$_[0] = 100;
	$_[1] = 200;
}

$a = 10;
$b = 20;

print "Before :\$a - $a, \$b - $b \n";

fun($a, $b);

print "After :\$a - $a, \$b - $b \n";


print "-" x 60, "\n";
# pass by reference is important

@arr = (1..100);

%hsh = (101..200);

sub fun1
{
	print "@_ \n";
}

fun1(\@arr, \%hsh);





