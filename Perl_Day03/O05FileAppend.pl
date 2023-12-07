
open(FA, ">> myfile.txt");

$line = <stdin>;

print FA $line;

close(FA);

