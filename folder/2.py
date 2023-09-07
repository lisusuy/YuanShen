import os
import subprocess
import pickle

# 规则1：匹配os
result1 = os.system("echo 'os command'")
print(result1)

# 规则3：匹配pickle.loads
serialized_data = b'\x80\x03X\x0b\x00\x00\x00Hello, World!q\x00.'
obj = pickle.loads(serialized_data)
print(obj)

# 规则4：匹配subprocess.call
result2 = subprocess.call(["ls", "-l"])
print(result2)

# 规则5：匹配subprocess.Popen
proc = subprocess.Popen(["echo", "subprocess.Popen"])
proc.wait()

# 规则6：匹配os.popen
stream = os.popen("echo 'os.popen command'")
output = stream.read()
print(output)

# 规则7：匹配subprocess.run
result3 = subprocess.run(["echo", "subprocess.run"])
print(result3)

# 规则8：匹配getstatusoutput
import commands  # This is for demonstration purposes only, as it may not work in all Python environments.
result4 = commands.getstatusoutput("echo 'getstatusoutput command'")
print(result4)

# 规则9：匹配eval
eval("print('eval command')")

# 规则10：匹配exec
exec("print('exec command')")

# 规则11：匹配compile
code = compile("print('compile command')", "<string>", "exec")
exec(code)

# 规则12：匹配execfile
try:
    execfile("nonexistent_file.py")  # This will raise an exception since the file does not exist.
except Exception as e:
    print(e)

# 规则13：匹配getoutput
import commands  # This is for demonstration purposes only, as it may not work in all Python environments.
output2 = commands.getoutput("echo 'getoutput command'")
print(output2)