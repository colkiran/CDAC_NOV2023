

#! c:\perl64\bin

sub greet
{
	print "Greetings Mr.Sachin, Welcome to the event...\n";
}

greet();

print "-" x 60, "\n";

sub greetGst
{
	print "@_ \n";
	print "Greetings Mr.$_[0], Welcome to the event....\n";
}

greetGst("Sachin", "Tendulkar", "Ramesh", 10, 20, 30);

print "-" x 60, "\n";

sub add
{
	print $_[0] + $_[1],  "\n";
}


add(10, 20);


print "-" x 60, "\n";

sub prod
{
	return $_[0] * $_[1];
}

$a = 10; $b = 5;

print "The product of $a and $b is :", prod($a, $b), "\n";
