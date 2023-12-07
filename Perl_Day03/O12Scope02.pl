
sub fun1
{
	print "fun1 code....\n";
	my $lx = 100;
	local $lcl = 500;
	print "$lcl \n";
	fun2();
	
}


sub fun2
{
	print "fun2 code.....\n";
	
	print "-" x 60, "\n";
	print "Local Variable :$lcl \n";
	print "Lexical Variable :$lx \n";
	fun3();
}


sub fun3
{
	print "fun3 - Local Variable :$lcl \n";
}

fun1()

	