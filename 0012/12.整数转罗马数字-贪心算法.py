class Solution(object):
  def intToRoman(self, num):
      digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
      roman_digits = []#创建一个空列表来储存罗马数字字符
      # Loop through each symbol.
      for value, symbol in digits:
          # We don't want to continue looping if we're done.
          if num == 0: break#考虑到了数字为零的情况
          count, num = divmod(num, value)#divmod()为取整和取余数的函数，返回整数部分和余数部分
          # Append "count" copies of "symbol" to roman_digits.
          roman_digits.append(symbol * count)#将整数部分结合罗马数字字符扩充到roman_digits中
      return "".join(roman_digits)#拼接列表中字符串的方法，在每一个位置加入空字符，并拼接。
