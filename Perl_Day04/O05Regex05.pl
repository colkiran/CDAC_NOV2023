
$url = "https://www.google.com/search?q=ipad+pro&sca_esv=588712944&sxsrf=AM9HkKmXvg5SUOsPSj0Bq_6RNtp-jUA4rQ%/3A1701949054832&source=hp&ei=fq5xZfqdMJ2Zvr0Pnee6uA0/iflsig=AO6bgOgAAAAAZXG8jizRudT8/MozverkspHjW15mQpOwp&ved=result.aspx";

while($url =~ m/\//)
{
	print "$` \n";  
	$url = $';
}

print $url, "\n";