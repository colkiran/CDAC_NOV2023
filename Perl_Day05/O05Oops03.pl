
#! :]perl64\bin



#! c:\perl64\bin

# inheritence

package A;

sub fun
{
	print "funA of Package A \n";
	print $_[0], "\n";
}


# =========================================
	
package B;

sub fun
{
	print "funB of package B \n";
	print $_[0], "\n";
}

# ======================================

package C;

@ISA = qw(A, B);

sub funC
{
	print "func of Package C \n";
	print $_[0], "\n";
}


C->fun();



=cut;
C->funA()
C->FunB()
C->Func()
=cut;