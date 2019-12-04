# SquidProxyServer
An implementation of the popular Squid Proxy service using SSL Bump as an Intercepting Proxy; with custom error pages for website filtering and SquidAnalyzer service for proxy traffic analytics.

*By: Sal Trupiano and Travis Thayer* | *CSI-3660: System Administration* | *Oakland University*



To get started, please follow these steps:

  1) Download this repository to your CentOS machine running an the httpd (Apache) service.
  2) Place the contents in the 'html_files' folder in /var/www/html/ directory (or wherever your Document Root may be).
  3) Place the entire 'common' folder in /var/www/html/ directory (or wherever your Document Root may be).
  4) Now, navigate to your server's IP address/port used for httpd.
  5) You should see the entire webpage show up, as seen in the presentation.
  6) Follow the steps on the "Project Overview" page to establish/configure our service completely.

Implementation of the service was shared between Sal Trupiano and Travis Thayer.
Design and implementation of the service information webpage was by Sal Trupiano, edited and updated by Travis Thayer.

Configuration files that are cusomized are located in the "common" folder.
The following script files in the "common" folder have been customized:
- ERR_CUSTOMPAGE.html (custom error page for Squid content filtering)
- httpd.conf (customized Apache configuration file)
- myCA.der (custom-generated root certificate authority file for client download)
- squid.conf (customized configuration file for Squid proxy service)
- squidanalyzer.conf (customized configuration file for Squid Analyzer)

All files with customized statements will have a comment with four stars within the code, indicating a summary of what has been changed, and who made the change, as well as citations if the code was sourced from an exterior location.
