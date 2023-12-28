
#! c:\perl64\bin

open(FW, "> myfile.txt");

$choice = "yes";

$st = "";

while ($choice eq "yes")
{

	print "Enter the contents of the file :";

	$st = $st . <stdin>;
	
	print "Do you want to continue :(yes / no)";
	
	$choice = <stdin>;
	
	chomp($choice);
}

print FW $st;

close FW;
