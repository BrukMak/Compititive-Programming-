class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'
        }
        
        ans = []
        given = date.split()
        ans.append(given[-1])
        ans.append(months[given[-2]])
        if len(given[0]) == 4:
            ans.append(given[0][:2])  
        else:
            ans.append("0" + given[0][:1])
            
        
        return "-".join(ans)