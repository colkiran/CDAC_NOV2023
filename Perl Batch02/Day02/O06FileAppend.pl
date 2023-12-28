
#! c:\perl64\bin

open(FA, ">> myfile.txt");

print "Enter the contents of the file:";

$st = <stdin>;

print FA $st;

close FA;

