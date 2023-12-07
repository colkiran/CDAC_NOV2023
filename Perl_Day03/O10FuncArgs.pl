
sub fun(\@\%;@);

sub fun(\@\%;@)
{
	print "@_ \n";
}

@arr = (1..15);

%hsh = (a..l);

fun(@arr, %hsh, 10, 20, 30, 40, "hello")