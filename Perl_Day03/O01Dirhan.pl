
opendir(DIRHAN, "c:\\windows");
$count =0;

while ($files = readdir(DIRHAN))
{
	if ($files =~ m/\.log$/)			# =~ equal operator in regex
	{
		print "$files \n";
		$count++;
=cut;	
		open(FL, "< c:\\windows\\$files");
		
		while (<FL>)
		{
			print "$_ \n";
		}
		close(FL);
=cut;
	}
}

print "-" x 60, "\n";
print "There are $count files in the directory.\n";
print "-" x 60, "\n";
closedir(DIRHAN);
