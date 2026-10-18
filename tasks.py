   import subprocess


   def run_maintenance(cmd):
       return subprocess.run(cmd, shell=True, capture_output=True)
