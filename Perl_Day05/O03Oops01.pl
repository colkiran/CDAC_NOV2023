
#! c:\perl64\bin

package A;

sub fun
{
		print "@_ \n";
		print "Hello World \n";
		print "Greetings Mr.$_[1], Welcome to the Event \n";
}

A -> fun("Sachin");
