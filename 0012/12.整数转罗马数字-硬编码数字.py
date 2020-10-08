class Solution(object):
    def intToRoman(self, num):
        thousands = ["", "M", "MM", "MMM"]#4000以内的所有情况
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]#百位数的所有情况
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]#十位数的所有情况
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]#个位数的所有情况
        return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]#分别计算千百十个位数的值，得到所对应的字符串情况拼接返回结果
