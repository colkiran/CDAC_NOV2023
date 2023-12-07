
#! c:\perl64\bin

open(FW, "> myfile.txt");

$line = <stdin>;

print FW $line;

close(FW);
