
#! c:\perl64\bin

open(FL, "< data.txt");

while (<FL>)			# data will get streamed from the file
{
	print "$_ \n";
}

close(FL)