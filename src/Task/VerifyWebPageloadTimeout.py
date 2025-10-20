#You want to check whether a web page loads within 3 seconds
# (performance test condition).
#load_time = 4.2
#⚠️ Page load too slow: 4.2 seconds
from contextlib import nullcontext

expetecd_Page_loadtimeout=float(input("Standard Page_ load_timeout :"))
url=str(input("Enter the URL:").strip())
Page_load_timeOut=float(input("Enter the WebPage_loadTimeOut:").strip())
if url!=nullcontext:
    print("Valid URL")
if Page_load_timeOut<=expetecd_Page_loadtimeout:
    print("performance of webPage is good: ✅")
elif Page_load_timeOut>expetecd_Page_loadtimeout and Page_load_timeOut<=4.2:
    print("⚠️ Page load too slow: loadtimeout>3<=4.2 seconds")
else:
    print("Page_load time out error: ❌")


