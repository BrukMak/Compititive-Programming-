class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if queryIP.count('.') == 3:
            return self.isIpv4(queryIP)
        return self.isIpv6(queryIP)
    
    # Check the string contain numbers only
    
    # Ipv4 checker
    def isIpv4(self, ip):
        ip = ip.split('.')
        
        for val in ip:
            if len(val) == 0 or len(val) > 3:
                return 'Neither'
            if val[0] == '0' and len(val) != 1 or not val.isdigit() or int(val) > 255:
                return 'Neither'
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
            return 'Neither'
        for val in ip:
            if len(val) > 4 or not self.checkHex(val):
                return 'Neither'
        return 'IPv6'