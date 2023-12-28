

#! c:\perl64\bin

opendir(DH, "C:\\Training\\Perl Files\\CDAC\\Batch02\\Day02");

while ($filename = readdir(DH))
{
	if ($filename =~ m/\.pl$/i)
	{
		print $filename, "\n";
	}
}

closedir DH;


=cut;
@filename = readdir(DH);

for ($i = 0; $i <= $#filename; $i++)
{
	print $filename[$i], "\n";
}

closedir DH;
