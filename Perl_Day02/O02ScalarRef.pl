
#! c:\perl64\bin

$var = "Hello World";

print "$var \n";

$adr = \$var;

print "$adr :", \$var,  "\n";

print ${$adr}, "\n";

${$adr} = "perl references";

print "$var \n";

print "-" * 60, "\n";

$i = 10;

$j = \$i;

print "$i \n";

print "$j :", \$i,  "\n";

print "$i \t ${$j} \n";

${$j} += 5;

print "$i \n";
