siteIn = input("Please Enter a Website to Block, type 'quit' to terminate. ")    #enter the first value
total = 0
scoreCounter = 0
 
while siteIn != "quit":                      #loop until the sentinel value (-1) is entered
        with open("/etc/squid/blockedsites.txt", "a") as blockFile:
            blockFile.write("\n{siteIn}")
        siteIn = input("If you have another website to block, enter it here. If not, type 'quit' to terminate. ")  
 
print ("The new sites were successfully blocked.")
