
#! c:\perl64\bin

$i = 100;

print "The value of \$i is :$i \n";

$ref = \$i;

print "The address of \$i is :$ref \n";

print "The address of \$i is :",\$i, "\n";

# dereferencing

${$ref} += 10;		# incrementing the value of $i

print "The value of \$i is :$i \n";
