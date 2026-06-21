failed_count = {}

with open("sample_auth.log", "r") as file:
    logs = file.readlines()

for log in logs:
    if "Failed password" in log:

        ip = log.split("from ")[1].strip()

        if ip in failed_count:
            failed_count[ip] += 1
        else:
            failed_count[ip] = 1

with open("report.txt", "w") as report:

    for ip, count in failed_count.items():

        if count >= 3:

            severity = "HIGH"

            print("\n🚨 ALERT 🚨")
            print("Possible Brute Force Attack")
            print("IP Address:", ip)
            print("Failed Attempts:", count)
            print("Severity:", severity)

            report.write(
                f"IP Address: {ip}\n"
                f"Failed Attempts: {count}\n"
                f"Severity: {severity}\n\n"
            )

print("\nReport saved to report.txt")
