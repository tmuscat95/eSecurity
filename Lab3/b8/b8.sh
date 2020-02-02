hashcat -a 3 -m 1000 b8.txt password?l > b8_l.log
hashcat -a 3 -m 1000 b8.txt password?u > b8_u.log
hashcat -a 3 -m 1000 b8.txt password?d > b8_d.log
hashcat -a 3 -m 0 b8.txt password?l > b8_lmd5.log
hashcat -a 3 -m 0 b8.txt password?u > b8_umd5.log
hashcat -a 3 -m 0 b8.txt password?d > b8_dmd5.log
