test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL"]

def get_TestStatus(status):
    return status == "PASS"

teststatus_result=list(filter(get_TestStatus,test_results))
print(teststatus_result)


