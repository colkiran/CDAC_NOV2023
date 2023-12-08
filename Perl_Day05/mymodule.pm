

#sub greet(\$;@);

our $guest = "Sachin Tendulkar";

@cities = ("Mumbai", "Chennai", "Delhi", "Bangalore", "Hyderabad", "Bhopal");


sub greet
{
	print "@_ \n";
	
  	$gst = $_[0];
	print "Welcome Mr.$gst, Welcome to the event \n";
	
}

1;
