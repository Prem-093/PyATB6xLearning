response_times_ms = [1200, 1500, 1800]

def time_sec(time):
    return time/1000

response_time=list(map(time_sec,response_times_ms))
print(response_time)

