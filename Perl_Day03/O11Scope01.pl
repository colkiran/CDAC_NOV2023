
#! c:\perl64\bin

our $glb = 150;

sub fun
{
	my $x = 100;
	print "lexical var \$x :$x \n";
	print "Global inside :$glb \n";
}

print "Before Global $glb \n";

fun();

print "After :$x \n";

print "Before Global $glb \n";

