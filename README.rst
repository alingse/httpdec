
httpdec  
========

a tool can decode http headers | cookies | query | body from clipboard or file


httpdec -d h input output

httpdec -d c input output

httpdec -d h -p

httpdec -d c -p


clippaste|httpdec -d h|jq -r '.Cookie'|httpdec -d c|clipcopy
