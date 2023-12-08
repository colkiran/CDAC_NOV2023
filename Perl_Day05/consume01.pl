
#use warnings;
# use strict;

BEGIN {
	unshift(@INC, "C:\\Training\\Perl Files\\CDAC\\Perl_Day05") ;
}

use mymodule;

greet("Sathish");

print "-" x 60, "\n";

print "@cities \n";

=cut;



print "-" x 60, "\n";

# print "@INC \n";

for (my $i=0; $i<=$#INC; $i++)
{
	print $INC[$i]," \n";
}

#print %INC, "\n";

print "-" x 60, "\n";

for my $k (keys(%INC))
{
	print "$k => $INC{$k} \n";
}


