
$st = "abc cab bac bbc cable table cca cnn cba";

if ($st =~ tr/abc/xyz/)
{
	print "Match found \n";
	print "$st \n";
} else {
	print "Match not found \n";
}