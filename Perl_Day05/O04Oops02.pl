
#! c:\perl64\bin

# inheritence

package A;

sub funA
{
	print "funA of Package A \n";
	print $_[0], "\n";
}


# =========================================

package B;

@ISA = qw(A);			# inheritance

sub funB
{
	print "funB of package B \n";
	print $_[0], "\n";
}

# ======================================

package C;

@ISA = qw(B);

sub funC
{
	print "func of Package C \n";
	print $_[0], "\n";
}


C -> funC();
C -> funA();
C -> funB();
