#!/usr/bin/perl
use strict;
use warnings;

#Pass form information to .pl file containing the actual encryption
#background from http://www.pacifymind.net/nature-blur-desktop-background-10334/

#Pass the data to backend.pl


print <<EOT;
Content-type: text/html


<html>

<head> <title> CS457 </title> </head>

<center>

<h1 style="font-family:verdana;"> Login Authenticaticator </h1>

</center>

<body background="http://www.pacifymind.net/wp-content/uploads/10334d-nature-blur-picture-in-hd.jpg">






<center>
<form action="login.cgi" method="post">
	<br>
	<br>
Username: <input type="text" name="usrnme" ><br>
	<br>	
Password:  <input type="text" name="pass" ><br>
	<br>

<input type="submit" value="Login" style="font-family: 'verdana';">
</form>

<form>
<right> <input type="submit" value="Register" style="font-family: 'verdana';"></right>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</form>

</center>

<left>
<p style="font-family:verdana;">
This is a web application designed to test various encryption methods of user accounts 
for the purposes of network security. <br>This project is being designed and developed for CS457 Network Security as a project.
<p>
</left>



</body>

</html>

EOT

__END__

