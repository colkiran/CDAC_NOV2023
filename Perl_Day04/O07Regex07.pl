
$st = "cat matcatbat rathatcat CATCH patmatcatrat";

# replace cat by tiger

#if ($st =~ s/cat/tiger/gi)

if ($st =~ s/(.at)/uc($1)/gie)
{
	print "Match found \n";
	print "$st \n";
} else {
	print "Match not found \n";
}