
#! C:\perl64\bin

$st = "the quick brown fox jumps over the lazy dog";

if ($st =~ m/\bfox/)
{
	print "Match found \n";
	print "String that did not match regex 		- $` \n";
	print "String that matched the regex 		- $& \n";
	print "String that is yet to be chcecked 	- $' \n";
} else {
	print "Match not found \n";
}
