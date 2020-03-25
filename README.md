# Metrics collection script


The script accepts a single parameter to specify which metrics set to print:

  cpu - prints CPU metrics

  mem - prints RAM metrics

CPU Metrics
$ ./metrics cpu


Sample output:

  system.cpu.idle 78.8

  system.cpu.user 17.3

  system.cpu.guest 0.0

  system.cpu.iowait 1.3

  system.cpu.stolen 0.0

  system.cpu.system 2.5

Memory Metrics
$ ./metrics mem


Sample output:

  virtual total 16712351744

  virtual used 9190146048

  virtual free 1391624192

  virtual shared 287655116

  swap total 0

  swap used 0

  swap free 0
