#! c:\perl64\bin

$dt = "13/04/1997";

if ($dt =~ m/([0-2][1-9]|[1-3][0-1])(\/|-)(0[1-9]|1[0-2])(\2)(19[0-9]{2}|[2-9][0-9]{3})/)
{
	
	print "Match found \n";
	print "$& \n";
	
} else {
	
	print "Match not found \n";
}

