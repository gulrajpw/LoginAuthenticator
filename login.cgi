#!/usr/bin/perl
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
	#if the login credentials match an entry in the database, log the user in
	#If they do not match, say try again, display redirects to create an account or
	#forgot password.

my $q = CGI->new;
my $usrnme = $q->param('usrnme');
my $pass = $q->param('pass');

#Open up the database and check to see if the credentials match.

	
print <<EOT;
Content-type:text/html

	<html>
		<body>


		</body>


	</html>

EOT

__END__


