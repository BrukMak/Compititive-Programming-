class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        check1 = self.isIpv4(queryIP)
        check2 = None
        if not check1:
            check2 = self.isIpv6(queryIP)
        
        return check1 or check2 if check1 or check2 else 'Neither'
    
#     Check the string contain numbers only
    def checkDigit(self, val):
        for c in val:
            if ord(c) < 48 or ord(c) > 57:
                return False
        return True
    # Ipv4 checker
    def isIpv4(self, ip):
        ip = ip.split('.')
        if len(ip) != 4 or '' in ip:
            return ''
        for val in ip:
            if len(val) == 0 or (val[0] == '0' and len(val) > 1) or not self.checkDigit(val) or int(val) > 255:
                return ''
        return 'IPv4'
    
    # hexadecimal checker
    def checkHex(self,val):
        letters = {'A', 'B', 'C', 'D', 'E' , 'F', 'a', 'b', 'c', 'd' , 'e', 'f'}
        for c in val:
            if c not in letters and( ord(c) < 48 or ord(c) > 57):
                return False
        return True
    
    # Ipv6 checker
    def isIpv6(self, ip):
        ip= ip.split(':')
        
        if len(ip) != 8 or '' in ip:
            return ''
        for val in ip:
            if len(val) > 4 or not self.checkHex(val):
                return ''
        return 'IPv6'