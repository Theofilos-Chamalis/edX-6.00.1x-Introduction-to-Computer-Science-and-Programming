# Paste your code into this box
def solve(strs):
  maxx = '';
  for i in xrange(len(strs)):
      for j in xrange(i+1, len(strs)):
          q = strs[0];
          s = strs[i:j+1];
          if ''.join(sorted(s)) == s:
              maxx = max(maxx, s, key=len)
          else:
              break;
  if maxx == '' :
      return q;
  else:
      return maxx;
  
print solve(s);