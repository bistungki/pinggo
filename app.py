import subprocess, os, sys


def _process(cmd):
    results = []
    logfile = open(os.getcwd() + "/app.logs", "a", encoding='utf-8')
    process = subprocess.Popen(
        cmd.split(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in process.stdout:
        logs = line.decode("utf8")
        sys.stdout.write(logs)
        logfile.write(logs)
        results.append(line.decode("utf8"))
    process.wait()
    return results

if __name__ == "__main__":
    _process("ping 8.8.8.8")
