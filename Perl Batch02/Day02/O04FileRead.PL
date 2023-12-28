
#! c:\perl64\bin

open(FL, "< data.txt") || die("file not found \n");;

# read FL, $str, 500;

# print $str;

while (<FL>)
{
	print $_;
}
close FL;

